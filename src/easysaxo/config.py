"""EasySaxo Alpha Main configuration."""
class App:
    def __init__(self, name, ver):
        self.name = name
        self.ver = ver
        self.dev = "SXF"
        self.problem = "in the chair"
easysaxo = App("EasySaxo", "Alpha 1.09") # yes im that lazy to write this ever again

COMMAND_REGISTRY = {}
GET_REGISTRY = {}
HELP_REGISTRY = {}

def register_command(name, aliases=None, help_text=None, registry=COMMAND_REGISTRY):
    # do NOT even dare moving a thing here bro
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

from colorama import Fore, Style


class Changelog:
    _r_title = f"Changelog! ({easysaxo.name} {easysaxo.ver})"
    _color_title = f"{Fore.CYAN}Changelog!{Style.RESET_ALL} ({Fore.CYAN}{easysaxo.name} {easysaxo.ver}{Style.RESET_ALL})"
    
    entries = [  # noqa: RUF012
        f"Added new commands: {Fore.BLUE}unzip{Style.RESET_ALL}",
        f"Updated flag format for system shell commands (does not affect '-s' or '-e'): {Fore.LIGHTBLUE_EX}-<{Style.RESET_ALL}.",
        f"Fixed commands by uncaught exceptions: {Fore.BLUE}regex, dirsz, dirdel{Style.RESET_ALL}.",
        f"Updated command functionality for: {Fore.BLUE}filerd, web{Style.RESET_ALL}.",
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

def clr(): # clear screen
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# he was whipping up ANGER IN A KETTLE

import os

from prompt_toolkit.completion import Completer, Completion


class PathCompleter(Completer):
    def __init__(self, get_base_dir_func):
        self.get_base_dir = get_base_dir_func

    def get_completions(self, document, complete_event):
        full_text = document.text_before_cursor
        parts = full_text.split(maxsplit=1)
        text = parts[1] if len(parts) > 1 else ""

        base_dir = self.get_base_dir()

        if "/" in text or "\\" in text:
            dirname, prefix = os.path.split(text)
            search_dir = os.path.join(base_dir, dirname) if not os.path.isabs(dirname) else dirname
        else:
            dirname = ""
            prefix = text
            search_dir = base_dir

        if not os.path.exists(search_dir) or not os.path.isdir(search_dir): return

        try:
            for item in os.listdir(search_dir):
                if item.startswith(prefix):
                    full_path = os.path.join(search_dir, item)
                    display = item + ("/" if os.path.isdir(full_path) else "")
                    completion_val = os.path.join(dirname, display) if dirname else display
                    
                    yield Completion(
                        completion_val,
                        start_position=-len(prefix),  # Replace only the typed prefix
                        display=display
                    )
        except PermissionError: return

def build_completion_dict(translations: dict) -> dict:    
    from .esmodules.builtinrender import Image, TextToImage
    from .esmodules.dirloct import DirLocation, base_dir
    from .esmodules.lister import MathList
    
    path_completer = PathCompleter(lambda: DirLocation.base_dir if hasattr(DirLocation, 'base_dir') else base_dir)
    
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
            "lang": None
        },
        "reset": dict.fromkeys(("name", "username", "password", "pswd", "key", "all", "user")),
        "math": {
            "pi": None, "e": None,
            **{f"{func}(": None for func in MathList.mathset if func not in MathList._uncallable}
        },
        "mathhelp": dict.fromkeys(MathList.mathset),
        
        "filerd": path_completer,   # when the user types something like
        "readf": path_completer,    # 'C:/', the pathcompleter function
        "cat": path_completer,      # will do its job :p
        "cd": path_completer,
        "unzip": path_completer,
        "uzip": path_completer,
        "extract": path_completer,
        "filelst": path_completer,
        "ls": path_completer,
        "fileopn": path_completer,
        "filedel": path_completer,
        "filewrt": path_completer,
        "filesz": path_completer,
        "jsonrd": path_completer,
        "tree": path_completer,
        "playaudio": path_completer,
        "ddelete": path_completer,
        "dirdel": path_completer,
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
        if trans_key not in comp_dict:
            comp_dict[trans_key] = None

    return comp_dict


def app_databuild():
    import datetime

    from .esmodules.dirloct import PROJECT_ROOT, DirLocation, base_dir
    from .esmodules.lister import FileList

    FileList._allow = [f"{file}.py" for file in FileList._allow] if base_dir is PROJECT_ROOT else [file for file in FileList._allow]

    mtimes = []
    total_size = 0

    for file_rel in FileList._allow:
        resolved_path = DirLocation._resolve_path(file_rel) if base_dir is PROJECT_ROOT else os.path.join(PROJECT_ROOT, file_rel)
        if os.path.exists(resolved_path):
            mtimes.append(os.path.getmtime(resolved_path))
            total_size += os.path.getsize(resolved_path)

    latest_mtime = max(mtimes) if mtimes else 0
    build_mdata_display = (
        datetime.datetime.fromtimestamp(latest_mtime, tz=datetime.UTC).strftime("%Y-%m-%d")
        if latest_mtime
        else "N/A"
    )

    return build_mdata_display