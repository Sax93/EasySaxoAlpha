"""======================= Main ======================="""
# NOTE: `main.py` is the file that has to be debugged/executed for the program to fully work.
# Runs main processes like command input and user data processing
# Ironically, it is not the most dangerous file to modify

import sys, os, unicodedata, time, shlex, subprocess, shutil
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1" # was tired of the pygame msg
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0" # tensorflow hide msgs

# if this code works, it was written by sxf
# if it doesnt, ion know who did :p

# =================================================
# Import section
# =================================================
from .config import easysaxo, COMMAND_REGISTRY, clr
from . import commands
from .esmodules.heavyholder import ThreadData, SessionManager

# Rich support
try:
    from rich.console import Console
    from rich.table import Table
    console = Console()
    RICH_AVAILABLE = True
except ImportError: RICH_AVAILABLE = False

# Prompt_Toolkit support
try:
    from prompt_toolkit import PromptSession
    from prompt_toolkit.completion import WordCompleter
    from prompt_toolkit.patch_stdout import patch_stdout
    PROMPT_TOOLKIT_AVAILABLE = True
except ImportError: PROMPT_TOOLKIT_AVAILABLE = False

from colorama import Fore, Style, just_fix_windows_console
just_fix_windows_console()

#=================================================
# Core main loop
#=================================================
def Core(session_info=None):
    enable_ee = False
    scee = True
    import json
    from pathlib import Path
    
    Tdir = Path(__file__).resolve().parent
    TRANSLATIONS_FILE = Tdir / "translations.json"
    
    translations = {}
    if TRANSLATIONS_FILE.exists():
        with open(TRANSLATIONS_FILE, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
            for key, val in raw_data.items():
                if isinstance(val, dict): translations.update(val)
                else: translations[key] = val

    if session_info is None:
        preboot_file = None
        if len(sys.argv) > 1:
            if sys.argv[1].lower() == "load" and len(sys.argv) > 2: preboot_file = sys.argv[2]
            elif sys.argv[1].endswith(".json"): preboot_file = sys.argv[1]

        session_info = SessionManager.load_session(preboot_file)

    if isinstance(session_info, dict):
        ThreadData.current_user = session_info.get("user_name", "User")
        ThreadData.current_pswd = session_info.get("password")
    else: ThreadData.current_user = session_info
    
    from .esmodules.dirloct import base_dir
    print(f"{Fore.LIGHTBLACK_EX}Default path: {base_dir}{Style.RESET_ALL}")
    print(f"Welcome to {Fore.CYAN}{easysaxo.name}{Style.RESET_ALL}! Insert commands down below.")

    all_commands = list(COMMAND_REGISTRY.keys()) + list(translations.keys())

    if PROMPT_TOOLKIT_AVAILABLE:
        completer = WordCompleter(all_commands, ignore_case=True)
        session = PromptSession(completer=completer)
    else:
        try:
            import readline
            def completer(text, state):
                options = [c for c in all_commands if c.startswith(text)]
                return options[state] if state < len(options) else None
            readline.set_completer(completer)
            readline.parse_and_bind("tab: complete")
        except ImportError: pass

    # ==== Main Loop ====
    
    while True:
        try:
            print()
            prompt_str = Fore.BLACK + Style.BRIGHT + f"{ThreadData.current_user} > " + Style.RESET_ALL
            if PROMPT_TOOLKIT_AVAILABLE:
                with patch_stdout(): usit = session.prompt(f"{ThreadData.current_user} > ").strip()
            else: usit = input(prompt_str).strip()
            
        except KeyboardInterrupt:
            try:
                extoken = input(f"\n{Fore.LIGHTBLACK_EX}Want to exit? (Y/N): {Style.RESET_ALL}").lower()
                if extoken == "y":
                    SessionManager.save_session(ThreadData.current_user)
                    break
                else: continue
            except (KeyboardInterrupt, EOFError): sys.exit("\nExiting.") # aka subtle exit
        except EOFError: break
            
        if not usit: continue

        usit = unicodedata.normalize("NFKC", usit).strip()

        override_mode = None
        if usit.endswith(" -e"):
            override_mode = "easysaxo"
            usit = usit[:-2].strip()
        elif usit.endswith(" -s"):
            override_mode = "system"
            usit = usit[:-2].strip()

        effective_mode = override_mode if override_mode is not None else getattr(ThreadData, "target_mode", "auto")

        parts = usit.split(maxsplit=1)
        cmd = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else None
        
        if cmd in translations: cmd = translations[cmd]

        in_easysaxo = cmd in COMMAND_REGISTRY
        sys_binary = shutil.which(cmd)

        if effective_mode == "system": # forced syscmd
            if sys_binary:
                try: subprocess.run(usit, shell=True)
                except Exception as err: print(f"{Fore.RED}System command error: {err}{Style.RESET_ALL}")
            else: print(f"{Fore.RED}System command '{cmd}' not found in PATH.{Style.RESET_ALL}")
            
        elif effective_mode == "easysaxo": # forced escmd
            if in_easysaxo: COMMAND_REGISTRY[cmd](arg)
            else: print(f"{Fore.RED}EasySaxo command '{cmd}' not found.{Style.RESET_ALL}")
            
        else: # if our target match is auto
            if in_easysaxo: COMMAND_REGISTRY[cmd](arg)
            elif sys_binary:
                try: subprocess.run(usit, shell=True)
                except Exception as err: print(f"{Fore.RED}System command error: {err}{Style.RESET_ALL}")
                
            # easter egg support (built-in to hide from the user view)    
            elif cmd not in COMMAND_REGISTRY and enable_ee:
                if cmd == "getmeaneasteregg": commands.e1()
                elif cmd in ["noeasteregg", "falseget", "lookatthis", "lookatts"]: commands.e2()
                elif cmd == "osaka": commands.e3()
                elif cmd in ["mans not hot", "mansnothot", "no ketchup", "the sauce flexing", "thesauceflexing"]:
                    if commands.ee4: commands.e4()
                    else: print(f"{Fore.RED}Unknown command. Type 'help' for assistance.{Style.RESET_ALL}") 
                elif cmd in ["traceback", "error", "locateerror", "errorloc"]: commands.e5()
                else: print(f"{Fore.RED}Unknown command. Type 'help' for assistance.{Style.RESET_ALL}")
                
            #allow easter eggs (also hidden)
            elif cmd in ["secretenable", "enable_ee", "eastereggenable"] and scee:
                enable_ee = True
                scee = False
                print(f"{Fore.LIGHTBLACK_EX}Something happened.{Style.RESET_ALL} You have to find it out.")
            else: print(f"{Fore.RED}Unknown command. Type 'help' for assistance.{Style.RESET_ALL}")

import bcrypt

def run():
    preboot_file = None
    #session loader
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "load" and len(sys.argv) > 2: preboot_file = sys.argv[2]
        elif sys.argv[1].endswith(".json"): preboot_file = sys.argv[1]

    session_data = SessionManager.load_session(preboot_file)
    if isinstance(session_data, dict):
        ThreadData.current_user = session_data.get("user_name", "User")
        ThreadData.current_pswd = session_data.get("password")
    else: ThreadData.current_user = session_data
    
    if ThreadData.current_pswd is not None: # password checker
        while True:
            keyacc = input(f"{Fore.LIGHTRED_EX}Insert password: {Style.RESET_ALL}{Fore.LIGHTBLACK_EX}")
            
            try:
                is_valid = bcrypt.checkpw(keyacc.encode('utf-8'), ThreadData.current_pswd.encode('utf-8'))
            except Exception:
                is_valid = False
                
            if is_valid:
                print(f"{Fore.LIGHTGREEN_EX}Opening app...{Style.RESET_ALL}")
                time.sleep(0.5)
                clr()
                break
                
            print(f"{Fore.RED}Wrong password, try again.{Style.RESET_ALL}\n")
    
    Core(session_info=session_data) # nothing special yet 
    
if __name__ == "__main__":
    run()