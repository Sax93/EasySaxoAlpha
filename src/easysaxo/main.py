"""======================= Main =======================
EasySaxo main file for execution.

Author: SXF
Description: App that holds EasySaxo main menu
"""
# NOTE: `main.py` is the file that has to be debugged/executed for the program to fully work.
# Runs main processes like command input and user data processing

import json
import os
import readline  # ruff: ignore[unused-import]
import shutil
import subprocess
import sys
import unicodedata

# Set environment before loading Pygame/Rich integrations
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from rich import print
from rich.console import Console

console = Console()


def s_interrupt_hook(exctype, value, traceback):
    if exctype is KeyboardInterrupt:
        console.print("\n[bold yellow]Loading cancelled by user.[/bold yellow]\n[bold red]Exiting.[/bold red]")
        sys.exit(0)
    else:
        sys.__excepthook__(exctype, value, traceback)


sys.excepthook = s_interrupt_hook

console.print("[bold cyan]Loading EasySaxo...[/bold cyan]")

# Project imports
from .config import COMMAND_REGISTRY, clr, easysaxo
from .esmodules import dirloct
from .esmodules.heavyholder import SessionManager, ThreadData

sys.stdout.write(f"\x1b]2;{easysaxo.name} {easysaxo.ver}\x07")
sys.stdout.flush()


# = session info process

def session_info_proc(session_info):
    if session_info is None:
        preboot_file = None
        if len(sys.argv) > 1:
            if sys.argv[1].lower() == "load" and len(sys.argv) > 2:
                preboot_file = sys.argv[2]
            elif sys.argv[1].endswith(".json"):
                preboot_file = sys.argv[1]
        session_info = SessionManager.load_session(preboot_file)

    if isinstance(session_info, dict):
        ThreadData.current_user = session_info.get("user_name", "User")
        ThreadData.current_pswd = session_info.get("password")
    else: ThreadData.current_user = session_info

    return session_info


# 1

