"""EasySaxo Alpha Command Input/Registry"""
# NOTE: `commands.py` is strictly for command creation, not meant to support other than command registering.

import os, time, sys, shutil, subprocess
from .config import register_command, GET_REGISTRY, HELP_REGISTRY, easysaxo, clr
from .esmodules.computer import ComputerData
from .esmodules.telemetry import TelemetryData
from .esmodules.dirloct import DirLocation, base_dir
from .esmodules.mathf import MathFunc
from .esmodules.misc import whats_new, hrs, StatusHandler, module_importing, StHd, bootcheck
from .esmodules.jsonregex import JsonData, RegexData
from .esmodules.medi import MediaData
from .esmodules.heavyholder import ThreadData, SessionManager
from .esmodules.lister import MATHSET_HELP, mathset, required_modules
from colorama import Fore, Style

ee4 = True
developer = "ID-10T"

#=================================================
# Command Mappings
#=================================================

# For in-MathSet guide
for math_key, help_str in MATHSET_HELP.items():
    HELP_REGISTRY[math_key] = help_str

# =========== EASTER EGGS SECTION ============
from .esmodules import easters
import random

def e1():
    easters.eas1()

def e2():
    easters.eas2()
        
def e3():
    from .esmodules.lister import osaka
    print(f"{Fore.LIGHTYELLOW_EX}{random.choice(osaka)} :D{Style.RESET_ALL}")

def e4():
    global ee4
    easters.eas4()
    ee4 = False
    return ee4

def e5():
    easters.eas5()

# =========== ATTRIBUTES FOR 'GET' ===========

@register_command("cpu", aliases=["processor"], registry=GET_REGISTRY, help_text="get cpu - Displays CPU details and usage statistics.")
def g_cpu(): ComputerData.getcpu()

@register_command("arch", aliases=["sysarch", "architecture"], registry=GET_REGISTRY, help_text="get arch - Displays architecture and byte order.")
def g_arch(): ComputerData.getarch()

@register_command("os", aliases=["system", "sys"], registry=GET_REGISTRY, help_text="get os - Displays OS name and version details.")
def g_os(): ComputerData.getos()

@register_command("ram", aliases=["memoryram", "memory"], registry=GET_REGISTRY, help_text="get ram - Displays system RAM and Swap usage.")
def g_ram(): ComputerData.getram()

@register_command("gpu", aliases=["videoboard", "video", "graphic"], registry=GET_REGISTRY, help_text="get gpu - Displays GPU hardware information.")
def g_gpu(): ComputerData.getgpu()

@register_command("disk", aliases=["drive", "drives", "disks"], registry=GET_REGISTRY, help_text="get disk - Displays disk partitions and usage.")
def g_disk(): ComputerData.getdisk()

@register_command("motherboard", registry=GET_REGISTRY, help_text="get motherboard - Displays motherboard details.")
def g_mboard(): ComputerData.getmotherboard()

@register_command("battery", aliases=["bat"], registry=GET_REGISTRY, help_text="get battery - Displays battery status.")
def g_batt(): ComputerData.getbattery()

@register_command("user", aliases=["sysuser"], registry=GET_REGISTRY, help_text="get user - Displays logged user and hostname.")
def g_user(): ComputerData.getuserinfo()

@register_command("python", aliases=["py", "pydata"], registry=GET_REGISTRY, help_text="get python - Displays Python version and path info.")
def g_py(): ComputerData.getpythoninfo()

@register_command("packages", aliases=["pypack"], registry=GET_REGISTRY, help_text="get packages - Lists installed pip packages.")
def g_pkg(): ComputerData.getinstalledpackages()

@register_command("env", registry=GET_REGISTRY, help_text="get env - Displays environment variables.")
def g_env(): ComputerData.getenvvars()

@register_command("processes", aliases=["tasks"], registry=GET_REGISTRY, help_text="get processes - Displays top CPU processes.")
def g_proc(): ComputerData.getprocesses()

