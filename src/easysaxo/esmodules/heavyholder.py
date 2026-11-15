"""Threading and heavytask holder for EasySaxo"""

# `heavyholder.py` ONLY FOR COMPLEX TASK & OVERLAP COMMAND DEFINING
# you know what else is heavy?

import threading
import time

from rich import print

from ..config import easysaxo
from .dirloct import DirLocation, base_dir

try:
    from prompt_toolkit import print_formatted_text
    from prompt_toolkit.formatted_text import HTML
    PROMPT_TOOLKIT_AVAILABLE = True
except ImportError:
    PROMPT_TOOLKIT_AVAILABLE = False
    HTML = None
    print_formatted_text = None


class ThreadData:
    """Manages global thread state, active user runtime variables
    and asynchronous background tasks.
    """

    current_user = "User"
    current_pswd = None
    target_mode = "auto"
    path_display = False
    log_muter = True

    @staticmethod
    def getthreads(): print(f"Active background threads: [green]{threading.active_count()}[/green]")

    @staticmethod
    def _timer_task(seconds, message):
        time.sleep(seconds)
        if PROMPT_TOOLKIT_AVAILABLE: print_formatted_text(HTML(f"<ansiyellow>==== [TIMER ALERT]: {message} ====</ansiyellow>"))
        else: print(f"\n[yellow]==== [TIMER ALERT]: {message} ====[/yellow]\n")

    @staticmethod
    def set_timer(seconds, message):
        try:
            sec = int(seconds)
            msg = message or "Timer finished!"
            threading.Thread(target=ThreadData._timer_task, args=(sec, msg), daemon=True).start()
            print(f"Timer set for [cyan]{sec} seconds[/cyan] in the background.")
        except ValueError:
            easysaxo.k_log("6")
            print("[red]Please provide a valid integer for seconds.[/red]")

import json
import os

from .lister import MathList


class SessionManager:
    """Handles persistence for user workspace settings, environment variables,
    and authentication state via JSON storage.
    """

    active_session_file = os.path.join(base_dir, "session.json")

    @staticmethod
    def save_session(user_name: str | None, filepath: str | None = None):
        uname = user_name or ThreadData.current_user
        target = DirLocation._resolve_path(filepath) if filepath else SessionManager.active_session_file
        user_vars = {k: v for k, v in MathList.mathset.items() if k not in MathList._reserved}
        
        try:
            with open(target, "w", encoding="utf-8") as f:
                json.dump({
                    "user_name": uname,
                    "variables": user_vars,
                    "password": ThreadData.current_pswd,
                    "path_display": ThreadData.path_display,
                    "log_muter": ThreadData.log_muter
                }, f, indent=4)
            SessionManager.active_session_file = target
            print(f"[green]Session saved successfully to '{os.path.basename(target)}'.[/green]")
        except (PermissionError, FileNotFoundError, KeyboardInterrupt) as e: 
            easysaxo.k_log("4" if isinstance(e, PermissionError) else "5" if isinstance(e, FileNotFoundError) else "11")
            print(f"[red]Error saving session: {e}[/red]")

    @staticmethod
    def load_session(filepath: str | None) -> dict:
        target = DirLocation._resolve_path(filepath) if filepath else SessionManager.active_session_file
        default_data = {"user_name": "User", "password": None}
        if not os.path.exists(target):
            print("[yellow]File not specified or found. Default data loaded.[/yellow]")
            return default_data

        try:
            # check if file is empty before attempting json.load
            if os.path.getsize(target) == 0: return default_data

            with open(target, "r", encoding="utf-8") as f: data = json.load(f)

            user_name = data.get("user_name", "User")
            password = data.get("password", None)

            for k in [k for k in MathList.mathset if k not in MathList._reserved]: del MathList.mathset[k]
            for var_name, value in data.get("variables", {}).items(): MathList.mathset[var_name] = value

            SessionManager.active_session_file = target
            print(f"[cyan]Loaded '{os.path.basename(target)}' for user '{user_name}'.[/cyan]")

            return {
                "user_name": user_name,
                "password": password,
                "pathdisplay": data.get("pathdisplay", False),
                "log_muter": data.get("log_muter", True)
            }

        except (json.JSONDecodeError, ImportError, FileNotFoundError, KeyboardInterrupt) as e:
            easysaxo.k_log("11" if isinstance(e, KeyboardInterrupt) else "5" if isinstance(e, FileNotFoundError) else "3")
            print(f"[red]Failed to load session: {e}[/red]")
            return default_data

# set command

def set_stat(arg):
    if not arg:
        easysaxo.k_log("2")
        print("[red]Usage: set <setting> <name> [value][/red]")
        return

    parts = arg.split(maxsplit=2)

    # edit username
    if parts[0].lower() == "name" and len(parts) >= 2:
        ThreadData.current_user = parts[1]
        print(f"User name replaced to [green]{parts[1]}[/green].")
        SessionManager.save_session(ThreadData.current_user)

    # edit/add variable
    elif parts[0].lower() in ["var", "variable"] and len(parts) == 3:
        from .mathf import MathFunc
        MathFunc.set_var(parts[1], parts[2])
        SessionManager.save_session(ThreadData.current_user)

    # set new password
    elif parts[0].lower() in ["password", "key", "pswd"] and len(parts) >= 2:
        import bcrypt
        plain_pwd = parts[1].encode('utf-8')
        hashed_bytes = bcrypt.hashpw(plain_pwd, bcrypt.gensalt())
        ThreadData.current_pswd = hashed_bytes.decode('utf-8')
        print("Password assigned successfully. It will load [magenta]next session[/magenta].")
        SessionManager.save_session(ThreadData.current_user)

    # set command match
    elif parts[0].lower() in ["cmdmatch", "cmdrun", "mode"] and len(parts) >= 2:
        mode_arg = parts[1].lower()
        if mode_arg in ["sys", "path", "device", "s"]: # system
            ThreadData.target_mode = "system"
            print("[lightgreen]Default execution mode set to: System Shell[/lightgreen]")
        elif mode_arg in ["es", "app", "local", "e"]: # app
            ThreadData.target_mode = "easysaxo"
            print(f"[lightcyan]Default execution mode set to: {easysaxo.name} Shell (Internal)[/lightcyan]")
        else: # auto
            ThreadData.target_mode = "auto"
            print("[lightyellow]Default execution mode set to: Auto (EasySaxo -> System)[/lightyellow]")
            print("Use [cyan]'-e'[/cyan] to force app command, or [cyan]'-s'[/cyan] to force system command.")

    # set name <-> path display
    elif parts[0].lower() in ["pathmode", "pathdisplay"] and len(parts) >= 2:
        path_arg = parts[1].lower()
        if path_arg in ["on", "enable"]:
            ThreadData.path_display = True
            print("[lightgreen]Path mode enabled.[/lightgreen]")
        elif path_arg in ["off", "disable"]:
            ThreadData.path_display = False
            print("[lightred]Path mode disabled.[/lightred]")
        else:
            easysaxo.k_log("1") 
            print("[red]Unknown/malformed subcommand.[/red]")
        SessionManager.save_session(ThreadData.current_user)
    else:
        easysaxo.k_log("1")
        print("[red]Unknown/malformed set subcommand.[/red]")