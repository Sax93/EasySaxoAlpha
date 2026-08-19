"""EasySaxo Alpha Main configuration."""
class App:
    def __init__(self, name, ver):
        self.name = name
        self.ver = ver
        self.dev = "SXF"
        self.problem = "in the chair"
easysaxo = App("EasySaxo", "Alpha 1.06") # yes im that lazy to write this ever again

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
        f"Fixed commands: {Fore.BLUE}filesz{Style.RESET_ALL} (due to missing registry).",
        f"Fixed command subprocess: {Fore.LIGHTBLUE_EX}fileopn{Style.RESET_ALL} (due to uncaught exceptions).",
        f"Fixed {Fore.LIGHTGREEN_EX}subprocess{Style.RESET_ALL} exception raise, along with {Fore.BLUE}get packages{Style.RESET_ALL} fix.",
        f"Applied {Fore.BLUE}render <preset>{Style.RESET_ALL} changes to {Fore.BLUE}banner render <preset>{Style.RESET_ALL}.",
        f"Enhanced autocompleter ({Fore.LIGHTCYAN_EX}support for some subcommand-ranged commands{Style.RESET_ALL}).",
        f"Fixed {Fore.BLUE}math{Style.RESET_ALL} parsing."
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

def build_completion_dict(translations: dict) -> dict:
    from .esmodules.builtinrender import Image, TextToImage
    from .esmodules.lister import MathList
    
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
        "math": {f"{func}(": None for func in MathList._reserved},
        "mathhelp": {func: None for func in MathList.mathset}
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