@register_command("net", aliases=["network"], registry=GET_REGISTRY, help_text="get net - Displays network traffic statistics.")
def g_net(): TelemetryData.getnet()

@register_command("upt", aliases=["uptime"], registry=GET_REGISTRY, help_text="get upt - Displays system uptime.")
def g_upt(): TelemetryData.getupt()

@register_command("ip", aliases=["ipaddress"], registry=GET_REGISTRY, help_text="get ip - Displays local network IP addresses.")
def g_ip(): TelemetryData.getip()

@register_command("mac", aliases=["macaddress"], registry=GET_REGISTRY, help_text="get mac - Displays primary MAC address.")
def g_mac(): TelemetryData.getmac()

@register_command("publicip", aliases=["pipaddress", "publicipaddress"], registry=GET_REGISTRY, help_text="get publicip - Displays public IP address.")
def g_pubip(): TelemetryData.getpublicip()

@register_command("netstats", aliases=["adastats", "adapter", "netadapter"], registry=GET_REGISTRY, help_text="get netstats - Displays network adapter statuses.")
def g_netstat(): TelemetryData.getnetstats()

@register_command("connections", registry=GET_REGISTRY, help_text="get connections - Displays active network connections.")
def g_conn(): TelemetryData.getconnections()

@register_command("speedtest", registry=GET_REGISTRY, help_text="get speedtest - Performs network speed test.")
def g_speed(): TelemetryData.speedtest_network()

@register_command("threads", registry=GET_REGISTRY, help_text="get threads - Displays active background threads.")
def g_th(): ThreadData.getthreads()

@register_command("mathset", registry=GET_REGISTRY, help_text="get mathset - Displays available math functions/constants.")
def g_mset(): MathFunc.getmath()

@register_command("vars", aliases=["variables"], registry=GET_REGISTRY, help_text="get vars - Lists user math variables.")
def g_vars(): MathFunc.list_vars()

@register_command("appname", registry=GET_REGISTRY, help_text="get appname - Displays app name.")
def g_appn(): print(f"App name: {Fore.CYAN}{easysaxo.name}{Style.RESET_ALL}")

@register_command("appver", aliases=["version"], registry=GET_REGISTRY, help_text="get appver - Displays app version.")
def g_appv(): print(f"App version: {Fore.CYAN}{easysaxo.ver}{Style.RESET_ALL}")

@register_command("appdev", aliases=["developer", "creator", "devs", "dev"], registry=GET_REGISTRY)
def g_appd():
    possible_devs = ["SXF", "SFX", "Your mom lol", developer]
    pctg = [98, 1.2, 0.7, 0.1]
    easysaxo.dev = random.choices(possible_devs, weights=pctg, k=1)[0]
    print(f"App developer: {Fore.CYAN}{easysaxo.dev}{Style.RESET_ALL}")

@register_command("app", aliases=["appinfo"], registry=GET_REGISTRY, help_text="get app - Displays general app details.")
def g_app(): print(f"App: {Fore.CYAN}{easysaxo.name} {easysaxo.ver}{Style.RESET_ALL} by {easysaxo.dev}")

@register_command("username", aliases=["name"], registry=GET_REGISTRY, help_text="get username - Displays registered user name (in app).")
def g_uname(): print(f"Username: {Fore.CYAN}{ThreadData.current_user}{Style.RESET_ALL}.")

@register_command("password", aliases=["pswd", "key"], registry=GET_REGISTRY, help_text="By privacy built-in configuration, you cannot get password.")
def g_pswd(): print(f"{Fore.RED}You cannot get password due to security protocols{Style.RESET_ALL}.")

