"""EasySaxo Alpha Main configuration"""
class App:
    def __init__(self, name, ver):
        self.name = name
        self.ver = ver
        self.dev = "SXF"
        self.problem = "in the chair"
easysaxo = App("EasySaxo", "Alpha 1.053.2") # yes im that lazy to write this ever again

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
    header = f"===== {Fore.CYAN}Changelog!{Style.RESET_ALL} ({Fore.YELLOW}{easysaxo.name} v{easysaxo.ver}{Style.RESET_ALL}) ====="
    entries = [  # noqa: RUF012  # Reserved for changelog purposes only.
        f"Added commands: {Fore.BLUE}shutdown{Style.RESET_ALL}.",
        f"Bugfixes in {Fore.MAGENTA}code organization{Style.RESET_ALL}, {Fore.LIGHTBLUE_EX}precise error handling{Style.RESET_ALL}.",
        f"Various enhancements in {Fore.MAGENTA}main{Style.RESET_ALL} file.",
        f"Minor bugfixes in {Fore.MAGENTA}commands, dirloct, misc{Style.RESET_ALL}.",
        f"Minor bugfixes in {Fore.BLUE}render{Style.RESET_ALL} command.",
    ]
    _visible_header = re.sub(r'\x1b\[[0-9;]*m', '', header) # hide color cmds in terminal, so
    footer = "=" * len(_visible_header)                     # len(footer) matches len(header)

    def entry_x(self):
        for i, entry in enumerate(self.entries, 1):
            print(f"  {i}. {entry}")

Nw = Changelog()

def whats_new():
    print(Nw.header)
    Nw.entry_x()
    print(Nw.footer)

def clr(): # clear screen
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# its ASTONISHING to be the 58th codeline in a config script.