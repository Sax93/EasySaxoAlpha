"""Miscellaneous function holder for EasySaxo."""

import time

from colorama import Fore, Style

from ..config import easysaxo

# `misc.py` may handle miscellaneous data and functions.

# Talking
def talk(text: str, sleeptime: float = 0.73):
    print(text)
    time.sleep(sleeptime)

# Time and Date
def hrs():
    print(f"Time: {Fore.LIGHTYELLOW_EX}{time.strftime('%H:%M:%S')}{Style.RESET_ALL}")
    print(f"Date: {Fore.LIGHTRED_EX}{time.strftime('%Y-%m-%d')}{Style.RESET_ALL}")

# Uninstaller
def uninstaller():
    import os
    import shutil
    import subprocess
    import sys
    base_dir = os.path.dirname(os.path.abspath(__file__))
    note_path = os.path.join(base_dir, "goodbye.txt")

    with open(note_path, "w", encoding="utf-8") as f: # farewell :(
        f.write("Thanks for using EasySaxo! I'll miss you. :(\n")

    try:
        if os.name == 'nt': os.startfile(note_path)
        elif sys.platform == 'darwin': subprocess.Popen(["open", note_path])
        else: subprocess.Popen(["xdg-open", note_path])
    except (PermissionError, FileNotFoundError, subprocess.CalledProcessError, KeyboardInterrupt): pass

    for folder in ["esmodules", "__pycache__", ".vscode"]: # delete app folders
        folder_path = os.path.join(base_dir, folder)
        if os.path.exists(folder_path): shutil.rmtree(folder_path, ignore_errors=True)

    from .lister import FileList
    for file in FileList._delete: # delete app files
        file_path = os.path.join(base_dir, file)
        if os.path.exists(file_path):
            try: os.remove(file_path)
            except PermissionError:
                """Just ignore the file."""

    print("Uninstalled successfully.")
    sys.exit(0) # Force exit

def unins_guide():
    try:
        print(f"{Fore.LIGHTRED_EX}WARNING! This will delete all {easysaxo.name} files and info.{Style.RESET_ALL}")
        con = input(f"{Fore.LIGHTCYAN_EX}Do you still want to proceed? (Y/N): {Style.RESET_ALL}").strip().lower() # please do not

        if con in ["y", "yes"]:
            print(f"Uninstalling {easysaxo.name} {easysaxo.ver}...")
            time.sleep(0.5)
            uninstaller()
        else: print("Uninstall canceled.")
    except KeyboardInterrupt: return

# Fake traceback cuz y not

def traceback(err):
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