@register_command("attr", aliases=["attribute", "all"], registry=GET_REGISTRY, help_text="get attr - Fetches all telemetry and system specs.")
def g_all():
    print(f"{Fore.BLUE}== COMPUTER DATA =={Style.RESET_ALL}")
    for func in [g_cpu, g_arch, g_os, g_mboard, g_ram, g_gpu, g_disk, g_batt, g_user, g_py]: func()
    print(f"\n{Fore.BLUE}== TELEMETRY DATA =={Style.RESET_ALL}")
    for func in [g_net, g_upt, g_ip, g_mac, g_pubip, g_netstat]: func()
    print(f"\n{Fore.BLUE}== THREADING/MATH DATA =={Style.RESET_ALL}")
    for func in [g_th, g_mset, g_vars]: func()
    print(f"\n{Fore.BLUE}== MISC DATA =={Style.RESET_ALL}")
    for func in [g_uname, g_appn, g_appv, g_appd]: func()


# =========== CORE COMMANDS + HELP ===========

@register_command("help", aliases=["?", "-h"], help_text="help [command] - Shows command list or syntax details for a target command.")
def c_help(arg):
    if not arg:
        from .esmodules.lister import CMDlist
        print(CMDlist)
    else:
        target = arg.lower().strip()
        if target in HELP_REGISTRY:
            print(f"\n{Fore.GREEN}=== Usage for '{target}' ==={Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{HELP_REGISTRY[target]}{Style.RESET_ALL}\n")
        elif target in GET_REGISTRY and target in HELP_REGISTRY:
            print(f"\n{Fore.GREEN}=== Usage for 'get {target}' ==={Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{HELP_REGISTRY[target]}{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.RED}No usage details found for '{arg}'. Type 'help' for options.{Style.RESET_ALL}")

@register_command("exit", aliases=["quit", "kill", "-q"], help_text="exit - Save session state and exit app.")
def c_exit(arg):
    SessionManager.save_session(ThreadData.current_user)
    sys.exit(0)

@register_command("clear", aliases=["clr", "clrscr"], help_text="clear - Clears the terminal screen.")
def c_clear(arg): clr()

@register_command("save", help_text="save [filepath.json] - Saves the current session state along with its storable data.")
def c_save(arg): SessionManager.save_session(ThreadData.current_user, arg)

@register_command("load", help_text="load <filepath.json> - Loads session state and variables from a file.")
def c_load(arg):
    if arg:
        session_info = SessionManager.load_session(arg)
        if isinstance(session_info, dict):
            ThreadData.current_user = session_info.get("user_name", "User")
            ThreadData.current_pswd = session_info.get("password")
        else: ThreadData.current_user = session_info
    else: print(f"{Fore.RED}Usage: load <filepath.json>{Style.RESET_ALL}")
        
@register_command("delvar", help_text="delvar <var_name> - Deletes a user-defined math variable.")
def c_delvar(arg):
    if arg: MathFunc.del_var(arg); SessionManager.save_session(ThreadData.current_user)
    else: print(f"{Fore.RED}Usage: delvar <var_name>{Style.RESET_ALL}")

@register_command("del", help_text="del var <var_name> - Deletes a user-defined math variable.")
def c_del(arg):
    if arg and arg.lower().startswith("var "):
        MathFunc.del_var(arg.split(maxsplit=1)[1]); SessionManager.save_session(ThreadData.current_user)
    else: print(f"{Fore.RED}Usage: del var <var_name>{Style.RESET_ALL}")

@register_command("get", help_text="get <attribute|subcommand> - Fetches system metrics, variables, or specs.")
def c_get(arg):
    from .esmodules.misc import module_importing
    if not arg: print(f"{Fore.RED}Missing argument for 'get'. Type 'help' for options.{Style.RESET_ALL}")
    elif arg.startswith("module "): # checks specified mod
        mtocheck = arg.split(maxsplit=1)[1]
        for mod in mtocheck.replace(",", " ").split(): module_importing(mod.upper())
    elif arg == "module": module_importing(required_modules) # checks all modules
    elif arg in GET_REGISTRY: GET_REGISTRY[arg]()
    else: MathFunc.getvar(arg)

@register_command("runloc", aliases=["path", "location", "currentdir", "pwd"], help_text="runloc - Prints the current working directory path.")
def c_runloc(arg): DirLocation.runloc()

