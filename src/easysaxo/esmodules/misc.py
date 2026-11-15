"""Miscellaneous function holder for EasySaxo."""

import sys
import time

from rich import print

from ..config import easysaxo


# Time and Date
def hrs():
    print(f"Time: [light_yellow]{time.strftime('%H:%M:%S')}[/light_yellow]")
    print(f"Date: [light_red]{time.strftime('%Y-%m-%d')}[/light_red]")

class AppOper:
    @staticmethod
    def restart_app():
        import subprocess
        
        from ..config import clr
        try:
            clr()
            from .dirloct import DirLocation as Dl
            subprocess.run(Dl._resolve_path("..\\..\\run.bat"), check=False)
            sys.exit(0)
        except (FileNotFoundError, subprocess.CalledProcessError): sys.exit(0)
        except KeyboardInterrupt:
            easysaxo.k_log("11")
            return

    @staticmethod
    def uninstaller():
        import os
        import shutil
        import subprocess
        import sys

        from .dirloct import DirLocation, base_dir

        note_path = os.path.join(base_dir, "goodbye.txt")

        easysaxo.k_log("a0")
        with open(note_path, "w", encoding="utf-8") as f: f.write("Thanks for using EasySaxo! I'll miss you. :(\nalso try osaka collector 2 bro its free")

        try:
            if os.name == 'nt': os.startfile(note_path)
            elif sys.platform == 'darwin': subprocess.Popen(["open", note_path])
            else: subprocess.Popen(["xdg-open", note_path])
        except (PermissionError, FileNotFoundError, subprocess.CalledProcessError, KeyboardInterrupt): pass
        # delete app folders
        folder_path = os.path.join(base_dir, DirLocation._resolve_path("..\\.."))
        if os.path.exists(folder_path): shutil.rmtree(folder_path, ignore_errors=True)

        from .lister import FileList
        for file in FileList._delete: # delete app files
            file_path = os.path.join(base_dir, file)
            if os.path.exists(file_path):
                try: os.remove(file_path)
                except PermissionError: """Just ignore the file."""

        print("Uninstalled successfully.")
        sys.exit(0)

    @staticmethod
    def unins_guide():
        try:
            print(f"[light_red]WARNING! This will delete all {easysaxo.name} files and info.[/light_red]")
            con = input("[light_cyan]Do you still want to proceed? (Y/N): [/light_cyan]").strip().lower() # please do not

            if con in ["y", "yes"]:
                print(f"Uninstalling {easysaxo.name} {easysaxo.ver}...")
                time.sleep(0.5)
                AppOper.uninstaller()
                return
            print("Uninstall canceled.")
        except KeyboardInterrupt: return

    # Inside AppOper class in misc.py
    @staticmethod
    def handle_update():
        import os
        import re
        import shutil
        import tempfile
        import zipfile

        import requests

        from ..config import easysaxo
        from .dirloct import PROJECT_ROOT

        print(f"Current version: [cyan]{easysaxo.ver}[/cyan]")
        print("Checking for updates on GitHub...")

        try:
            # fetch remote config.py to read the latest version string
            raw_url = "https://raw.githubusercontent.com/Sax93/EasySaxoAlpha/main/src/easysaxo/config.py"
            resp = requests.get(raw_url, timeout=10)
            if not resp.ok:
                print(f"[red]Failed to check remote version (Status: {resp.status_code}).[/red]")
                return

            match = re.search(r'easysaxo\s*=\s*App\([^,]+,\s*"([^"]+)"\)', resp.text)
            if not match:
                print("[red]Could not parse remote version.[/red]")
                return

            remote_ver = match.group(1)
            local_ver = easysaxo.ver

            print(f"\nRemote version: [cyan]{remote_ver}[/cyan]")

            def parse_ver(v_str):
                nums = re.findall(r'\d+', v_str)
                return [int(n) for n in nums]

            local_nums = parse_ver(local_ver)
            remote_nums = parse_ver(remote_ver)

            # compare versions according to specs
            if local_nums == remote_nums:
                easysaxo.disclaim("[yellow]You have the latest version[/yellow]")
                return
            elif local_nums > remote_nums:
                easysaxo.disclaim("[yellow]You have a greater version[/yellow]")
                return
            else:
                # remote version is higher
                choice = input("[yellow]Update? [y/N]: [/yellow]").strip().lower()
                if choice != 'y':
                    print("Update canceled.")
                    return

                print("[cyan]Downloading latest release from GitHub...[/cyan]")
                zip_url = "https://github.com/Sax93/EasySaxoAlpha/archive/refs/heads/main.zip"
                temp_dir = tempfile.gettempdir()
                zip_path = os.path.join(temp_dir, "EasySaxoAlpha-main.zip")

                r = requests.get(zip_url, stream=True, timeout=15)
                with open(zip_path, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk: f.write(chunk)

                extract_dir = os.path.join(temp_dir, "EasySaxoAlpha_extracted")
                os.makedirs(extract_dir, exist_ok=True)

                with zipfile.ZipFile(zip_path, "r") as zf: zf.extractall(extract_dir)

                # replace files in installation root
                src_repo_root = os.path.join(extract_dir, "EasySaxoAlpha-main")
                inst_root = os.path.abspath(os.path.join(PROJECT_ROOT, "..", ".."))

                print("Replacing files...")
                for item in os.listdir(src_repo_root):
                    s_item = os.path.join(src_repo_root, item)
                    d_item = os.path.join(inst_root, item)
                    if os.path.isdir(s_item):
                        if os.path.exists(d_item): shutil.rmtree(d_item)
                        shutil.copytree(s_item, d_item)
                    else: shutil.copy2(s_item, d_item)

                print("[green]Update successful![/green]")
                time.sleep(1)
                AppOper.restart_app()

        except Exception as e: print(f"[red]Update failed: {e}[/red]")  # ruff: ignore[blind-except]