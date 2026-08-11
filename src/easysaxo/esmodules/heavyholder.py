#=================================================
# Threading + Session Saving-Loading
#=================================================

# `heavyholder.py` ONLY FOR COMPLEX TASK & OVERLAP COMMAND DEFINING
# you know what else is heavy?

import threading, time
from colorama import Fore, Style
from .dirloct import base_dir, DirLocation

try:
    from prompt_toolkit.formatted_text import HTML
    from prompt_toolkit import print_formatted_text
    PROMPT_TOOLKIT_AVAILABLE = True
except ImportError:
    PROMPT_TOOLKIT_AVAILABLE = False
    HTML = None
    print_formatted_text = None

class ThreadData:
    current_user = "User"
    current_pswd = None
    target_mode = "auto"
    # why storing this here? to make ezsaxo less comprehensible

    @staticmethod
    def getthreads():
        print(f"Active background threads: {Fore.GREEN}{threading.active_count()}{Style.RESET_ALL}")

    @staticmethod
    def _timer_task(seconds, message):
        time.sleep(seconds)
        if PROMPT_TOOLKIT_AVAILABLE: print_formatted_text(HTML(f"<ansiyellow>==== [TIMER ALERT]: {message} ====</ansiyellow>"))
        else: print(f"\n{Fore.YELLOW}==== [TIMER ALERT]: {message} ===={Style.RESET_ALL}\n")

    @staticmethod
    def set_timer(seconds, message):
        try:
            sec = int(seconds)
            msg = message if message else "Timer finished!"
            threading.Thread(target=ThreadData._timer_task, args=(sec, msg), daemon=True).start()
            print(f"Timer set for {Fore.CYAN}{sec} seconds{Style.RESET_ALL} in the background.")
        except ValueError: print(f"{Fore.RED}Please provide a valid integer for seconds.{Style.RESET_ALL}")
        
import json, os
from .lister import MathList

class SessionManager:
    active_session_file = os.path.join(base_dir, "session.json")
    
    @staticmethod
    def save_session(user_name: str = None, filepath: str = None):
        uname = user_name if user_name else ThreadData.current_user
        target = DirLocation._resolve_path(filepath) if filepath else SessionManager.active_session_file
        user_vars = {k: v for k, v in MathList.mathset.items() if k not in MathList._reserved}
        try:
            with open(target, "w", encoding="utf-8") as f:
                json.dump({
                    "user_name": uname, 
                    "variables": user_vars, 
                    "password": ThreadData.current_pswd
                }, f, indent=4)
            SessionManager.active_session_file = target
            print(f"{Fore.GREEN}Session saved successfully to '{os.path.basename(target)}'.{Style.RESET_ALL}")
        except Exception as e: print(f"{Fore.RED}Error saving session: {e}{Style.RESET_ALL}")

    @staticmethod
    def load_session(filepath: str = None) -> dict:
        target = DirLocation._resolve_path(filepath) if filepath else SessionManager.active_session_file
        default_data = {"user_name": "User", "password": None}
        if not os.path.exists(target): 
            return default_data

        try:
            # check if file is empty (0 bytes) before attempting json.load
            if os.path.getsize(target) == 0:
                return default_data

            with open(target, "r", encoding="utf-8") as f: 
                data = json.load(f)

            user_name = data.get("user_name", "User")
            password = data.get("password", None)

            for k in [k for k in MathList.mathset.keys() if k not in MathList._reserved]: 
                del MathList.mathset[k]
            for var_name, value in data.get("variables", {}).items(): 
                MathList.mathset[var_name] = value

            SessionManager.active_session_file = target
            print(f"{Fore.CYAN}Loaded '{os.path.basename(target)}' for user '{user_name}'.{Style.RESET_ALL}")
        
            return {"user_name": user_name, "password": password}
        
        except (json.JSONDecodeError, Exception) as e:
            print(f"{Fore.RED}Failed to load session: {e}{Style.RESET_ALL}")
            return default_data
        
# 100 lines? there u go

# set command

def set_stat(arg):
    if not arg: print(f"{Fore.RED}Usage: set <setting> <name> [value]{Style.RESET_ALL}")
    else:
        parts = arg.split(maxsplit=2)
        # edit username
        if parts[0].lower() == "name" and len(parts) >= 2:
            ThreadData.current_user = parts[1]
            print(f"User name replaced to {Fore.GREEN}{parts[1]}{Style.RESET_ALL}.")
            SessionManager.save_session(ThreadData.current_user)
            
        # edit/add variable
        elif parts[0].lower() in ["var", "variable"] and len(parts) == 3:
            from .mathf import MathFunc
            MathFunc.set_var(parts[1], parts[2]); SessionManager.save_session(ThreadData.current_user)
        
        # set new password
        elif parts[0].lower() in ["password", "key", "pswd"] and len(parts) >= 2:
            import bcrypt
            plain_pwd = parts[1].encode('utf-8')
            hashed_bytes = bcrypt.hashpw(plain_pwd, bcrypt.gensalt())
            ThreadData.current_pswd = hashed_bytes.decode('utf-8')
            print(f"Password assigned successfully. It will load {Fore.MAGENTA}next session{Style.RESET_ALL}.")
            SessionManager.save_session(ThreadData.current_user)
        
        # set command match
        elif parts[0].lower() in ["cmdmatch", "cmdrun", "mode"] and len(parts) >= 2:
            mode_arg = parts[1].lower()
            if mode_arg in ["sys", "path", "device", "s"]: # system
                ThreadData.target_mode = "system"
                print(f"{Fore.LIGHTGREEN_EX}Default execution mode set to: System Shell{Style.RESET_ALL}")
            elif mode_arg in ["es", "app", "local", "e"]: # app
                ThreadData.target_mode = "easysaxo"
                print(f"{Fore.LIGHTCYAN_EX}Default execution mode set to: {easysaxo.name} Shell (Internal){Style.RESET_ALL}")
            else: # auto
                ThreadData.target_mode = "auto"
                print(f"{Fore.LIGHTYELLOW_EX}Default execution mode set to: Auto (EasySaxo -> System){Style.RESET_ALL}")
                print(f"You can either use {Fore.CYAN}'-e'{Style.RESET_ALL} to force app command, or {Fore.CYAN}'-s'{Style.RESET_ALL} to force system command!")
                
        else: print(f"{Fore.RED}Unknown/malformed set subcommand.{Style.RESET_ALL}")