@register_command("check", aliases=["allowance", "checkf", "filechk"], help_text="check - Checks if all script files exist and are available.")
def c_check(arg): DirLocation.allowance()

@register_command("dircrt", aliases=(["dcreate", "mkdir"]), help_text="dircrt <dirname> - Creates a raw directory.")
def c_dircrt(arg): DirLocation.dircrt(arg) if arg else print(f"{Fore.RED}Missing directory name.{Style.RESET_ALL}")

@register_command("dirdel", aliases=(["ddelete", "rm-r", "rmdir"]), help_text="dirdel <dirname> - Deletes a directory.")
def c_dirdel(arg): DirLocation.dirdel(arg) if arg else print(f"{Fore.RED}Missing directory path.{Style.RESET_ALL}")

@register_command("filelst", aliases=["ls", "dir", "lsdir", "dirls", "listdir", "dirlist"], help_text="filelst [path] - Lists files and subdirectories in the specified or current directory.")
def c_filelst(arg): DirLocation.ls(arg)

@register_command("fileopn", aliases=["openf", "opn"], help_text="fileopn <filepath> - Opens a file with the default system application.")
def c_fileopn(arg): DirLocation.fileopn(arg) if arg else print(f"{Fore.RED}Missing filepath.{Style.RESET_ALL}")

@register_command("filecls", aliases=["closef", "clsf"], help_text="filecls <process_name> - Terminates process(es) matching the given name.")
def c_filecls(arg): DirLocation.filecls(arg) if arg else print(f"{Fore.RED}Missing process name.{Style.RESET_ALL}")

@register_command("filecrt", aliases=["createf", "touch"], help_text="filecrt <filepath> - Creates an empty file at the designated location.")
def c_filecrt(arg):
    if not arg:
        print(f"{Fore.RED}Missing filepath.{Style.RESET_ALL}")
        return
    parts = arg.split()
    if len(parts) == 2: target_path = os.path.join(parts[1], parts[0])
    else: target_path = parts[0]
    DirLocation.filecrt(target_path)

@register_command("filerd", aliases=["readf", "cat"], help_text="filerd <filepath> - Reads and prints text content from a target file.")
def c_filerd(arg): DirLocation.filerd(arg) if arg else print(f"{Fore.RED}Missing filepath.{Style.RESET_ALL}")

@register_command("filedel", aliases=["deletef", "rm"], help_text="filedel <filepath> - Permanently removes a file from disk.")
def c_filedel(arg): DirLocation.filedel(arg) if arg else print(f"{Fore.RED}Missing filepath.{Style.RESET_ALL}")

@register_command("filewrt", aliases=["writef"], help_text="filewrt <filepath> <content> - [ONE LINE] Overwrites target file with text content.")
def c_filewrt(arg):
    from .esmodules.lister import files_to_allow as rsv
    parts = arg.split(maxsplit=1) if arg else []
    if not parts: print(f"{Fore.RED}Usage: filewrt <filepath> <content>{Style.RESET_ALL}")
    target_file = parts[0][:-3] if parts[0].endswith(".py") else parts[0]
    if parts[0] in rsv or target_file in rsv:
        print(f"{Fore.LIGHTRED_EX}Hey, hey, no touching there.{Style.RESET_ALL}")
        return
    elif len(parts) == 2: DirLocation.filewrt(parts[0], parts[1])
    else: print(f"{Fore.RED}Usage: filewrt <filepath> <content>{Style.RESET_ALL}")

@register_command("jsonrd", help_text="jsonrd <filepath> - Parses and pretty-prints JSON file contents.")
def c_jsonrd(arg): JsonData.jsonrd(arg) if arg else print(f"{Fore.RED}Missing filepath.{Style.RESET_ALL}")

