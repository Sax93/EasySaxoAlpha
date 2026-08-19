"""EasySaxo Alpha Command Input/Registry.
Full to all GET and base commands/subcommands"""
# NOTE: `commands.py` is strictly for command creation, not meant to support other than command registering.

from colorama import Fore, Style

from .config import GET_REGISTRY, HELP_REGISTRY, easysaxo, register_command, whats_new
from .esmodules.computer import ComputerData, ComputerOper
from .esmodules.dirloct import DirLocation
from .esmodules.heavyholder import SessionManager, ThreadData
from .esmodules.jsonregex import JsonData, RegexData
from .esmodules.lister import MathList
from .esmodules.mathf import MathFunc
from .esmodules.medi import MediaData
from .esmodules.misc import hrs
from .esmodules.telemetry import TelemetryData

ee4 = True

#=================================================
# Command Mappings
#=================================================

# For in-MathSet guide
for math_key, help_str in MathList.MATHSET_HELP.items():
    HELP_REGISTRY[math_key] = help_str

# =========== EASTER EGGS SECTION ============
import random

from .esmodules import easters


def e1(): easters.eas1()

def e2(): easters.eas2()

def e3():
    from .esmodules.lister import EasterList
    print(f"{Fore.LIGHTYELLOW_EX}{random.choice(EasterList.osaka)} :D{Style.RESET_ALL}")

def e4():
    global ee4
    easters.eas4()
    ee4 = False
    return ee4

def e5(): easters.eas5()

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
    possible_devs = ["SXF", "SFX", "Your mom lol"]
    pctg = [98, 1.2, 0.8]
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
    for func in [g_cpu, g_arch, g_os, g_mboard, g_ram, g_gpu, g_disk, g_batt, g_user, g_py, g_proc]: func()
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
        from .esmodules.lister import CommandList
        print(CommandList.CMDlist)
    else:
        target = arg.lower().strip()
        if target in HELP_REGISTRY:
            print(f"\n{Fore.GREEN}=== Usage for '{target}' ==={Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{HELP_REGISTRY[target]}{Style.RESET_ALL}")
        elif target in GET_REGISTRY and target in HELP_REGISTRY:
            print(f"\n{Fore.GREEN}=== Usage for 'get {target}' ==={Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{HELP_REGISTRY[target]}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}No usage details found for '{arg}'. Type 'help' for options.{Style.RESET_ALL}")

@register_command("exit", aliases=["quit", "kill"], help_text="exit - Save session state and exit app.")
def c_exit(arg):
    import sys
    SessionManager.save_session(ThreadData.current_user)
    sys.exit(0)

@register_command("clear", aliases=["clr", "clrscr"], help_text="clear - Clears the terminal screen.")
def c_clear(arg):
    from .config import clr
    clr()

@register_command("save", help_text="save [filepath.json] - Saves the current session state along with its storable data.")
def c_save(arg): SessionManager.save_session(ThreadData.current_user, arg)

@register_command("load", help_text="load <filepath.json> - Loads session state and variables from a file.")
def c_load(arg):
    if arg:
        session_info = SessionManager.load_session(arg)
        if isinstance(session_info, dict):
            ThreadData.current_user = session_info.get("user_name", "User")
            ThreadData.current_pswd = session_info.get("password")
            ThreadData.path_display = session_info.get("pathdisplay", False)
            ThreadData.target_mode = session_info.get("target_mode", "auto")
        else:
            ThreadData.current_user = session_info
            print(f"{Fore.RED}JSON file not found or specified.{Style.RESET_ALL}")
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
    if not arg: print(f"{Fore.RED}Missing argument for 'get'. Type 'help' for options.{Style.RESET_ALL}")
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

@register_command("cd", aliases=["chdir"], help_text="cd <path> - Changes current working directory.")
def c_cd(arg): DirLocation.cd(arg)

@register_command("filelst", aliases=["ls", "dir", "lsdir", "dirls", "listdir", "dirlist"], help_text="filelst <path> - Lists files and subdirectories in the specified or current directory.")
def c_filelst(arg): DirLocation.ls(arg)

@register_command("tree", aliases=["filetree", "dirtree"], help_text="tree <dir> - Renders directory as a tree.")
def c_treedir(arg): DirLocation.filetree(arg)

@register_command("fileopn", aliases=["openf", "opn"], help_text="fileopn <filepath> - Opens a file with the default system application.")
def c_fileopn(arg): DirLocation.fileopn(arg) if arg else print(f"{Fore.RED}Missing filepath.{Style.RESET_ALL}")

@register_command("filecls", aliases=["closef", "clsf"], help_text="filecls <process_name> - Terminates process(es) matching the given name.")
def c_filecls(arg): DirLocation.filecls(arg) if arg else print(f"{Fore.RED}Missing process name.{Style.RESET_ALL}")

@register_command("filecrt", aliases=["createf", "touch"], help_text="filecrt <filepath> - Creates an empty file at the designated location.")
def c_filecrt(arg):
    import os
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

