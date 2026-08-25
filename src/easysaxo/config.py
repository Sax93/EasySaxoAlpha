"""EasySaxo Alpha Main configuration."""
class App:
    def __init__(self, name, ver):
        self.name = name
        self.ver = ver
        self.dev = "SXF"
        self.problem = "in the chair"
easysaxo = App("EasySaxo", "Alpha 1.082") # yes im that lazy to write this ever again

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
    _raw_title = f"Changelog! ({easysaxo.name} {easysaxo.ver})"
    _color_title = f"{Fore.CYAN}Changelog!{Style.RESET_ALL} ({Fore.CYAN}{easysaxo.name} {easysaxo.ver}{Style.RESET_ALL})"
    
    entries = [  # noqa: RUF012
        f"Added commands: {Fore.BLUE}web, dirsz{Style.RESET_ALL} ({Fore.CYAN}help web{Style.RESET_ALL} / {Fore.CYAN}help dirsz{Style.RESET_ALL} for quick description).",
        f"Added flag to system-shell command: {Fore.LIGHTBLUE_EX}-silent{Style.RESET_ALL} (hides error display if encountered).",
        f"Updated minimum and recommended {Fore.BLUE}requirements{Style.RESET_ALL} to run {easysaxo.name}.",
        f"Removed unused dependencies from {Fore.RED}pyproject.toml{Style.RESET_ALL}, app optimization by debloating.",
        f"{Fore.LIGHTYELLOW_EX}KeyboardInterrupt{Style.RESET_ALL} error from startup patched.",
        f"Added {Fore.LIGHTGREEN_EX}country flags{Style.RESET_ALL} as preset doodles to command line: {Fore.CYAN}banner render <doodle>{Style.RESET_ALL}.",
        f"Modified {Fore.LIGHTMAGENTA_EX}path display{Style.RESET_ALL} along with {Fore.BLUE}cd{Style.RESET_ALL} command.",
        f"Added {Fore.LIGHTGREEN_EX}build date{Style.RESET_ALL} to app metadata.",
        f"Updated {Fore.CYAN}Changelog{Style.RESET_ALL} display."
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
        min_header_len = len(cls._raw_title) + 6
        inner_width = max(max_content_len, min_header_len) + 2

        needed_eq = inner_width - len(cls._raw_title) - 2
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
        text = document.text_before_cursor
        base_dir = self.get_base_dir()

        if "/" in text or "\\" in text:  # path split
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
                        start_position=-len(text),
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
        "get": {subcmd: None for subcmd in GET_REGISTRY},
        "help": {},
        "render": {preset: None for preset in Image.get_presets()},
        "banner": {
            "render": {preset: None for preset in TextToImage.get_presets()},
            "-r": {preset: None for preset in TextToImage.get_presets()}
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
        "reset": {rval: None for rval in ("name", "username", "password", "pswd", "key", "all", "user")},
        "math": {
            "pi": None, "e": None,
            **{f"{func}(": None for func in MathList.mathset if func not in MathList._uncallable}
        },
        "mathhelp": {func: None for func in MathList.mathset},
        
        "filerd": path_completer,   # when the user types something like
        "readf": path_completer,    # 'C:/', the pathcompleter function
        "cat": path_completer,      # will do its job :p
        "cd": path_completer,
        "filelst": path_completer,
        "ls": path_completer,
        "fileopn": path_completer,
        "filedel": path_completer,
        "filewrt": path_completer,
        "filesz": path_completer,
        "jsonrd": path_completer,
        "tree": path_completer,
        "playaudio": path_completer
    }

    all_commands = list(COMMAND_REGISTRY.keys()) + list(translations.keys())
    subcommand_maps["help"] = {cmd: None for cmd in all_commands}

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