@register_command("regex", help_text="regex <pattern> <text/file> [-f]- Evaluates regex pattern against input text string.")
def c_regex(arg):
    parts = arg.split() if arg else []
    if len(parts) == 3 and parts[2] == "-f":
        textfile_path = DirLocation._resolve_path(parts[1])
        RegexData.match_file(parts[0], textfile_path)
    elif len(parts) >= 2:
        pattern = parts[0]
        text = " ".join(parts[1:]) # rejoin remaining parts in case text contains spaces
        RegexData.match_pattern(pattern, text)
    else: 
        print(f"{Fore.RED}Usage: regex <pattern> <text/file> [-f]{Style.RESET_ALL}")

@register_command("playaudio", aliases=["playa"],help_text="playaudio <filepath> - Plays an audio file asynchronously.")
def c_playaudio(arg): MediaData.playaudio(arg) if arg else print(f"{Fore.RED}Missing filepath.{Style.RESET_ALL}")

@register_command("stopaudio", aliases=["stopa"], help_text="stopaudio - Stops currently playing audio playback.")
def c_stopaudio(arg): MediaData.stopaudio()

@register_command("pkm", aliases=["pianomode", "pmode"], help_text="pkm - Enters one-octave piano mode [EXPERIMENTAL]")
def c_pkm(arg):
    from .esmodules.mamidi import run_piano
    run_piano()

@register_command("render", aliases=["asciiart", "art"], help_text="render <imagepath> [columnnum] - Renders an image in ASCII.")
def c_render(arg):
    from .esmodules.lister import RENlist
    if not arg:
        print(f"{Fore.RED}Usage: render <imgpath> [colnum]{Style.RESET_ALL}")
        return
    parts = arg.split()
    target = parts[0]
    colnum = parts[1] if len(parts) > 1 else "80"
    if target.upper() in RENlist:
        MediaData.render_preset(target.lower())
        return
    
    MediaData.render(target, colnum)

@register_command("banner", aliases=["tart", "amply"], help_text="banner <text> - Reprints the input text, bigger.")
def c_banner(arg): MediaData.txt2rt(arg) if arg else MediaData.txt2rt('Missing text!')

@register_command("set", help_text="set <varfeature> <val> - Updates session settings or math variables.")
def c_set(arg): # prob greatest cmd
    if not arg: print(f"{Fore.RED}Usage: set name/password <new_name/new_password>\nset var <var_name> <value>\nset cmdmatch es/sys{Style.RESET_ALL}")
    else:
        parts = arg.split(maxsplit=2)
        # edit username
        if parts[0].lower() == "name" and len(parts) >= 2:
            ThreadData.current_user = parts[1]
            print(f"User name replaced to {Fore.GREEN}{parts[1]}{Style.RESET_ALL}.")
            SessionManager.save_session(ThreadData.current_user)
            
        # edit/add variable
        elif parts[0].lower() in ["var", "variable"] and len(parts) == 3:
            MathFunc.set_var(parts[1], parts[2]); SessionManager.save_session(ThreadData.current_user)
        
        # set new password
        elif parts[0].lower() in ["password", "key", "pswd"] and len(parts) >= 2:
            import bcrypt
            plain_pwd = parts[1].encode('utf-8')
            hashed_bytes = bcrypt.hashpw(plain_pwd, bcrypt.gensalt())
            ThreadData.current_pswd = hashed_bytes.decode('utf-8')
            print(f"Password assigned successfully. It will load {Fore.MAGENTA}next session{Style.RESET_ALL}.")
            SessionManager.save_session(ThreadData.current_user)
        
        # set command match
        elif parts[0].lower() in ["cmdmatch", "cmdrun", "mode"] and len(parts) >= 2:
            mode_arg = parts[1].lower()
            if mode_arg in ["sys", "path", "device", "s"]: # system
                ThreadData.target_mode = "system"
                print(f"{Fore.LIGHTGREEN_EX}Default execution mode set to: System Shell{Style.RESET_ALL}")
            elif mode_arg in ["es", "app", "local", "e"]: # app
                ThreadData.target_mode = "easysaxo"
                print(f"{Fore.LIGHTCYAN_EX}Default execution mode set to: {easysaxo.name} Shell (Internal){Style.RESET_ALL}")
            else: # auto
                ThreadData.target_mode = "auto"
                print(f"{Fore.LIGHTYELLOW_EX}Default execution mode set to: Auto (EasySaxo -> System){Style.RESET_ALL}")
                print(f"You can either use {Fore.CYAN}'-e'{Style.RESET_ALL} to force app command, or {Fore.CYAN}'-s'{Style.RESET_ALL} to force system command!")
                
        else: print(f"{Fore.RED}Unknown/malformed set subcommand.{Style.RESET_ALL}")

