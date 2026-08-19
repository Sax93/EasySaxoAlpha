"""Directory / File manager for EasySaxo"""

# `dirloct.py` ONLY FOR FILE-RELATED COMMAND DEFINING

import os
import platform
import subprocess

from colorama import Fore, Style

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
dir_forcreate = os.path.join(base_dir, "esmodules", "filecreation")

class DirLocation:
    @staticmethod
    def cd(path=None):
        global base_dir
        if not path:
            print(f"Current directory: {Fore.MAGENTA}{base_dir}{Style.RESET_ALL}")
            return

        clean_path = path.strip()
        if clean_path.lower().startswith("/d "):
            clean_path = clean_path[3:].strip()
            print(f"{Fore.LIGHTBLACK_EX}'/d' in this command is automated, you do not need to type it!{Style.RESET_ALL}")

        target = DirLocation._resolve_path(clean_path)

        if os.path.exists(target) and os.path.isdir(target):
            os.chdir(target)
            base_dir = os.getcwd()
            print(f"Directory changed to {Fore.MAGENTA}{base_dir}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Directory '{clean_path}' does not exist.{Style.RESET_ALL}")

    @staticmethod
    def runloc():
        print(f"Running in {Fore.MAGENTA}{base_dir}{Style.RESET_ALL}.")

    @staticmethod
    def _resolve_path(filepath: str) -> str:
        if os.path.isabs(filepath): return filepath

        # check direct path relative to project root
        root_path = os.path.join(base_dir, filepath)
        if os.path.exists(root_path): return root_path

        # check inside esmodules
        es_path = os.path.join(base_dir, "esmodules", filepath)
        if os.path.exists(es_path): return es_path

        # fallback to filecreation
        os.makedirs(dir_forcreate, exist_ok=True)
        return os.path.join(dir_forcreate, filepath)

    @staticmethod
    def allowance():
        from .lister import FileList

        FileList._allow = [f"{file}.py" for file in FileList._allow]

        for file in FileList._allow:
            resolved_path = DirLocation._resolve_path(file)

            if not os.path.exists(resolved_path):
                print(f"Missing: {Fore.RED}{file}{Style.RESET_ALL}")
                continue

            is_init = file.endswith("__init__.py")
            is_valid_size = is_init or os.path.getsize(resolved_path) > 0

            if is_valid_size: print(f"Checked: {Fore.GREEN}{file}{Style.RESET_ALL}")
            else: print(f"Empty (expected non-empty): {Fore.YELLOW}{file}{Style.RESET_ALL}")

    @staticmethod
    def filesz(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath)
            if not os.path.exists(full_path):
                print(f"File {Fore.RED}{filepath}{Style.RESET_ALL} does not exist.")
                return
            if os.path.isdir(full_path):
                print(f"{Fore.RED}{filepath}{Style.RESET_ALL} is a directory, not a file.")
                return

            size_bytes = os.path.getsize(full_path)

            for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                if size_bytes < 1024.0:
                    readable_size = f"{size_bytes:.2f} {unit}"
                    break
                size_bytes /= 1024.0

            print(f"Size of {Fore.CYAN}{filepath}{Style.RESET_ALL}: {Fore.YELLOW}{readable_size}{Style.RESET_ALL}")
        except (FileNotFoundError, PermissionError) as e:
            print(f"{Fore.RED}Error getting file size: {e}{Style.RESET_ALL}")

    @staticmethod
    def ls(filepath=None):
        try:
            target_dir = DirLocation._resolve_path(filepath) if filepath else base_dir
            if not os.path.exists(target_dir):
                print(f"Directory {Fore.RED}{filepath}{Style.RESET_ALL} does not exist.")
                return
            if not os.path.isdir(target_dir):
                print(f"{Fore.RED}{filepath}{Style.RESET_ALL} is not a directory.")
                return

            items = os.listdir(target_dir)
            print(f"\n--- Directory Contents of {Fore.CYAN}{target_dir}{Style.RESET_ALL} ---")
            for item in sorted(items):
                item_path = os.path.join(target_dir, item)
                if os.path.isdir(item_path):
                    print(f"{Fore.BLUE}[DIR]  {item}{Style.RESET_ALL}")
                else:
                    # Get file size in bytes
                    size_bytes = os.path.getsize(item_path)

                    for unit in ['B', 'KB', 'MB', 'GB']:
                        if size_bytes < 1024.0:
                            size_str = f"{size_bytes:.2f} {unit}"
                            break
                        size_bytes /= 1024.0

                    print(f"{Fore.GREEN}[FILE] {item}{Style.RESET_ALL} ({Fore.YELLOW}{size_str}{Style.RESET_ALL})")
            print("--- End of Directory Listing ---\n")
        except (PermissionError, FileNotFoundError) as e:
            print(f"{Fore.RED}Error listing directory: {e}{Style.RESET_ALL}")

    @staticmethod
    def filetree(filepath=None, max_depth=4):
        try:
            target_dir = DirLocation._resolve_path(filepath) if filepath else base_dir
            if not os.path.exists(target_dir):
                print(f"Directory {Fore.RED}{filepath}{Style.RESET_ALL} does not exist.")
                return
            if not os.path.isdir(target_dir):
                print(f"{Fore.RED}{filepath}{Style.RESET_ALL} is not a directory.")
                return

            print(f"\n{Fore.CYAN} Directory Tree: {target_dir}{Style.RESET_ALL}\n")

            def _build_tree(dir_path, prefix="", current_depth=0):
                if current_depth > max_depth:
                    print(f"{prefix}{Fore.LIGHTBLACK_EX}... (max depth reached){Style.RESET_ALL}")
                    return

                try:
                    entries = sorted(os.listdir(dir_path))
                except PermissionError:
                    print(f"{prefix}{Fore.RED}[Permission Denied]{Style.RESET_ALL}")
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
                        print(f"{prefix}{connector}{Fore.BLUE}{Style.BRIGHT}{item}/{Style.RESET_ALL}")
                        _build_tree(item_path, prefix + child_prefix, current_depth + 1)
                    else:
                        from .lister import FileList
                        # color coding based on file extension
                        _, ext = os.path.splitext(item)
                        ext_color = FileList.EXTENSION_COLORS.get(ext.lower(), Fore.GREEN)

                        print(f"{prefix}{connector}{ext_color}{item}{Style.RESET_ALL}")

            _build_tree(target_dir)
            print(f"\n{Fore.CYAN}--- End of Directory Tree ---{Style.RESET_ALL}\n")

        except (PermissionError, FileNotFoundError) as e:
            print(f"{Fore.RED}Error rendering directory tree: {e}{Style.RESET_ALL}")

    @staticmethod
    def fileopn(filepath):
        import sys
        try:
            full_path = DirLocation._resolve_path(filepath)
            if not os.path.exists(full_path):
                print(f"File {Fore.RED}{filepath}{Style.RESET_ALL} does not exist.")
                return None

            # first, check if it's a python script
            if filepath.endswith(".py"):
                print(f"Executing {Fore.GREEN}{filepath}{Style.RESET_ALL}...")

                # run the python script
                result = subprocess.run(
                    [sys.executable, full_path],
                    capture_output=True,
                    text=True,
                    check=True
                )

                # check if execution threw an error to show in shell
                if result.returncode != 0:
                    traceback_str = result.stderr
                    print(f"{Fore.MAGENTA}Execution returns an exception:{Style.RESET_ALL}\n{traceback_str}")
                    return traceback_str
                else:
                    if result.stdout:
                        print(result.stdout, end="")
                    print(f"{Fore.GREEN}Process finished with exit code {Fore.CYAN}{result.returncode}{Style.RESET_ALL}")
                    return None
            else:
                print(f"Opening {Fore.GREEN}{filepath}{Style.RESET_ALL}...")
                if os.name == "nt":
                    os.startfile(full_path)
                elif platform.system() == "Darwin":
                    subprocess.run(["open", full_path], check=True)
                else:
                    subprocess.run(["xdg-open", full_path], check=True)
                return None

        except (PermissionError, FileNotFoundError) as e:
            print(f"{Fore.RED}Error opening file: {e}{Style.RESET_ALL}")
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
                        print(f"Closed process {Fore.GREEN}{proc.info['name']}{Style.RESET_ALL} (PID: {proc.info['pid']}).")
                        terminated = True
                except (psutil.NoSuchProcess, psutil.AccessDenied): continue
            if not terminated: print(f"No running process found matching {Fore.YELLOW}{process_name_or_file}{Style.RESET_ALL}.")
        except (PermissionError, psutil.NoSuchProcess, psutil.AccessDenied) as e:
            print(f"{Fore.RED}Error closing file process: {e}{Style.RESET_ALL}")

    @staticmethod
    def filecrt(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath)
            if os.path.exists(full_path): print(f"File {Fore.YELLOW}{filepath}{Style.RESET_ALL} already exists.")
            else:
                open(full_path, "a").close()
                print(f"File {Fore.GREEN}{filepath}{Style.RESET_ALL} created successfully.")
        except (PermissionError) as e: print(f"{Fore.RED}Error creating file: {e}{Style.RESET_ALL}")

    @staticmethod
    def dircrt(filepath):
        try:
            # Resolve target path relative to current working directory
            full_path = os.path.abspath(os.path.join(base_dir, filepath)) if not os.path.isabs(filepath) else filepath
            if os.path.exists(full_path):
                print(f"Directory or path {Fore.YELLOW}{filepath}{Style.RESET_ALL} already exists.")
            else:
                os.makedirs(full_path, exist_ok=True)
                print(f"Directory {Fore.GREEN}{filepath}{Style.RESET_ALL} created successfully.")
        except PermissionError as e:
            print(f"{Fore.RED}Error creating directory: {e}{Style.RESET_ALL}")

    @staticmethod
    def dirdel(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath)
            if os.path.exists(full_path) and os.path.isdir(full_path):
                os.rmdir(full_path)
                print(f"Directory {Fore.GREEN}{filepath}{Style.RESET_ALL} deleted successfully.")
            else:
                print(f"Directory {Fore.RED}{filepath}{Style.RESET_ALL} does not exist or is not a folder.")
        except PermissionError as e:
            print(f"{Fore.RED}Error deleting directory: {e}{Style.RESET_ALL}")

    @staticmethod
    def filerd(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath)
            if os.path.exists(full_path):
                with open(full_path, "r", encoding="utf-8") as f: content = f.read()
                print(f"\n--- Contents of {Fore.CYAN}{filepath}{Style.RESET_ALL} ---\n{content}\n--- End of file ---")
            else: print(f"File {Fore.RED}{filepath}{Style.RESET_ALL} does not exist.")
        except PermissionError as e: print(f"{Fore.RED}Error reading file: {e}{Style.RESET_ALL}")

    @staticmethod
    def filedel(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath)
            if os.path.exists(full_path):
                os.remove(full_path)
                print(f"File {Fore.GREEN}{filepath}{Style.RESET_ALL} deleted successfully.")
            else: print(f"File {Fore.RED}{filepath}{Style.RESET_ALL} does not exist.")
        except PermissionError as e: print(f"{Fore.RED}Error deleting file: {e}{Style.RESET_ALL}")

    @staticmethod
    def filewrt(filepath, content=None):
        import ast

        from .lister import CommandList

        class QuickLinter(ast.NodeVisitor):
            """AST Visitor that checks for warnings beyond syntax errors."""
            def __init__(self):
                self.warnings = []

            def visit_FunctionDef(self, node):
                # 1. Snake_case check for function names
                if any(c.isupper() for c in node.name):
                    self.warnings.append(f"Line {node.lineno}: Function '{node.name}' should use snake_case.")

                # 2. Check for unused arguments
                args = [a.arg for a in node.args.args if a.arg != "self"]
                used_vars = {child.id for child in ast.walk(node) if isinstance(child, ast.Name)}
                for arg in args:
                    if arg not in used_vars and not arg.startswith("_"):
                        self.warnings.append(f"Line {node.lineno}: Unused argument '{arg}' in function '{node.name}'.")

                self.generic_visit(node)

            def visit_ClassDef(self, node):
                # 3. PascalCase check for class names
                if not node.name[0].isupper() or "_" in node.name:
                    self.warnings.append(f"Line {node.lineno}: Class '{node.name}' should use PascalCase/CamelCase.")
                self.generic_visit(node)

            def visit_Import(self, node):
                # 4. Discourage wildcard or bad import practices
                for alias in node.names:
                    if alias.name == "sys" or alias.name == "os":
                        # Example: check or flag global usages
                        pass
                self.generic_visit(node)

            def visit_Call(self, node):
                # 5. Flag dangerous functions like eval() or exec()
                if isinstance(node.func, ast.Name) and node.func.id in ("eval", "exec"):
                    self.warnings.append(f"Line {node.lineno}: Use of unsafe function '{node.func.id}()'.")
                self.generic_visit(node)

        def _run_linter(code_str):
            """Parses code and runs AST checks, returning formatted warning strings."""
            try:
                tree = ast.parse(code_str)
                linter = QuickLinter()
                linter.visit(tree)
                return linter.warnings, None
            except SyntaxError as se:
                return [], f"SyntaxError on line {se.lineno}, col {se.offset}: {se.msg}"
            except NameError as ne:
                return [], f"NameError on line {ne.lineno}, col {ne.offset}: {ne.msg}"

        try:
            full_path = DirLocation._resolve_path(filepath)

            if content is None:
                print(f"{Fore.CYAN}--- Interactive Line Editor for '{filepath}' ---{Style.RESET_ALL}")
                print(CommandList.FWRTlist)

                lines = []
                if os.path.exists(full_path):
                    try:
                        with open(full_path, "r", encoding="utf-8") as f:
                            lines = f.read().splitlines()
                        if lines:
                            print(f"{Fore.LIGHTBLACK_EX}Loaded existing file content ({len(lines)} lines).{Style.RESET_ALL}")
                    except PermissionError:
                        """just dont give two shiis"""

                while True:
                    try:
                        line = input()
                        cmd = line.strip()

                        if cmd in [":w", ":x", ":save", "EOF", ":EOF", "END"]:
                            if filepath.endswith(".py"):
                                warnings, syntax_err = _run_linter("\n".join(lines))
                                if syntax_err:
                                    print(f"{Fore.RED}[Linter] {syntax_err}{Style.RESET_ALL}")
                                    confirm = input(f"{Fore.YELLOW}Save with syntax error? (y/N): {Style.RESET_ALL}").strip().lower()
                                    if confirm != 'y':
                                        continue
                                elif warnings:
                                    print(f"{Fore.YELLOW}[Linter Warnings]:{Style.RESET_ALL}")
                                    for w in warnings:
                                        print(f" - {Fore.YELLOW}{w}{Style.RESET_ALL}")
                            break

                        elif cmd == ":q":
                            print(f"{Fore.YELLOW}Changes discarded.{Style.RESET_ALL}")
                            return

                        elif cmd in [":lint", ":check", ":lt"]:
                            warnings, syntax_err = _run_linter("\n".join(lines))
                            if syntax_err:
                                print(f"{Fore.RED}[Linter] {syntax_err}{Style.RESET_ALL}")
                            elif warnings:
                                print(f"{Fore.YELLOW}[Linter Found {len(warnings)} Warning(s)]:{Style.RESET_ALL}")
                                for w in warnings:
                                    print(f" - {Fore.YELLOW}{w}{Style.RESET_ALL}")
                            else:
                                print(f"{Fore.GREEN}[Linter] Check return no errors.{Style.RESET_ALL}")

                        elif cmd in [":l", ":list"]:
                            print(f"\n{Fore.CYAN}--- Buffer Preview ---{Style.RESET_ALL}")
                            for idx, l in enumerate(lines, 1):
                                print(f"{Fore.YELLOW}{idx:3d} |{Style.RESET_ALL} {l}")
                            print(f"{Fore.CYAN}-----------------------{Style.RESET_ALL}\n")

                        elif cmd == ":c":
                            lines.clear()
                            print(f"{Fore.RED}Buffer cleared.{Style.RESET_ALL}")

                        elif cmd.startswith(":d"):
                            parts = cmd.split(maxsplit=1)
                            if len(parts) == 2 and parts[1].isdigit():
                                idx = int(parts[1]) - 1
                                if 0 <= idx < len(lines):
                                    removed = lines.pop(idx)
                                    print(f"{Fore.RED}Removed line {idx+1}: {Style.RESET_ALL}{removed}")
                                else:
                                    print(f"{Fore.RED}Invalid line number.{Style.RESET_ALL}")
                            else:
                                print(f"{Fore.RED}Usage: :d <line_number>{Style.RESET_ALL}")

                        elif cmd.startswith(":i"):
                            parts = cmd.split(maxsplit=2)
                            if len(parts) >= 3 and parts[1].isdigit():
                                idx = int(parts[1]) - 1
                                new_text = parts[2]
                                if 0 <= idx <= len(lines):
                                    lines.insert(idx, new_text)
                                    print(f"{Fore.GREEN}Inserted line {idx+1}.{Style.RESET_ALL}")
                                else:
                                    print(f"{Fore.RED}Line number out of range.{Style.RESET_ALL}")
                            else:
                                print(f"{Fore.RED}Usage: :i <line_number> <text>{Style.RESET_ALL}")

                        elif cmd in [":h", ":help"]:
                            print(CommandList.FWRTlist)

                        else:
                            lines.append(line)

                    except KeyboardInterrupt:
                        print(f"\n{Fore.RED}Write operation cancelled.{Style.RESET_ALL}")
                        return
                content = "\n".join(lines)

            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Content written to {Fore.GREEN}{filepath}{Style.RESET_ALL} successfully.")
        except PermissionError as e:
            print(f"{Fore.RED}Error writing to file: {e}{Style.RESET_ALL}")

    @staticmethod
    def filesort(dirpath, file_ext, dirdest):
        try:
            import shutil
            source_dir = DirLocation._resolve_path(dirpath)
            dest_dir = DirLocation._resolve_path(dirdest)

            if not os.path.exists(source_dir) or not os.path.isdir(source_dir):
                print(f"{Fore.RED}Source directory '{dirpath}' does not exist or is not a directory.{Style.RESET_ALL}")
                return

            os.makedirs(dest_dir, exist_ok=True)
            if not file_ext.startswith("."):
                file_ext = f".{file_ext}"
            file_ext = file_ext.lower()

            moved_count = 0
            for item in os.listdir(source_dir):
                src_file_path = os.path.join(source_dir, item)

                if os.path.isdir(src_file_path):
                    continue

                if item.lower().endswith(file_ext):
                    dest_file_path = os.path.join(dest_dir, item)
                    shutil.move(src_file_path, dest_file_path)
                    moved_count += 1

            print(f"{Fore.GREEN}Successfully moved {moved_count} file(s) with extension '{file_ext}' to '{dirdest}'.{Style.RESET_ALL}")
        except (PermissionError) as e:
            print(f"{Fore.RED}Error moving files into destination '{dirdest}': {e}{Style.RESET_ALL}")

# do not move, its sensitive and it may do nothing