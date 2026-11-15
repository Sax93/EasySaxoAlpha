"""Directory / File manager for EasySaxo."""

import os
import platform
import subprocess
import sys
import tempfile
import zipfile

from rich import print

from ..config import easysaxo
from .lister import FileDisclaimer as Fd

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

base_dir = PROJECT_ROOT
dir_forcreate = os.path.join(PROJECT_ROOT, "esmodules", "filecreation")

class DirLocation:
    """Path identifier global operator and handler"""
    FLAGS = {  # noqa: RUF012
        "-<inst": lambda: os.path.join(PROJECT_ROOT, "..", ".."),
        "-<root": lambda: PROJECT_ROOT,
        "-<es": lambda: os.path.join(PROJECT_ROOT, "esmodules"),
        "-<fc": lambda: dir_forcreate,
        "-<temp": tempfile.gettempdir,
        "-<home": lambda: os.path.expanduser("~"),
        "-<desk": lambda: os.path.join(os.path.expanduser("~"), "Desktop"),
        "-<dwn": lambda: os.path.join(os.path.expanduser("~"), "Downloads"),
        "-<docs": lambda: os.path.join(os.path.expanduser("~"), "Documents"),
        "-<imgs": lambda: os.path.join(os.path.expanduser("~"), "Pictures"),
        "-<aud": lambda: os.path.join(os.path.expanduser("~"), "Music"),
        "-<vid": lambda: os.path.join(os.path.expanduser("~"), "Videos"),
        "-<bin": lambda: os.path.dirname(sys.executable),
    }

    @staticmethod
    def _get_file_bom(filepath: str) -> str:
        """Returns the byte order mark (BOM) of a file if present, else returns 'None'."""
        if not filepath: return "None"
        if os.path.isdir(filepath): return "Directory"

        try:
            with open(filepath, "rb") as f:
                raw = f.read(4)
                if raw.startswith((b'\xff\xfe\x00\x00', b'\x00\x00\xfe\xff')): return "UTF-32"
                elif raw.startswith((b'\xff\xfe', b'\xfe\xff')): return "UTF-16"
                elif raw.startswith(b'\xef\xbb\xbf'): return "UTF-8"
                return "UTF-8"
        except Exception as e:  # noqa: BLE001
            easysaxo.k_log("10")
            print(f"[red]Error reading file for BOM: {e}[/red]")
            return "Error"

    @staticmethod
    def _parse_flag_or_path(filepath: str) -> str:
        """Evaluates flag keys (-<flag) or relative subpaths starting with flags."""
        if not filepath: return base_dir

        clean_path = filepath.strip()
        normalized_path = clean_path.replace("/", os.sep).replace("\\", os.sep)
        parts = normalized_path.split(os.sep)

        first_part = parts[0].lower()

        # resolve flag at the head of the path string
        if first_part in DirLocation.FLAGS:
            flag_base = DirLocation.FLAGS[first_part]()
            if len(parts) > 1: return os.path.join(flag_base, *parts[1:])
            return flag_base
        elif first_part.startswith("<-"): 
            print(Fd.res_flag_typo)
            return clean_path
        elif first_part.startswith("-<") and first_part not in DirLocation.FLAGS:
            print(Fd.res_flag_typo_2)
            return clean_path
        
        if "_" in filepath:
            filepath = filepath.replace("_", " ")
            return filepath

        return clean_path

    @staticmethod
    def _resolve_path(filepath: str, *, for_creation: bool = False) -> str:
        """Parses the entered filepath and resolves it to an absolute path based on a fixed order."""
        path = DirLocation._parse_flag_or_path(filepath)

        if not path: return base_dir

        path = os.path.normpath(path)

        # explicit and absolute paths should be parsed first
        if os.path.isabs(path): return os.path.abspath(path)

        candidates = (
            os.path.join(base_dir, path),
            os.path.join(PROJECT_ROOT, path),
            os.path.join(PROJECT_ROOT, "esmodules", path),
        )

        # existing paths are resolved consistently
        for candidate in candidates:
            if os.path.exists(candidate): return os.path.abspath(candidate)

        # missing paths now need an explicit creation sign
        if for_creation: return os.path.abspath(os.path.join(dir_forcreate, path))

        # default fallback
        return os.path.abspath(os.path.join(base_dir, path))

    @staticmethod
    def _encode_analyzer_io(filepath: str) -> bool:
        _f_bom = DirLocation._get_file_bom(filepath)
        if _f_bom in ["None", "Error"]:
            easysaxo.k_log("f1")
            print(Fd.utf_evaluator)
            print(f"[yellow]File [cyan]{filepath}[yellow] could not be read.[/yellow]")
            return False
        elif _f_bom == "Directory":
            easysaxo.k_log("f3")
            print(Fd.utf_evaluator)
            print(f"[yellow]Path [cyan]{filepath}[yellow] is a directory, not a file.[/yellow]")
            return False
        elif _f_bom not in ["UTF-8", "UTF-16"]:
            easysaxo.k_log("f1")
            print(Fd.utf_evaluator)
            print(f"[yellow]File [cyan]{filepath}[yellow] is not UTF-8 or UTF-16 encoded (detected BOM: [red]{_f_bom}[/red])")
            return False

        print(f"Encoding: [yellow]{_f_bom}[/yellow]")
        return True

    @staticmethod
    def cd(path=None):
        global base_dir
        if not path:
            print(f"Current directory: [magenta]{DirLocation.get_display_path()}[/magenta]")
            return

        clean_path = path.strip()

        if clean_path.lower().startswith("/d "):
            clean_path = clean_path[3:].strip()
            print(Fd.cd_d_flag)

        target = DirLocation._resolve_path(clean_path)

        if os.path.exists(target) and os.path.isdir(target):
            os.chdir(target)
            base_dir = os.getcwd()
            print(f"Directory changed to [magenta]{DirLocation.get_display_path()}[/magenta]")
        else:
            easysaxo.k_log("5")
            print(f"[red]Directory '{clean_path}' does not exist.[/red]")

    @staticmethod
    def get_display_path(path=None):
        """Returns ~easysaxo relative path if within PROJECT_ROOT, else returns normalized path."""
        target_path = os.path.abspath(path) if path else base_dir

        if target_path == PROJECT_ROOT: return "~easysaxo"
        elif target_path.startswith(PROJECT_ROOT + os.sep):
            rel_path = os.path.relpath(target_path, PROJECT_ROOT)
            return f"~easysaxo\\{rel_path}"
        return target_path

    @staticmethod
    def allowance():
        try:
            from .lister import FileList

            _files_to_check = [f if f.endswith(".py") else f"{f}.py" for f in FileList._allow]

            files_to_check = [DirLocation._resolve_path(f"-<root\\{f}") for f in _files_to_check]

            for file in files_to_check:
                target_path = os.path.join(PROJECT_ROOT, file)

                if not os.path.exists(target_path):
                    print(f"[red]Missing: [yellow]{file}[/yellow][/red]")
                    continue

                is_init = file.endswith("__init__.py")
                is_valid_size = is_init or os.path.exists(target_path) and os.path.getsize(target_path) > 3

                if not is_valid_size:
                    print(f"[cyan]Below size: [yellow]{file}[/yellow][/cyan]")
                    return

                print(f"[green]Checked: [yellow]{file}[/yellow][/green]")
        except (ImportError, KeyboardInterrupt) as e: easysaxo.k_log("11" if isinstance(e, KeyboardInterrupt) else "10")

    @staticmethod
    def filesz(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath)
            if not os.path.exists(full_path):
                easysaxo.k_log("5")
                print(f"File [red]{filepath}[/red] does not exist.")
                return
            if os.path.isdir(full_path):
                easysaxo.k_log("f3")
                print(f"[red]{filepath}[/red] is a directory, not a file.")
                return

            size_bytes = os.path.getsize(full_path)

            for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                if size_bytes < 1024.0:
                    readable_size = f"{size_bytes:.2f} {unit}"
                    break
                size_bytes /= 1024.0

            display_file = DirLocation.get_display_path(full_path)
            print(f"Size of [cyan]{display_file}[/cyan]: [yellow]{readable_size}[/yellow]")
        except (FileNotFoundError, PermissionError, KeyboardInterrupt) as e:
            easysaxo.k_log("4" if isinstance(e, PermissionError) else "5" if isinstance(e, FileNotFoundError) else "11")
            print(f"[red]Error getting file size: {e}[/red]")

    @staticmethod
    def dirsz(filepath=None):
        import psutil
        try:
            full_path = os.path.abspath(DirLocation._resolve_path(filepath)) if filepath else base_dir
            if not os.path.exists(full_path):
                easysaxo.k_log("5")
                print(f"Directory [red]{filepath}[/red] does not exist.")
                return
            if not os.path.isdir(full_path):
                easysaxo.k_log("f2")
                print(f"[red]{filepath}[/red] is a file, not a directory.")
                return

            if os.path.dirname(full_path) == full_path:
                usage = psutil.disk_usage(full_path)
                size_bytes = usage.used
            else:
                def _get_dir_size(path):
                    total = 0
                    try:
                        with os.scandir(path) as it:
                            for entry in it:
                                try:
                                    if entry.is_file(follow_symlinks=False): total += entry.stat(follow_symlinks=False).st_size
                                    elif entry.is_dir(follow_symlinks=False): total += _get_dir_size(entry.path)
                                except (PermissionError, FileNotFoundError, OSError): continue
                    except (PermissionError, FileNotFoundError, OSError): pass
                    return total

                size_bytes = _get_dir_size(full_path)

            for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                if size_bytes < 1024.0:
                    readable_size = f"{size_bytes:.2f} {unit}"
                    break
                size_bytes /= 1024.0

            display_dir = DirLocation.get_display_path(full_path)
            if filepath and filepath != ".": target_display = f"{filepath} ({display_dir})"
            else: target_display = display_dir

            print(f"Size of directory [cyan]{target_display}[/cyan]: [yellow]{readable_size}[/yellow]")
        except (FileNotFoundError, PermissionError, KeyboardInterrupt) as e: 
            easysaxo.k_log("5" if isinstance(e, FileNotFoundError) else "4" if isinstance(e, PermissionError) else "11")
            print(f"[red]Error getting directory size: {e}[/red]")

    @staticmethod
    def ls(filepath=None):
        try:
            target_dir = DirLocation._resolve_path(filepath) if filepath else base_dir
            if not os.path.exists(target_dir):
                easysaxo.k_log("5")
                print(f"Directory [red]{filepath}[/red] does not exist.")
                return
            if not os.path.isdir(target_dir):
                easysaxo.k_log("f2")
                print(f"[red]{filepath}[/red] is not a directory.")
                return

            display_dir = DirLocation.get_display_path(target_dir)
            print(f"\n--- Directory Contents of [cyan]{display_dir}[/cyan] ---")

            with os.scandir(target_dir) as entries:
                for entry in sorted(entries, key=lambda e: e.name.lower()):
                    if entry.is_dir(follow_symlinks=False): print(f"[blue][DIR]  {entry.name}[/blue]")
                    else:
                        size_bytes = entry.stat(follow_symlinks=False).st_size

                        for unit in ['B', 'KB', 'MB', 'GB']:
                            if size_bytes < 1024.0:
                                size_str = f"{size_bytes:.2f} {unit}"
                                break
                            size_bytes /= 1024.0

                        print(f"[green][FILE] {entry.name}[/green] ([yellow]{size_str}[/yellow])")

            print("--- End of Directory Listing ---\n")
        except (PermissionError, FileNotFoundError) as e: 
            easysaxo.k_log("4" if isinstance(e, PermissionError) else "5")
            print(f"[red]Error listing directory: {e}[/red]")

    @staticmethod
    def filetree(filepath=None, max_depth=4):
        try:
            target_dir = DirLocation._resolve_path(filepath) if filepath else base_dir
            if not os.path.exists(target_dir):
                easysaxo.k_log("5")
                print(f"Directory [red]{filepath}[/red] does not exist.")
                return
            if not os.path.isdir(target_dir):
                easysaxo.k_log("f2")
                print(f"[red]{filepath}[/red] is not a directory.")
                return

            display_dir = DirLocation.get_display_path(target_dir)
            print(f"\n[cyan] Directory Tree: {display_dir}[/cyan]\n")

            def _build_tree(dir_path, prefix="", current_depth=0):
                if current_depth > max_depth:
                    print(f"{prefix}[lightblack]... (max depth reached)[/lightblack]")
                    return

                try: entries = sorted(os.listdir(dir_path))
                except PermissionError:
                    print(f"{prefix}[red][Permission Denied][/red]")
                    return
                except OSError:
                    print(f"{prefix}[red][OS Exception][/red]")
                    return

                dirs = [e for e in entries if os.path.isdir(os.path.join(dir_path, e))]
                files = [e for e in entries if not os.path.isdir(os.path.join(dir_path, e))]

                all_items = dirs + files
                total_items = len(all_items)

                for index, item in enumerate(all_items):
                    is_last = (index == total_items - 1)
                    connector = "└── " if is_last else "├── "
                    child_prefix = "    " if is_last else "│   "

                    item_path = os.path.join(dir_path, item)

                    if os.path.isdir(item_path):
                        print(f"{prefix}{connector}[blue][BRIGHT]{item}/[/BRIGHT][/blue]")
                        _build_tree(item_path, prefix + child_prefix, current_depth + 1)
                    else:
                        from .lister import FileList
                        _, ext = os.path.splitext(item)
                        ext_color = FileList.EXTENSION_COLORS.get(ext.lower(), "[white]")

                        print(f"{prefix}{connector}{ext_color}{item}[/white]")

            _build_tree(target_dir)
            print("\n[cyan]--- End of Directory Tree ---[/cyan]\n")

        except (PermissionError, FileNotFoundError, KeyboardInterrupt) as e: 
            easysaxo.k_log("5" if isinstance(e, FileNotFoundError) else "4" if isinstance(e, PermissionError) else "11")
            print(f"[red]Error rendering directory tree: {e}[/red]")

    @staticmethod
    def fileopn(filepath):
        import sys
        try:
            full_path = DirLocation._resolve_path(filepath)
            if not os.path.exists(full_path):
                easysaxo.k_log("5")
                print(f"File [red]{filepath}[/red] does not exist.")
                return None

            display_file = DirLocation.get_display_path(full_path)

            if filepath.endswith(".py"):
                print(f"Executing [green]{display_file}[/green]...")

                result = subprocess.run(
                    [sys.executable, full_path],
                    capture_output=True,
                    text=True,
                    check=True
                )

                if result.returncode != 0:
                    traceback_str = result.stderr
                    print(f"[magenta]Program returns an exception:[/magenta]\n{traceback_str}")
                    return traceback_str
                else:
                    if result.stdout: print(result.stdout, end="")
                    print(f"[green]Program finished with exit code [/green][cyan]{result.returncode}[/cyan]")
                    return None
            else:
                print(f"Opening [green]{display_file}[/green]...")
                if os.name == "nt": os.startfile(full_path)
                elif platform.system() == "Darwin": subprocess.run(["open", full_path], check=True)
                else: subprocess.run(["xdg-open", full_path], check=True)
                return None

        except subprocess.CalledProcessError as e:
            print(f"\nProgram '[red]{full_path}[/red]' returned exit code [cyan]{e.returncode!s}[/cyan]:\n"
                  f"[magenta]{e}[/magenta]")
        except (PermissionError, FileNotFoundError) as e:
            easysaxo.k_log("4" if isinstance(e, PermissionError) else "5")
            print(f"[red]Error opening file: {e}[/red]")
            return str(e)

    @staticmethod
    def filecls(process_name_or_file):
        import psutil
        try:
            target = os.path.basename(process_name_or_file).lower()
            terminated = False
            for proc in psutil.process_iter(["pid", "name"]):
                try:
                    if target in proc.info["name"].lower():
                        proc.terminate()
                        print(f"Closed process [green]{proc.info['name']}[/green] (PID: {proc.info['pid']}).")
                        terminated = True
                except (psutil.NoSuchProcess, psutil.AccessDenied): continue
            if not terminated:
                easysaxo.k_log("p1")
                print(f"No running process found matching [yellow]{process_name_or_file}[/yellow].")
        except (PermissionError, psutil.NoSuchProcess, psutil.AccessDenied) as e:
            easysaxo.k_log("4" if isinstance(e, PermissionError or psutil.AccessDenied) else "10")
            print(f"[red]Error closing file process: {e}[/red]")

    @staticmethod
    def filecrt(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath, for_creation=True)
            display_file = DirLocation.get_display_path(full_path)

            if os.path.exists(full_path): 
                easysaxo.k_log("f4")
                print(f"File [yellow]{display_file}[/yellow] already exists.")
            else:
                parent_dir = os.path.dirname(full_path)
                if parent_dir: os.makedirs(parent_dir, exist_ok=True)

                open(full_path, "a").close()
                print(f"File [green]{display_file}[/green] created successfully.")
        except (PermissionError, FileNotFoundError) as e:
            easysaxo.k_log("4")
            print(f"[red]Error creating file: {e}[/red]")

    @staticmethod
    def dircrt(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath, for_creation=True)
            display_dir = DirLocation.get_display_path(full_path)
            if os.path.exists(full_path):
                easysaxo.k_log("f4")
                print(f"Directory or path [yellow]{display_dir}[/yellow] already exists.")
            else:
                os.makedirs(full_path, exist_ok=True)
                print(f"Directory [green]{display_dir}[/green] created successfully.")
        except PermissionError as e: 
            easysaxo.k_log("4")
            print(f"[red]Error creating directory: {e}[/red]")

    @staticmethod
    def dirdel(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath)
            display_dir = DirLocation.get_display_path(full_path)
            if os.path.exists(full_path) and os.path.isdir(full_path):
                os.rmdir(full_path)
                print(f"Directory [green]{display_dir}[/green] deleted successfully.")
            else:
                easysaxo.k_log("5" if not os.path.exists(full_path) else "f2")
                print(f"Directory [red]{display_dir}[/red] does not exist or is not a folder.")
        except (OSError):
            import shutil
            full_path = DirLocation._resolve_path(filepath)
            display_dir = DirLocation.get_display_path(full_path)
            if os.path.exists(full_path) and os.path.isdir(full_path):
                shutil.rmtree(full_path)
                print(f"Directory [green]{display_dir}[/green] deleted successfully.")
        except (KeyboardInterrupt, PermissionError) as e:
            easysaxo.k_log("4" if isinstance(e, PermissionError) else "11")
            print(f"[red]Error deleting directory: {e}[/red]")

    @staticmethod
    def filerd(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath)
            display_file = DirLocation.get_display_path(full_path)

            _f_bom = DirLocation._encode_analyzer_io(full_path)
            if _f_bom is False: return
            
            if os.path.exists(full_path):
                with open(full_path, "r", encoding="utf-8") as f:  content = f.read()

                display_content = content

                if filepath.endswith(".py"):
                    try:
                        from pygments import highlight
                        from pygments.formatters import TerminalFormatter
                        from pygments.lexers import PythonLexer

                        display_content = highlight(content, PythonLexer(), TerminalFormatter())
                    except ImportError:  display_content = f"[green]{content}[/green]"

                print(f"\n--- Contents of [cyan]{display_file}[/cyan] ---\n{display_content}\n--- End of file ---")
            else:
                easysaxo.k_log("5")
                print(f"File [red]{filepath}[/red] does not exist.")
        except PermissionError as e:
            easysaxo.k_log("4")
            print(f"[red]Error reading file: {e}[/red]")
        except UnicodeDecodeError:
            easysaxo.k_log("f1")
            print("[red]Make sure your file is valid for reading.[/red]")
        except KeyboardInterrupt:
            easysaxo.k_log("11")
            print("\n[red]Read operation cancelled by user.[/red]")

    @staticmethod
    def filedel(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath)
            display_file = DirLocation.get_display_path(full_path)
            if os.path.exists(full_path):
                os.remove(full_path)
                print(f"File [green]{display_file}[/green] deleted successfully.")
                return
            easysaxo.k_log("5")
            print(f"File [red]{display_file}[/red] does not exist.")
        except (PermissionError, OSError) as e:  
            easysaxo.k_log("4")
            print(f"[red]Error deleting file: {e}[/red]")

    @staticmethod
    def filewrt(filepath, content=None):
        import ast

        from .lister import CommandList

        class QuickLinter(ast.NodeVisitor):
            def __init__(self): self.warnings = []

            def visit_FunctionDef(self, node):
                if any(c.isupper() for c in node.name):
                    self.warnings.append(f"Line {node.lineno}: Function '{node.name}' should use snake_case.")

                args = [a.arg for a in node.args.args if a.arg != "self"]
                used_vars = {child.id for child in ast.walk(node) if isinstance(child, ast.Name)}
                for arg in args:
                    if arg not in used_vars and not arg.startswith("_"):
                        self.warnings.append(f"Line {node.lineno}: Unused argument '{arg}' in function '{node.name}'.")

                self.generic_visit(node)

            def visit_ClassDef(self, node):
                if not node.name[0].isupper() or "_" in node.name:
                    self.warnings.append(f"Line {node.lineno}: Class '{node.name}' should use PascalCase/CamelCase.")
                self.generic_visit(node)

            def visit_Import(self, node):
                for alias in node.names:
                    if alias.name == "sys" or alias.name == "os": 
                        """Pass."""
                self.generic_visit(node)

            def visit_Call(self, node):
                if isinstance(node.func, ast.Name) and node.func.id in ("eval", "exec"):
                    self.warnings.append(f"Line {node.lineno}: Use of unsafe function '{node.func.id}()'.")
                self.generic_visit(node)

        def _run_linter(code_str):
            try:
                tree = ast.parse(code_str)
                linter = QuickLinter()
                linter.visit(tree)
                return linter.warnings, None
            except SyntaxError as se: return [], f"SyntaxError on line {se.lineno}, col {se.offset}: {se.msg}"
            except NameError as ne: return [], f"NameError on line {ne.lineno}, col {ne.offset}: {ne.msg}"

        try:
            full_path = DirLocation._resolve_path(filepath)
            display_file = DirLocation.get_display_path(full_path)

            _f_bom = DirLocation._encode_analyzer_io(full_path)
            if _f_bom is False: return

            if os.path.isdir(full_path):
                easysaxo.k_log("f3")
                print(f"File [yellow]{display_file}[/yellow] is a directory, not a file.")
                return

            if content is None:
                print(f"[cyan]--- Interactive Line Editor for '{display_file}' ---[/cyan]")
                print(CommandList.FWRTlist)

                lines = []
                if os.path.exists(full_path):
                    try:
                        with open(full_path, "r", encoding="utf-8") as f: lines = f.read().splitlines()
                        if lines: print(f"[lightblack]Loaded existing file content ({len(lines)} lines).[/lightblack]")
                    except PermissionError: """just dont give two shiis"""

                while True:
                    try:
                        line = input()
                        cmd = line.strip()

                        if cmd in [":w", ":x", ":save", "EOF", ":EOF", "END", "exit"]:
                            if filepath.endswith(".py"):
                                warnings, syntax_err = _run_linter("\n".join(lines))
                                if syntax_err:
                                    print(f"[red][Linter] {syntax_err}[/red]")
                                    confirm = input("[yellow]Save with syntax error? (y/N): [/yellow]").strip().lower()
                                    if confirm != 'y':  continue
                                elif warnings:
                                    print("[yellow][Linter Warnings]:[/yellow]")
                                    for w in warnings:   print(f" - [yellow]{w}[/yellow]")
                            break

                        elif cmd == ":q":
                            print("[yellow]Changes discarded.[/yellow]")
                            return

                        elif cmd in [":lint", ":check", ":lt"]:
                            if not filepath.endswith(".py"):
                                print("[yellow]File is not a Python script.[/yellow]")
                                return
                            warnings, syntax_err = _run_linter("\n".join(lines))
                            if syntax_err: print(f"[red][Linter] {syntax_err}[/red]")
                            elif warnings:
                                print(f"[yellow][Linter Found {len(warnings)} Warning(s)]:[/yellow]")
                                for w in warnings: print(f" - [yellow]{w}[/yellow]")
                            else: print("[green][Linter] Check return no errors.[/green]")

                        elif cmd in [":l", ":list"]:
                            print("\n[cyan]--- Buffer Preview ---[/cyan]")
                            for idx, l in enumerate(lines, 1): print(f"[yellow]{idx:3d} |[/yellow] {l}")
                            print("[cyan]-----------------------[/cyan]\n")

                        elif cmd == ":c":
                            lines.clear()
                            print("[red]Buffer cleared.[/red]")

                        elif cmd.startswith(":d"):
                            parts = cmd.split(maxsplit=1)
                            if len(parts) == 2 and parts[1].isdigit():
                                idx = int(parts[1]) - 1
                                if 0 <= idx < len(lines):
                                    removed = lines.pop(idx)
                                    print(f"[red]Removed line {idx+1}: [/red]{removed}")
                                else: print("[red]Invalid line number.[/red]")
                            else: print("[red]Usage: :d <line_number>[/red]")

                        elif cmd.startswith(":i"):
                            parts = cmd.split(maxsplit=2)
                            if len(parts) >= 3 and parts[1].isdigit():
                                idx = int(parts[1]) - 1
                                new_text = parts[2]
                                if 0 <= idx <= len(lines):
                                    lines.insert(idx, new_text)
                                    print("[green]Inserted line {idx+1}.[/green]")
                                else: print("[red]Line number out of range.[/red]")
                            else: print("[red]Usage: :i <line_number> <text>[/red]")

                        elif cmd in [":h", ":help"]: print(CommandList.FWRTlist)

                        else: lines.append(line)

                    except KeyboardInterrupt:
                        print("\n[red]Write operation cancelled.[/red]")
                        return
                content = "\n".join(lines)

            with open(full_path, "w", encoding="utf-8") as f: f.write(content)
            print(f"Content written to [green]{display_file}[/green] successfully.")
        except (PermissionError, FileNotFoundError) as e: 
            easysaxo.k_log("4")
            print(f"[red]Error writing to file: {e}[/red]")
        except UnicodeDecodeError:
            easysaxo.k_log("f1")
            print("[red]Make sure your file is valid for writing.[/red]") 
        except KeyboardInterrupt:
            easysaxo.k_log("11")
            print("\n[red]Write operation cancelled by user.[/red]")

    @staticmethod
    def filesort(dirpath, file_ext, dirdest):
        try:
            import shutil
            source_dir = DirLocation._resolve_path(dirpath)
            dest_dir = DirLocation._resolve_path(dirdest)

            display_dest = DirLocation.get_display_path(dest_dir)

            if not os.path.exists(source_dir) or not os.path.isdir(source_dir):
                easysaxo.k_log("5" if not os.path.exists(source_dir) else "f2")
                print(f"[red]Source directory '{dirpath}' does not exist or is not a directory.[/red]")
                return

            os.makedirs(dest_dir, exist_ok=True)
            if not file_ext.startswith("."): file_ext = f".{file_ext}"
            file_ext = file_ext.lower()

            moved_count = 0
            for item in os.listdir(source_dir):
                src_file_path = os.path.join(source_dir, item)

                if os.path.isdir(src_file_path): continue

                if item.lower().endswith(file_ext):
                    dest_file_path = os.path.join(dest_dir, item)
                    shutil.move(src_file_path, dest_file_path)
                    moved_count += 1

            print(f"[green]Successfully moved {moved_count} file(s) with extension '{file_ext}' to '{display_dest}'.[/green]")
        except (PermissionError) as e:
            easysaxo.k_log("4")
            print(f"[red]Error moving files into destination '{dirdest}': {e}[/red]")

    @staticmethod
    def filemove(arg: str):
        try:
            import shutil
            if not arg:
                easysaxo.k_log("2")
                print("[red]Usage: move [file] [dir] OR move (file1, file2) [dir][/red]")
                return

            arg_str = arg.strip()
            files = []
            dest_raw = "."

            # group files in parentheses
            if arg_str.startswith("("):
                end_idx = arg_str.find(")")
                if end_idx == -1:
                    easysaxo.k_log("1")
                    print("[red]Malformed parentheses.[/red]")
                    return
                raw_files = arg_str[1:end_idx].split(",")
                files = [f.strip() for f in raw_files if f.strip()]
                dest_raw = arg_str[end_idx+1:].strip() or "."
            else:
                parts = arg_str.split()
                if len(parts) >= 2:
                    if parts[0].lower() in DirLocation.FLAGS and len(parts) == 2:
                        if parts[1].lower() in DirLocation.FLAGS:
                            files = [parts[0]]
                            dest_raw = parts[1]
                        else:
                            files = [parts[1]]
                            dest_raw = parts[0]
                    else:
                        files = [" ".join(parts[:-1])]
                        dest_raw = parts[-1]
                else:
                    files = [arg_str]
                    dest_raw = "."

            dest_path = DirLocation._resolve_path(dest_raw)
            os.makedirs(dest_path, exist_ok=True)
            if not os.path.isdir(dest_path):
                easysaxo.k_log("f2")
                print(f"[red]Destination '{dest_raw}' is not a valid directory.[/red]")
                return

            moved_count = 0
            for f_item in files:
                src_path = DirLocation._resolve_path(f_item)
                if not os.path.exists(src_path):
                    easysaxo.k_log("5")
                    print(f"[red]File or directory '{f_item}' does not exist.[/red]")
                    continue

                filename = os.path.basename(src_path)
                target_dest_path = os.path.join(dest_path, filename)

                shutil.move(src_path, target_dest_path)
                display_src = DirLocation.get_display_path(src_path)
                display_dest = DirLocation.get_display_path(target_dest_path)
                print(f"Moved [green]{display_src}[/green] -> [yellow]{display_dest}[/yellow]")
                moved_count += 1

            print(f"[green]Successfully moved {moved_count} item(s).[/green]")
        except (PermissionError, OSError, KeyboardInterrupt) as e:
            easysaxo.k_log("4" if isinstance(e, PermissionError) else "11")
            print(f"[red]Error executing move command: {e}[/red]")

    @staticmethod
    def unzip(zip_path: str, extract_to: str | None = None):
        try:
            full_zip = DirLocation._resolve_path(zip_path)

            if not os.path.exists(full_zip):
                easysaxo.k_log("5")
                print(f"[red]File '{zip_path}' does not exist.[/red]")
                return

            if not zipfile.is_zipfile(full_zip):
                easysaxo.k_log("f1")
                print(f"[red]'{zip_path}' is not a valid zip archive.[/red]")
                return

            # if no output folder specified, default to a directory named after the zip
            if not extract_to:
                base_name = os.path.splitext(os.path.basename(full_zip))[0]
                extract_to = os.path.join(os.path.dirname(full_zip), base_name)
            else: extract_to = DirLocation._resolve_path(extract_to)

            os.makedirs(extract_to, exist_ok=True)

            display_zip = DirLocation.get_display_path(full_zip)
            display_extract = DirLocation.get_display_path(extract_to)

            print(f"Extracting [cyan]{display_zip}[/cyan] -> [yellow]{display_extract}[/yellow]...")

            with zipfile.ZipFile(full_zip, "r") as zip_ref: zip_ref.extractall(extract_to)

            print("[green]Extraction complete![/green]")

        except (zipfile.BadZipFile, PermissionError, OSError, KeyboardInterrupt) as e: 
            easysaxo.k_log("3")
            print(f"[red]Failed to extract zip: {e}[/red]")