@register_command("reset", help_text="reset <name/password>")
def c_reset(arg):
    if not arg: print(f"{Fore.RED}Usage: reset <name/password>{Style.RESET_ALL}")
    else:
        parts = arg.strip().split()
        if parts[0].lower() in ["name", "username"] and len(parts) == 1: # set username as User
            ThreadData.current_user = "User"
            print(f"User name set to {Fore.GREEN}User{Style.RESET_ALL}")
            SessionManager.save_session(ThreadData.current_user)
        elif parts[0].lower() in ["password", "pswd", "key"] and len(parts) == 1: # erase current password
            ThreadData.current_pswd = None
            print("Password cleared successfully.")
            SessionManager.save_session(ThreadData.current_user)
        elif parts[0].lower() in ["all", "user"] and len(parts) == 1: # reset user
            ThreadData.current_user = "User"
            ThreadData.current_pswd = None
            print("User values resetted.")
            SessionManager.save_session(ThreadData.current_user)
        else: print(f"{Fore.RED}Usage: reset <name/password>{Style.RESET_ALL}")

@register_command("timer", help_text="timer <seconds> [message] - Sets a non-blocking background countdown timer alert.")
def c_timer(arg):
    parts = arg.split(maxsplit=1) if arg else []
    if len(parts) >= 1: ThreadData.set_timer(parts[0], parts[1] if len(parts)==2 else None)
    else: print(f"{Fore.RED}Usage: timer <seconds> <message>{Style.RESET_ALL}")

@register_command("math", aliases=["eq", "eval"],help_text="math <expression> - Evaluates mathematical expressions safely (e.g., math 2 + sqrt(16)).")
def c_math(arg): MathFunc.evaluate(arg) if arg else print(f"{Fore.RED}Usage: math <expression>{Style.RESET_ALL}")

@register_command("random", help_text="random [max] OR random [min] [max] - Generates a random integer.")
def c_rand(arg):
    if arg:
        try:
            nums = [int(x) for x in arg.split()]
            MathFunc.rtool(nums[0]) if len(nums) == 1 else MathFunc.rtool(nums[0], nums[1])
        except ValueError: print(f"{Fore.RED}Provide valid integers.{Style.RESET_ALL}")
    else: MathFunc.rtool()

@register_command("mathhelp", aliases=["mhelp"], help_text="mathhelp <attribute> - Displays help details for a specific MathSet function or constant.")
def c_mathhelp(arg): # useless though
    if not arg:
        print(f"{Fore.RED}Usage: mathhelp <attribute>{Style.RESET_ALL}")
        print(f"Available attributes: {Fore.CYAN}{', '.join(mathset.keys())}{Style.RESET_ALL}")
    else: MathFunc.help_attribute(arg)

@register_command("boot", aliases=["reboot"], help_text=f"boot - Reboots {easysaxo.name} safely")
def c_boot(arg):
    from . import main
    SessionManager.save_session(ThreadData.current_user)
    bootcheck()
    main.Core()
    

@register_command("time", aliases=["date"], help_text="time - Displays current system date and time.")
def c_time(arg): hrs()

@register_command("whatsnew", aliases=["news", "upd", "updates", "changes"], help_text="whatsnew - Displays software changelog highlights.")
def c_whatsnew(arg): whats_new()

@register_command("unins", aliases=["uninstall", "selfdel", "sdelete"], help_text="unins - Guider to uninstall the program.")
def b_unins(arg=None):
    from .esmodules.misc import unins_guide
    unins_guide()