@register_command("filewrt", aliases=["writef"], help_text="filewrt <filepath> [content] - Overwrites file. Omit content to start interactive multiline editor.")
def c_filewrt(arg):
    from .esmodules.lister import FileList
    parts = arg.split(maxsplit=1) if arg else []
    if not parts:
        print(f"{Fore.RED}Usage: filewrt <filepath> [content]{Style.RESET_ALL}")
        return

    filepath = parts[0]
    content = parts[1] if len(parts) == 2 else None

    target_file = filepath.removesuffix(".py")
    if filepath in FileList._allow or target_file in FileList._allow:
        print(f"{Fore.LIGHTRED_EX}Hey, hey, no touching there.{Style.RESET_ALL}")
        return

    DirLocation.filewrt(filepath, content)

@register_command("filesort", aliases=["sortf"], help_text="filesort <source_dir> <ext> <dest_dir> - Moves files matching extension from source to destination directory.")
def c_filesort(arg):
    parts = arg.split() if arg else []
    if len(parts) < 3:
        print(f"{Fore.RED}Usage: filesort <source_dir> <file_ext> <dest_dir>{Style.RESET_ALL}")
        return
    source_dir = parts[0]
    file_ext = parts[1]
    dest_dir = parts[2]
    DirLocation.filesort(source_dir, file_ext, dest_dir)

@register_command("filesz", aliases=["sizef", "sizeof"], help_text="filesz <file> - Shows size of a file.")
def c_filesz(arg): DirLocation.filesz(arg) if arg else print(f"{Fore.RED}Missing filepath.{Style.RESET_ALL}")

@register_command("jsonrd", help_text="jsonrd <filepath> - Parses and pretty-prints JSON file contents.")
def c_jsonrd(arg): JsonData.jsonrd(arg) if arg else print(f"{Fore.RED}Missing filepath.{Style.RESET_ALL}")

@register_command("regex", help_text="regex <pattern> <text> [-f] [-a] - Evaluates regex pattern (-f for file, -a for case-insensitive).")
def c_regex(arg):
    parts = arg.split() if arg else []
    if not parts:
        print(f"{Fore.RED}Usage: regex <pattern> <text/file> [-f] [-a]{Style.RESET_ALL}")
        return

    # farse flags
    flags = [p for p in parts if p.startswith("-")]
    has_file = "-f" in flags
    has_ignorecase = "-a" in flags

    # filter out flags from parts to get pattern and text/file
    non_flags = [p for p in parts if not p.startswith("-")]

    if len(non_flags) < 2:
        print(f"{Fore.RED}Usage: regex <pattern> <text/file> [-f] [-a]{Style.RESET_ALL}")
        return

    pattern = non_flags[0]
    target = non_flags[1]

    if has_file:
        textfile_path = DirLocation._resolve_path(target)
        RegexData.match_file(pattern, textfile_path, ignore_case=has_ignorecase)
    else:
        text = " ".join(non_flags[1:])  # rejoin remaining parts in case text contains spaces
        RegexData.match_pattern(pattern, text, ignore_case=has_ignorecase)

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
    if not arg:
        print(f"{Fore.RED}Usage: render <imgpath> [colnum]{Style.RESET_ALL}")
        return
    parts = arg.split()
    target = parts[0]
    colnum = parts[1] if len(parts) > 1 else "80"
    
    if MediaData.render_preset(target.lower()): return
        
    MediaData.render(target, colnum)

@register_command("banner", aliases=["tart", "amply"], help_text="banner <text> - Reprints the input text, bigger.")
def c_banner(arg):
    if not arg:
        MediaData.txt2rt('Missing text!')
        return
    parts = arg.split()

    if parts[0].lower() in ["render", "-r"]:
        MediaData.renderbanner(parts[1].lower())
        return

    MediaData.txt2rt(arg)

@register_command("set", help_text="set <varfeature> <val> - Updates session settings or math variables.")
def c_set(arg): # prob greatest cmd
    from .esmodules.heavyholder import set_stat
    set_stat(arg)

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
        print(f"Available attributes: {Fore.CYAN}{', '.join(MathList.mathset.keys())}{Style.RESET_ALL}")
    else: MathFunc.help_attribute(arg)

@register_command("time", aliases=["date"], help_text="time - Displays current system date and time.")
def c_time(arg): hrs()

@register_command("changelog", aliases=["news", "upd", "updates", "whatsnew"], help_text="changelog - Displays software changelog highlights.")
def c_whatsnew(arg): whats_new()

@register_command("unins", aliases=["uninstall", "selfdel", "sdelete"], help_text="unins - Guider to uninstall the program.")
def b_unins(arg=None):
    from .esmodules.misc import unins_guide
    unins_guide()

@register_command("shutdown", aliases=["turnoff", "shut"], help_text="shutdown [time]- Turns the computer off after a defined time.")
def s_shutdown(arg): ComputerOper.shut_down(arg)

@register_command("requirements", aliases=["reqs", "sysreqs"], help_text="requirements - Shows the app requirements.")
def s_requirements(arg): ComputerOper.requirements()