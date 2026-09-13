"""EasySaxo Alpha Main configuration."""
import os
import time

import psutil
from colorama import Fore, Style


class App:
    def __init__(self, name, ver):
        self.name = name
        self.ver = ver
        self.dev = "SXF"
        self.start_time = time.time()
        self.tag = f"{Fore.CYAN}[{name}]{Style.RESET_ALL} |>"
        self.mute = True
        self.logger = {
            # No character before number indicates a general error message
            "1": "Unknown/malformed command.",
            "2": "No arguments provided.",
            "3": "Operation failed.",
            "4": "Permission denied or access error.",
            "5": "File or directory not found.",
            "6": "Invalid input or value error.",
            "7": "Network or connection error.",
            "8": "Request or API error.",
            "9": "System command execution failed.",
            "10": "Unexpected error occurred.",
            "11": "Operation canceled",
            # 'a' before number indicates an info message
            "a0": "Exiting app.",
            "a1": "Condition already evaluated.",
            # 'f' before number indicates specific file error
            "f1": "Invalid file or path.",
            "f2": "Path is not a directory.",
            "f3": "Path is not a file.",
            "f4": "Path exists.",
            # 'p' before number indicates specific process error
            "p1": "Process does not exist.",
            # 'm' before number indicates specific math error
            "m1": "Cannot operate term.",
            "m2": "Variable does not exist.",
            "m3": "Term does not exist."
        }

    def k_log(self, log):
        """ 
            # No character before number indicates a general error message
            "1": "Unknown/malformed command."
            "2": "No arguments provided."
            "3": "Operation failed."
            "4": "Permission denied or access error."
            "5": "File or directory not found."
            "6": "Invalid input or value error."
            "7": "Network or connection error."
            "8": "Request or API error."
            "9": "System command execution failed."
            "10": "Unexpected error occurred."
            "11": "Operation canceled"

            # 'a' before number indicates an info message
            "a0": "Exiting app."

            # 'f' before number indicates specific file error
            "f1": "Invalid file or path."
            "f2": "Path is not a directory."
            "f3": "Path is not a file."
            "f4": "Path exists."

            # 'p' before number indicates specific process error
            "p1": "Process does not exist."
            
            # 'm' before number indicates specific math error
            "m1": "Cannot operate term."
            "m2": "Variable does not exist."
            "m3": "Term does not exist."
        """
        if self.mute == True: return
        print(f"{self.tag} {Fore.RED}(Code: {log}) {self.logger[log]}{Style.RESET_ALL}")

    def disclaim(self, disclaimer):
        """Disclaimer for app, info displayer."""
        print(f"{self.tag} {disclaimer}")

    def state(self):
        """Displays session information, build version, log state, and resource usage."""

        _bld = app_databuild()
        build = f"{self.ver} (Build Date: {_bld})"

        elapsed_seconds = int(time.time() - self.start_time)
        hours, remainder = divmod(elapsed_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        session_time = f"{hours:02d}h {minutes:02d}m {seconds:02d}s"

        log_status = f"{Fore.RED}Muted{Style.RESET_ALL}" if self.mute else f"{Fore.GREEN}Active{Style.RESET_ALL}"

        process = psutil.Process(os.getpid())
        mem_info = process.memory_info()
        mem_mb = mem_info.rss / (1024 * 1024)
        cpu_percent = process.cpu_percent(interval=0.1)

        print(f"\n{self.tag} {Fore.YELLOW}=== App State ==={Style.RESET_ALL}")
        print(f"  > Name & Version : {self.name} {build}")
        print(f"  > Developer      : {self.dev}")
        print(f"  > Session Time   : {session_time}")
        print(f"  > Logger State   : {log_status}")
        print(f"  > Memory Usage   : {mem_mb:.2f} MB")
        print(f"  > CPU Usage      : {cpu_percent:.1f}%")
        print(f"{Fore.CYAN}=" * 30 + f"{Style.RESET_ALL}\n")
        
easysaxo = App("EasySaxo", "Alpha 1.11.00") # yes im that lazy to write this ever again

COMMAND_REGISTRY = {}
GET_REGISTRY = {}
HELP_REGISTRY = {}

def register_command(name, aliases=None, help_text=None, registry=COMMAND_REGISTRY):
    """To register a command, use this decorator defining:
    - Command Name
    - Any alias (optional)
    - Help Text (neccesary)
    - Registry (leave empty for normal command registry)
    
    Keywords:
    - c = command
    - g = able-to-get attribute
    - b = base
    - s = system
    - t = telemetry"""
    def decorator(func):
        registry[name] = func
        HELP_REGISTRY[name] = help_text or func.__doc__ or "No usage details provided."
        if aliases:
            for alias in aliases:
                registry[alias] = func
                HELP_REGISTRY[alias] = HELP_REGISTRY[name]
        return func
    return decorator

import re


class Changelog:
    _r_title = f"Changelog! ({easysaxo.name} {easysaxo.ver})"
    _color_title = f"{Fore.CYAN}Changelog!{Style.RESET_ALL} ({Fore.CYAN}{easysaxo.name} {easysaxo.ver}{Style.RESET_ALL})"
    
    entries = [  # noqa: RUF012
        f"Added new commands: {Fore.BLUE}restart, sleep, lock, tempflush, dnsflush, app{Style.RESET_ALL}",
        f"Extended functionality for command: {Fore.BLUE}shutdown{Style.RESET_ALL}",
        f"Added {Fore.GREEN}path assurance disclaimers{Style.RESET_ALL} for path resolving.",
        f"Moved command as subcommand: {Fore.LIGHTBLUE_EX}unins{Style.RESET_ALL} -> {Fore.BLUE}app{Style.RESET_ALL}",
        f"Added {Fore.BLUE}app metadata{Style.RESET_ALL}",
        f"Restructured {Fore.LIGHTBLUE_EX}code base{Style.RESET_ALL} in app scripts.",
        f"Updated {Fore.GREEN}app and dev logos{Style.RESET_ALL}"
    ]

    @staticmethod
    def _strip_ansi(text: str) -> str: return re.sub(r'\x1b\[[0-9;]*m', '', text)

    @classmethod
    def print_box(cls):
        formatted_entries = []
        raw_lengths = []
        for i, entry in enumerate(cls.entries, 1):
            formatted = f"{i}. {entry}"
            formatted_entries.append(formatted)
            raw_lengths.append(len(cls._strip_ansi(formatted)))

        max_content_len = max(raw_lengths) if raw_lengths else 0
        min_header_len = len(cls._r_title) + 6
        inner_width = max(max_content_len, min_header_len) + 2

        needed_eq = inner_width - len(cls._r_title) - 2
        left_eq = "=" * (needed_eq // 2)
        right_eq = "=" * (needed_eq - len(left_eq))
        top_header = f"|{left_eq} {cls._color_title} {right_eq}|"

        print(f"\n{top_header}")
        print(f"|{' ' * inner_width}|")  # top space line

        for entry_text, raw_len in zip(formatted_entries, raw_lengths):
            padding = inner_width - raw_len - 1
            print(f"| {entry_text}{' ' * padding}|")

        print(f"|{' ' * inner_width}|")   # bottom space line
        print(f"|{'=' * inner_width}|")   # bottom border line

def whats_new(): Changelog.print_box()

def clr(): os.system('cls' if os.name == 'nt' else 'clear')

# insert

from prompt_toolkit.completion import Completer, Completion


class PathCompleter(Completer):
    def __init__(self, get_base_dir_func): self.get_base_dir = get_base_dir_func

    def get_completions(self, document, complete_event):
        from .esmodules.dirloct import DirLocation

        text = document.text_before_cursor
        parts = text.split(maxsplit=1)
        path_arg = parts[1] if len(parts) > 1 else ""

        # Extract active token if user is typing a second argument
        words = path_arg.split()
        active_word = words[-1] if words and not path_arg.endswith(" ") else ""

        if active_word.startswith("-<"):
            for flag_name in DirLocation.FLAGS:
                if flag_name.lower().startswith(active_word.lower()):
                    yield Completion(
                        flag_name,
                        start_position=-len(active_word),
                        display=flag_name,
                        meta="Dir Flag"
                    )
            return

        base_dir = self.get_base_dir()
        target_token = active_word

        if "/" in target_token or "\\" in target_token:
            dirname, prefix = os.path.split(target_token)
            
            # Check if path starts with a flag prefix (e.g., -<desk/folder)
            first_part = dirname.split(os.sep)[0].split("/")[0].lower()
            if first_part in DirLocation.FLAGS:
                resolved_base = DirLocation._resolve_path(first_part)
                sub_path = dirname[len(first_part):].lstrip("/\\")
                search_dir = os.path.join(resolved_base, sub_path)
            else: search_dir = os.path.join(base_dir, dirname) if not os.path.isabs(dirname) else dirname
        else:
            dirname = ""
            prefix = target_token
            search_dir = base_dir

        if not os.path.exists(search_dir) or not os.path.isdir(search_dir): return

        try:
            for item in os.listdir(search_dir):
                if item.lower().startswith(prefix.lower()):
                    full_path = os.path.join(search_dir, item)
                    is_dir = os.path.isdir(full_path)
                    display_name = item + ("/" if is_dir else "")
                    
                    completion_val = os.path.join(dirname, display_name) if dirname else display_name

                    yield Completion(
                        completion_val,
                        start_position=-len(target_token),
                        display=display_name
                    )
        except PermissionError: return

def build_completion_dict(translations: dict) -> dict:    
    from .esmodules.builtinrender import Image, TextToImage
    from .esmodules.dirloct import DirLocation, base_dir
    from .esmodules.lister import MathList
    
    path_completer = PathCompleter(lambda: base_dir)
    file_shortcut = path_completer and dict.fromkeys(DirLocation.FLAGS)
    
    # subcommand maps for base cmds
    subcommand_maps = {
        "get": dict.fromkeys(GET_REGISTRY),
        "help": {},
        "render": dict.fromkeys(Image.get_presets()),
        "banner": {
            "render": dict.fromkeys(TextToImage.get_presets()),
            "-r": dict.fromkeys(TextToImage.get_presets())
        },
        "set": {
            "name": None,
            "password": None, "pswd": None, "key": None,
            "variable": None, "var": None,
            "mode": {"sys": None, "app": None, "auto": None},
            "cmdmatch": {"sys": None, "app": None, "auto": None},
            "cmdrun": {"sys": None, "app": None, "auto": None},
            "pathdisplay": {"on": None, "off": None, "enable": None, "disable": None},
            "pathmode": {"on": None, "off": None, "enable": None, "disable": None},
            "language": None,
            "lang": None,
        },
        "reset": dict.fromkeys(("name", "username", "password", "pswd", "key", "all", "user")),
        "app": {
            "reset": None, "restart": None,
            "unins": None, "uninstall": None,
            "log": {"mute": None, "unmute": None, "codes": None,},
            "state": None,
            },
        f"{easysaxo.name.lower()}": {
            "reset": None, "restart": None,
            "unins": None, "uninstall": None,
            "log": {"mute": None, "unmute": None},
            },
        "math": {
            "pi": None, "e": None,
            **{f"{func}(": None for func in MathList.mathset if func not in MathList._uncallable}
        },
        "mathhelp": dict.fromkeys(MathList.mathset),
        
        "filecrt": file_shortcut,
        "createf": file_shortcut,
        "touch": file_shortcut,
        "dircrt": file_shortcut,
        "dcreate": file_shortcut,
        "mkdir": file_shortcut,
        "filerd": file_shortcut,
        "readf": file_shortcut,
        "cat": file_shortcut,
        "cd": file_shortcut,
        "unzip": file_shortcut,
        "uzip": file_shortcut,
        "extract": file_shortcut,
        "filelst": file_shortcut,
        "ls": file_shortcut,
        "fileopn": file_shortcut,
        "filedel": file_shortcut,
        "filewrt": file_shortcut,
        "filesz": file_shortcut,
        "dirsz": file_shortcut,
        "jsonrd": file_shortcut,
        "tree": file_shortcut,
        "playaudio": file_shortcut,
        "ddelete": file_shortcut,
        "dirdel": file_shortcut,

        "shutdown": dict.fromkeys(("/a", "-c", "abort", "cancel")), "turnoff": dict.fromkeys(("/a", "-c", "abort", "cancel")), "shut": dict.fromkeys(("/a", "-c", "abort", "cancel")),
        "restart": dict.fromkeys(("/a", "-c", "abort", "cancel")),
    }

    all_commands = list(COMMAND_REGISTRY.keys()) + list(translations.keys())
    subcommand_maps["help"] = dict.fromkeys(all_commands)

    func_to_cmds = {}
    for cmd_name, func_obj in COMMAND_REGISTRY.items():
        func_to_cmds.setdefault(func_obj, []).append(cmd_name)

    comp_dict = {}

    for func_obj, cmd_list in func_to_cmds.items():
        primary_match = next((cmd for cmd in cmd_list if cmd in subcommand_maps), None)
        
        subdict = subcommand_maps[primary_match] if primary_match else None
        
        for cmd in cmd_list: comp_dict[cmd] = subdict
            
    for trans_key in translations:
        if trans_key not in comp_dict: comp_dict[trans_key] = None

    return comp_dict

def app_databuild():
    import datetime

    from .esmodules.dirloct import PROJECT_ROOT, base_dir
    from .esmodules.lister import FileList

    is_at_root = (base_dir == PROJECT_ROOT)
    
    allow_files = []
    for f in FileList._allow:
        if is_at_root: allow_files.append(f if f.endswith(".py") else f"{f}.py")
        else: allow_files.append(f if f.endswith(".py") else f"{f}.py")

    mtimes = []
    total_size = 0

    for file_rel in allow_files:
        resolved_path = os.path.join(PROJECT_ROOT, file_rel)
        if os.path.exists(resolved_path):
            mtimes.append(os.path.getmtime(resolved_path))
            total_size += os.path.getsize(resolved_path)

    latest_mtime = max(mtimes) if mtimes else 0
    build_mdata_display = (
        datetime.datetime.fromtimestamp(latest_mtime, tz=datetime.UTC).strftime("%Y-%m-%d")
        if latest_mtime else "ubs"
    )

    return build_mdata_display