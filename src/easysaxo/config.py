"""EasySaxo Alpha Main configuration"""
class App:
    def __init__(self, name, ver):
        self.name = name
        self.ver = ver
        self.dev = "SXF"
        self.problem = "in the chair" 
easysaxo = App("EasySaxo", "Alpha 1.051") # yes im that lazy to write this ever again

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

# changelog
def whats_new():
    from colorama import Fore, Style
    print(
        f"\n===== {Fore.CYAN}Changelog!{Style.RESET_ALL} ({Fore.YELLOW}{easysaxo.name} v{easysaxo.ver}{Style.RESET_ALL}) =====\n"
        f"1. Added subcommand for {Fore.BLUE}'banner'{Style.RESET_ALL}: {Fore.LIGHTBLUE_EX}'render <doodle>'{Style.RESET_ALL}.\n"
        f"2. Minor bugfixes in {Fore.MAGENTA}commands, config, misc{Style.RESET_ALL}.\n"
        f"3. Changed name: {Fore.BLUE}'changelog'{Style.RESET_ALL}."
    )
    
def clr(): # clear screen
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# its beautiful to be the 38th codeline in a config script.