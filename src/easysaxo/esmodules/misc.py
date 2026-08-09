from ..config import easysaxo, clr
from colorama import Fore, Style

# `misc.py` may handle miscellaneous data and functions.

# What's new
def whats_new():
    print(
        f"\n===== {Fore.CYAN}What's New!{Style.RESET_ALL} ({Fore.YELLOW}{easysaxo.name} v{easysaxo.ver}{Style.RESET_ALL}) =====\n"
        f"2. Added commands: {Fore.BLUE}'banner', 'pkm'{Style.RESET_ALL}.\n"
        f"2. Fixed {Fore.LIGHTGREEN_EX}code & miscellaneous{Style.RESET_ALL} bugs.\n"
    )

# Talking
def talk(text: str, sleeptime: float = None):
    print(text)
    time.sleep(sleeptime) if sleeptime else time.sleep(0.73)

# Time and Date
import time

def hrs():
    print(f"Time: {Fore.LIGHTYELLOW_EX}{time.strftime('%H:%M:%S')}{Style.RESET_ALL}")
    print(f"Date: {Fore.LIGHTRED_EX}{time.strftime('%Y-%m-%d')}{Style.RESET_ALL}")

# Status Handler for modules
import importlib

class StatusHandler:
    def __init__(self, label_width=25):
        self.ok = f"{Fore.GREEN}OK{Style.RESET_ALL}"
        self.er = f"{Fore.RED}ERROR{Style.RESET_ALL}"
        self.label_width = label_width

    def print_status(self, label: str, success: bool, extra_info: str = ""):
        status = self.ok if success else self.er
        print(f"{label:<{self.label_width}}: [{status}] {extra_info}".strip())

    def check_imports(self, modules: list[str]):
        all_success = True
        for mod in modules:
            try:
                importlib.import_module(mod)
                self.print_status(f"Module {Fore.BLUE}{mod.upper()}{Style.RESET_ALL}", success=True)
            except ImportError as e:
                self.print_status(f"Module {Fore.BLUE}{mod.upper()}{Style.RESET_ALL}", success=False, extra_info=str(e))
                all_success = False
        return all_success

StHd = StatusHandler(label_width=20)

def module_importing(modlist):
    StHd.check_imports(modlist)
    print()
    
# In boot, this chunk down below takes priority over main.py
# to check if the app can run properly.
# Module importing might throw ERROR over GPutil and CPUinfo
# for actually no reason..

from .lister import required_modules as mods
from .dirloct import DirLocation
def bootcheck():
    clr()
    print(f"{Fore.LIGHTYELLOW_EX}This might take a few seconds...{Style.RESET_ALL}")
    module_importing(mods)
    DirLocation.allowance()
    clr()
    
bootcheck()


# Uninstaller
def uninstaller():
    import os, sys, subprocess
    base_dir = os.path.dirname(os.path.abspath(__file__))
    note_path = os.path.join(base_dir, "goodbye.txt")

    with open(note_path, "w", encoding="utf-8") as f: # farewell :(
        f.write("Thanks for using EasySaxo! I'll miss you. :(\n")

    try:
        if os.name == 'nt': os.startfile(note_path)
        elif sys.platform == 'darwin': subprocess.Popen(["open", note_path])
        else: subprocess.Popen(["xdg-open", note_path])
    except Exception as e: pass

    for folder in ["esmodules", "__pycache__", ".vscode"]: # delete app folders
        folder_path = os.path.join(base_dir, folder)
        if os.path.exists(folder_path): shutil.rmtree(folder_path, ignore_errors=True)
        
    from .lister import files_to_delete as fls
    for file in fls: # delete app files
        file_path = os.path.join(base_dir, file)
        if os.path.exists(file_path):
            try: os.remove(file_path)
            except Exception: pass # unless python crashes here

    print("Uninstalled successfully.")
    sys.exit(0) # Force exit

def unins_guide():
    print(f"{Fore.LIGHTRED_EX}WARNING! This will delete all EasySaxo files and info.{Style.RESET_ALL}")
    con = input(f"{Fore.LIGHTCYAN_EX}Do you still want to proceed? (Y/N): {Style.RESET_ALL}").strip().lower() # please do not
    
    if con in ["y", "yes"]:
        print(f"Uninstalling EasySaxo {easysaxo.ver}...")
        time.sleep(0.5)
        uninstaller()
    else: print("Uninstall canceled.")

# Fake traceback

def traceback(err):
    import time
    from .dirloct import base_dir
    print()
    print("Traceback (most recent call last):\n"
          f'  File {Fore.MAGENTA}"{base_dir}"{Style.RESET_ALL}, line {Fore.MAGENTA}199{Style.RESET_ALL}, in {Fore.MAGENTA}<module>{Style.RESET_ALL}\n'
          f'    {Fore.LIGHTRED_EX}run{Fore.RED}(){Style.RESET_ALL}\n'
          f'    {Fore.LIGHTRED_EX}~~~{Fore.RED}^^{Style.RESET_ALL}\n'
          f'  File {Fore.MAGENTA}"{base_dir}"{Style.RESET_ALL}, line {Fore.MAGENTA}98{Style.RESET_ALL}, in {Fore.MAGENTA}<module>{Style.RESET_ALL}\n'
          f'    {Fore.LIGHTRED_EX}tf u mean, im not {Fore.RED}the error!{Style.RESET_ALL}\n'
          f'    {Fore.LIGHTRED_EX}~~~~~~~~~~~~~~~~~~{Fore.RED}^^^^^^^^^^{Style.RESET_ALL}\n'
          f'{Fore.LIGHTMAGENTA_EX}{err}{Style.RESET_ALL}\n'
          )
    time.sleep(1)

# misc.py shall live argargagrgragragra