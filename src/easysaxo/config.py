"""EasySaxo Alpha Main configuration."""
class App:
    def __init__(self, name, ver):
        self.name = name
        self.ver = ver
        self.dev = "SXF"
        self.problem = "in the chair"
easysaxo = App("EasySaxo", "Alpha 1.07") # yes im that lazy to write this ever again

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
    header = f"===== {Fore.CYAN}Changelog!{Style.RESET_ALL} ({Fore.YELLOW}{easysaxo.name} {easysaxo.ver}{Style.RESET_ALL}) ====="
    entries = [  # noqa: RUF012  # Reserved for changelog purposes only.
        f"Removed command: {Fore.BLUE}runloc{Style.RESET_ALL} (due to '{Fore.BLUE}cd{Style.RESET_ALL}' command).",
        f"Added {Fore.LIGHTMAGENTA_EX}path completion{Style.RESET_ALL} to most commands which operate on files.",
        f"Fixed (and enhanced) {Fore.BLUE}path resolving{Style.RESET_ALL} and '{Fore.BLUE}check{Style.RESET_ALL}' command.",
        f"Structured {Fore.BLUE}help{Style.RESET_ALL} ({Fore.BLUE}command list{Style.RESET_ALL}) display.",
        f"{Fore.MAGENTA}File extension{Style.RESET_ALL} color scheme expanded.",
    ]
    
    _visible_header = re.sub(r'\x1b\[[0-9;]*m', '', header) # hide color cmds in terminal, so
    footer = "=" * len(_visible_header)                     # len(footer) matches len(header)

    def entry_x(self):
        for i, entry in enumerate(self.entries, 1): print(f"  {i}. {entry}")

Nw = Changelog()

def whats_new():
    print(Nw.header)
    Nw.entry_x()
    print(Nw.footer)

def clr(): # clear screen
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# its actually not pretty bad to be the 56th codeline in a config script.

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