def sysh(cmd: str):
    _no_return_code_flag = False
    try:
        parts = cmd.split()

        flags = [p for p in parts if p.startswith("-<") and p != "-s"]
        _no_return_code_flag = "-<silent" in flags
        p_cmd = [p for p in parts if not p.startswith("-<")]

        subprocess.run(p_cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        if not _no_return_code_flag:
            console.print(
                f"\n[bold red]Result from command '[bold yellow]{cmd}[/bold yellow]' returned exit code [bold magenta]{e.returncode}[/bold magenta]:[/bold red]\n"
                f"[dim red]{e}[/dim red]"
            )
        return
    except (PermissionError, TypeError, AttributeError, KeyboardInterrupt) as err:
        easysaxo.k_log("9")
        if not _no_return_code_flag: console.print(f"[bold red]System command exception:[/bold red] [bright_red]{err}[/bright_red]")
        else: print()


def inp_display(identifier: str) -> str:
    if ThreadData.path_display:
        path_helper = f"[dim cyan]{dirloct.DirLocation.get_display_path()}[/dim cyan]"
        console.print(path_helper)
    
    # ansi formatted str for terminal display
    return f"\033[1;35m{identifier}\033[0m \033[1;34m>\033[0m "


# 2

def trslt(translations):
    tr_file = dirloct.DirLocation._resolve_path("-<root\\translations.json")
    if os.path.exists(tr_file):
        with open(tr_file, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
            for key, val in raw_data.items():
                if isinstance(val, dict): translations.update(val)
                else: translations[key] = val


def kb_inter_holder():
    try:
        extoken = console.input("\n[bold yellow]Want to exit? (Y/N): [/bold yellow]").strip().lower()
        if not extoken: return
        if extoken == "y":
            easysaxo.k_log("a0")
            SessionManager.save_session(ThreadData.current_user)
            console.print("[bold red]Session saved. Exiting...[/bold red]")
            sys.exit(0)
    except (KeyboardInterrupt, EOFError):
        easysaxo.k_log("a0")
        sys.exit()


def Core(session_info=None):
    from . import commands  # Do not remove this import.  # ruff: ignore[unused-import]
    easysaxo.mute = ThreadData.log_muter

    session_info_proc(session_info)

    translations = {}
    trslt(translations)

    console.print(f"[dim blue]Root Directory:[/dim blue] [dim bright_cyan]{dirloct.base_dir}[/dim bright_cyan]")

    all_commands = list(COMMAND_REGISTRY.keys()) + list(translations.keys())

    try:
        import readline

        def completer(text, state):
            options = [c for c in all_commands if c.startswith(text)]
            return options[state] if state < len(options) else None

        readline.set_completer(completer)
        readline.parse_and_bind("tab: complete")
    except ImportError: pass

    while True:
        usit = None
        try:
            print()
            raw_prompt = inp_display(ThreadData.current_user)
            usit = input(raw_prompt).strip()
        except (KeyboardInterrupt, EOFError): kb_inter_holder()

        if not usit: continue

        usit = unicodedata.normalize("NFKC", usit).strip()

        override_mode = None
        if usit.endswith(" -e") or usit.startswith("> "):
            override_mode = "easysaxo"
            usit = usit[:-2].strip() if usit.endswith(" -e") else usit[2:].strip()
        elif usit.endswith(" -s") or usit.startswith("$ "):
            override_mode = "system"
            usit = usit[:-2].strip() if usit.endswith(" -s") else usit[2:].strip()

        effective_mode = override_mode if override_mode is not None else getattr(ThreadData, "target_mode", "auto")

        parts = usit.split(maxsplit=1)
        cmd = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else None

        if cmd in translations: cmd = translations[cmd]

        in_easysaxo = cmd in COMMAND_REGISTRY
        sys_binary = shutil.which(cmd)

        if effective_mode == "system":  # forced syscmd
            if sys_binary: sysh(usit)
            else: console.print(f"[bold red]System command '[bold yellow]{usit}[/bold yellow]' not found in PATH.[/bold red]")

        elif effective_mode == "easysaxo":  # forced escmd
            if in_easysaxo: COMMAND_REGISTRY[cmd](arg)
            else: console.print(f"[bold red]EasySaxo command '[bold yellow]{cmd}[/bold yellow]' not found.[/bold red]")

        else:  # auto mode
            if in_easysaxo: COMMAND_REGISTRY[cmd](arg)
            elif sys_binary: sysh(usit)
            else:
                easysaxo.k_log("1")
                console.print("[bold red]Unknown command.[/bold red] [dim white]Type '[bold cyan]help[/bold cyan]' for assistance.[/dim white]")

def run():
    clr()
    preboot_file = None
    # session loader
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "load" and len(sys.argv) > 2: preboot_file = sys.argv[2]
        elif sys.argv[1].endswith(".json"): preboot_file = sys.argv[1]

    session_data = SessionManager.load_session(preboot_file)
    if isinstance(session_data, dict):
        ThreadData.current_user = session_data.get("user_name", "User")
        ThreadData.current_pswd = session_data.get("password")
        ThreadData.path_display = session_data.get("pathdisplay", False)
        ThreadData.target_mode = session_data.get("target_mode", "auto")
    else: ThreadData.current_user = session_data

    import bcrypt

    try:
        if ThreadData.current_pswd is not None:  # password checker
            while True:
                keyacc = console.input("[bold light_salmon3]Insert password: [/bold light_salmon3][dim bright_black](Press Enter to cancel)[/dim bright_black] ")
                try: is_valid = bcrypt.checkpw(keyacc.encode('utf-8'), ThreadData.current_pswd.encode('utf-8'))
                except (TypeError, ValueError): is_valid = False
                if is_valid:
                    console.print("[bold green]✔ Access granted. Opening app...[/bold green]")
                    clr()
                    break
                console.print("[bold red]Wrong password, try again.[/bold red]\n")
        Core(session_info=session_data)
    except KeyboardInterrupt:
        easysaxo.k_log("a1")
        sys.exit()

if __name__ == "__main__": run()