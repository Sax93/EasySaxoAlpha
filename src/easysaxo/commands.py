"""EasySaxo Alpha Command Input/Registry. Full to all GET and base commands/subcommands"""

import os

from rich import print

from .config import GET_REGISTRY, HELP_REGISTRY, easysaxo, register_command, whats_new
from .esmodules.computer import ComputerData, ComputerOper
from .esmodules.dirloct import DirLocation
from .esmodules.heavyholder import SessionManager, ThreadData
from .esmodules.jsonregex import JsonData, RegexData
from .esmodules.lister import MathList
from .esmodules.mathf import MathFunc
from .esmodules.medi import MediaData
from .esmodules.misc import hrs

ee4 = True

# Help utils
def _telemetry_data():
    from .esmodules.telemetry import TelemetryData
    return TelemetryData

def _telemetry_operations():
    from .esmodules.telemetry import TelemetryOperations
    return TelemetryOperations

def _resolve_target_args(arg: str, *, for_creation: bool = False) -> str:
    """
    Parses dynamic path targets and flags.
    Handles usages:
      - `command -<desk file.txt`
      - `command file.txt -<desk`
      - `command path/to/file.txt`
    """
    if not arg: return ""

    parts = arg.split()
    
    # handle single flag/alias usage with extra tokens (`-<desk file name.txt`)
    if parts[0].lower() in DirLocation.FLAGS:
        dest_dir = DirLocation._resolve_path(parts[0])
        filename = " ".join(parts[1:])
        return os.path.join(dest_dir, filename) if filename else dest_dir

    # handle path with flag at the end (`file name.txt -<desk`)
    if parts[-1].lower() in DirLocation.FLAGS:
        dest_dir = DirLocation._resolve_path(parts[-1])
        filename = " ".join(parts[:-1])
        return os.path.join(dest_dir, filename) if filename else dest_dir

    # otherwise treat the entire argument string as a single path with spaces
    if for_creation: return arg.strip()

    return DirLocation._resolve_path(arg.strip())

for math_key, help_str in MathList.MATHSET_HELP.items(): HELP_REGISTRY[math_key] = help_str

# GET attrs

@register_command("aliases", aliases=["alias", "cmdalias"], registry=GET_REGISTRY, help_text="get aliases - Displays command aliases.")
def g_aliases(): ComputerData.getaliases()

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
def g_net(): _telemetry_data().getnet()

@register_command("upt", aliases=["uptime"], registry=GET_REGISTRY, help_text="get upt - Displays system uptime.")
def g_upt(): _telemetry_data().getupt()

@register_command("ip", aliases=["ipaddress"], registry=GET_REGISTRY, help_text="get ip - Displays local network IP addresses.")
def g_ip(): _telemetry_data().getip()

@register_command("mac", aliases=["macaddress"], registry=GET_REGISTRY, help_text="get mac - Displays primary MAC address.")
def g_mac(): _telemetry_data().getmac()

@register_command("publicip", aliases=["pipaddress", "publicipaddress"], registry=GET_REGISTRY, help_text="get publicip - Displays public IP address.")
def g_pubip(): _telemetry_data().getpublicip()

@register_command("netstats", aliases=["adastats", "adapter", "netadapter"], registry=GET_REGISTRY, help_text="get netstats - Displays network adapter statuses.")
def g_netstat(): _telemetry_data().getnetstats()

@register_command("connections", registry=GET_REGISTRY, help_text="get connections - Displays active network connections.")
def g_conn(): _telemetry_data().getconnections()

@register_command("speedtest", registry=GET_REGISTRY, help_text="get speedtest - Performs network speed test.")
def g_speed(): _telemetry_data().speedtest_network()

@register_command("threads", registry=GET_REGISTRY, help_text="get threads - Displays active background threads.")
def g_th(): ThreadData.getthreads()

@register_command("mathset", registry=GET_REGISTRY, help_text="get mathset - Displays available math functions/constants.")
def g_mset(): MathFunc.getmath()

@register_command("vars", aliases=["variables"], registry=GET_REGISTRY, help_text="get vars - Lists user math variables.")
def g_vars(): MathFunc.list_vars()

@register_command("appname", registry=GET_REGISTRY, help_text="get appname - Displays app name.")
def g_appn(): print(f"App name: [cyan]{easysaxo.name}[/cyan]")

@register_command("appver", aliases=["version"], registry=GET_REGISTRY, help_text="get appver - Displays app version.")
def g_appv():
    from .config import app_databuild
    build = app_databuild()
    print(f"App version: [cyan]{easysaxo.ver} (build-{build})[/cyan]")

@register_command("appdev", aliases=["developer", "dev"], registry=GET_REGISTRY)
def g_appd():
    print(f"App developer: [cyan]{easysaxo.dev}[/cyan]")

@register_command("_app", aliases=["appinfo"], registry=GET_REGISTRY, help_text="get app - Displays general app details.")
def g_app(): print(f"App: [cyan]{easysaxo.name} {easysaxo.ver}[/cyan] by [cyan]{easysaxo.dev}[/cyan]")

@register_command("username", aliases=["name"], registry=GET_REGISTRY, help_text="get username - Displays registered user name (in app).")
def g_uname(): print(f"Username: [cyan]{ThreadData.current_user}[/cyan].")

@register_command("attr", aliases=["attribute", "all"], registry=GET_REGISTRY, help_text="get attr - Fetches all telemetry and system specs.")
def g_all():
    try:
        print("[blue]== COMPUTER DATA ==[/blue]")
        for func in [g_cpu, g_arch, g_os,
                     g_mboard, g_ram, g_gpu,
                     g_disk, g_batt, g_user,
                     g_py, g_proc]: func()
        print("\n[blue]== TELEMETRY DATA ==[/blue]")
        for func in [g_net, g_upt, g_ip,
                     g_mac, g_pubip, g_netstat]: func()
        print("\n[blue]== THREADING/MATH DATA ==[/blue]\n")
        for func in [g_th, g_mset, g_vars]: func()
        print("\n[blue]== MISC DATA ==[/blue]\n")
        for func in [g_uname, g_appn, g_appv, g_appd]: func()
    except KeyboardInterrupt: easysaxo.k_log("11")

# COMMANDS

@register_command("help", aliases=["?", "-h"], help_text="help [command] - Shows command list or syntax details for a target command.")
def c_help(arg):
    if not arg:
        from .esmodules.lister import CommandList
        print(CommandList.CMDlist)
        return

    target = arg.lower().strip()

    if target in ["alias", "alt"]:
        from .esmodules.lister import CommandList
        print(CommandList.ALIASList)
        return

    if target in GET_REGISTRY and target in HELP_REGISTRY:
        print(f"\n[green]=== Usage for 'get {target}' ===[/green]")
        print(f"[yellow]{HELP_REGISTRY[target]}[/yellow]")

    elif target in HELP_REGISTRY:
        print(f"\n[green]=== Usage for '{target}' ===[/green]")
        print(f"[yellow]{HELP_REGISTRY[target]}[/yellow]")

    else:
        easysaxo.k_log("m3")
        print(f"[red]No usage details found for '{arg}'. Type 'help' for options.[/red]")

@register_command("exit", aliases=["quit", "kill"], help_text="exit - Save session state and exit app.")
def c_exit(arg):
    import sys
    SessionManager.save_session(ThreadData.current_user)
    easysaxo.k_log("a0")
    sys.exit(0)

@register_command("clear", aliases=["cls", "clrscr"], help_text="clear - Clears the terminal screen.")
def c_clear(arg):
    from .config import clr
    clr()

@register_command("save", help_text="save [filepath.json] - Saves the current session state along with its storable data.")
def c_save(arg):
    if arg == "translations.json":
        easysaxo.k_log("1")
        print("[red]Saving in `translations.json` is not allowed.[/red]")
        return

    target_path = _resolve_target_args(arg) if arg else None

    SessionManager.save_session(ThreadData.current_user, target_path)

@register_command("load", help_text="load <filepath.json> - Loads session state and variables from a file.")
def c_load(arg):
    if arg:
        target_path = _resolve_target_args(arg)
        session_info = SessionManager.load_session(target_path)
        if isinstance(session_info, dict):
            ThreadData.current_user = session_info.get("user_name", "User")
            ThreadData.current_pswd = session_info.get("password")
            ThreadData.path_display = session_info.get("pathdisplay", False)
            ThreadData.target_mode = session_info.get("target_mode", "auto")
        else:
            ThreadData.current_user = session_info
            easysaxo.k_log("5")
            print("[red]JSON file not found or specified.[/red]")
        return
    easysaxo.k_log("2")
    print("[red]Usage: load <filepath.json>[/red]")

@register_command("delvar", help_text="delvar <var_name> - Deletes a user-defined math variable.")
def c_delvar(arg):
    if not arg:
        easysaxo.k_log("2")
        print("[red]Usage: delvar <var_name>[/red]")
        return
    MathFunc.del_var(arg)
    SessionManager.save_session(ThreadData.current_user)       

@register_command("get", help_text="get <attribute|variable> - Fetches system metrics, variables, or specifications.")
def c_get(arg):
    if not arg:
        easysaxo.k_log("2")
        print("[red]Missing argument for 'get'. Type 'help' for options.[/red]")
    elif arg in GET_REGISTRY: GET_REGISTRY[arg]()
    else: MathFunc.getvar(arg)

@register_command("check", aliases=["allowance", "checkf", "filechk"], help_text="check - Checks if all main files exist and are available.")
def c_check(arg): DirLocation.allowance()

@register_command("dircrt", aliases=(["dcreate", "mkdir"]), help_text="dircrt <dirname> [destination_dir] - Creates a directory.")
def c_dircrt(arg):
    if not arg:
        easysaxo.k_log("2")
        print("[red]Missing directory name.[/red]")
        return

    DirLocation.dircrt(_resolve_target_args(arg, for_creation=True))

@register_command("dirdel", aliases=(["ddelete", "rm-r", "rmdir"]), help_text="dirdel <dirname> [destination_dir] - Deletes a directory.")
def c_dirdel(arg): 
    if not arg:
        easysaxo.k_log("2")
        print("[red]Missing directory path.[/red]")
        return
    DirLocation.dirdel(_resolve_target_args(arg))

@register_command("cd", aliases=["chdir"], help_text="cd [<path>] - Changes current working directory or displays current.")
def c_cd(arg): DirLocation.cd(arg)

@register_command("filelst", aliases=["ls", "dir", "lsdir", "dirls", "listdir", "dirlist"], help_text="filelst [path] - Lists files and subdirectories in the specified or current directory.")
def c_filelst(arg):
    target = _resolve_target_args(arg) if arg else ""
    DirLocation.ls(target)

@register_command("tree", aliases=["filetree", "dirtree"], help_text="tree [dir] [depth]- Renders directory as a tree.")
def c_treedir(arg):
    if not arg:
        target = ""
        DirLocation.filetree(target)
        return

    parts = arg.split(maxsplit=1)

    target = _resolve_target_args(parts[0]) if arg else ""
    if len(parts) > 1 and parts[1].isdigit(): max_depth = int(parts[1])
    elif len(parts) > 1 and parts[1].lower() in ["max", "all"]: max_depth = 1000
    else: max_depth = 4

    DirLocation.filetree(target, max_depth)

@register_command("fileopn", aliases=["openf", "opn"], help_text="fileopn <filepath> [destination_dir] - Opens a file with the default system application.")
def c_fileopn(arg):
    if not arg:
        easysaxo.k_log("2")
        print("[red]Missing filepath.[/red]")
        return
    DirLocation.fileopn(_resolve_target_args(arg))

@register_command("filecls", aliases=["closef", "clsf", "killproc"], help_text="filecls <process_name> - Terminates process(es) matching the given name.")
def c_filecls(arg):
    if not arg:
        easysaxo.k_log("2")
        print("[red]Missing file argument.[/red]")
        return
    DirLocation.filecls(arg)

@register_command("filecrt", aliases=["createf", "touch"], help_text="filecrt <filename|path> [destination_dir] - Creates an empty file in current or designated directory.")
def c_filecrt(arg):
    if not arg:
        easysaxo.k_log("2")
        print("[red]Missing file argument.[/red]")
        return

    DirLocation.filecrt(_resolve_target_args(arg, for_creation=True))

@register_command("filerd", aliases=["readf", "cat"], help_text="filerd <filepath> [destination_dir] - Reads and prints text content from a target file.")
def c_filerd(arg):
    if not arg:
        easysaxo.k_log("2")
        print("[red]Missing filepath.[/red]")
        return
    DirLocation.filerd(_resolve_target_args(arg))

@register_command("filedel", aliases=["deletef", "rm"], help_text="filedel <filepath> [destination_dir] - Permanently removes a file from disk.")
def c_filedel(arg):
    if not arg:
        easysaxo.k_log("2")
        print("[red]Missing filepath.[/red]")
        return
    DirLocation.filedel(_resolve_target_args(arg))

@register_command("filewrt", aliases=["writef"], help_text="filewrt <filepath> [content] - Overwrites file. Omit content to use interactive multiline editor.")
def c_filewrt(arg):
    from .esmodules.lister import FileList
    if not arg:
        easysaxo.k_log("2")
        print("[red]Usage: filewrt <filepath> [content][/red]")
        return

    parts = arg.split(maxsplit=1)
    target_arg = parts[0]
    content = parts[1] if len(parts) == 2 else None

    filepath = _resolve_target_args(target_arg)
    target_file = filepath.removesuffix(".py")

    if not os.path.exists(filepath):
        easysaxo.k_log("5")
        print(f"[red]File {filepath} does not exist.[/red]")
        return

    if filepath in FileList._allow or target_file in FileList._allow:
        easysaxo.k_log("4")
        print("[red]Hey, hey, no touching there.[/red]")
        return

    DirLocation.filewrt(filepath, content)

@register_command("filesort", aliases=["sortf"], help_text="filesort <source_dir> <ext> <dest_dir> - Moves files matching extension from source to destination directory.")
def c_filesort(arg):
    parts = arg.split() if arg else []
    if len(parts) < 3:
        easysaxo.k_log("1")
        print("[red]Usage: filesort <source_dir> <file_ext> <dest_dir>[/red]")
        return
    source_dir = _resolve_target_args(parts[0])
    file_ext = parts[1]
    dest_dir = _resolve_target_args(parts[2])
    DirLocation.filesort(source_dir, file_ext, dest_dir)

@register_command("filesz", aliases=["sizef", "sizeof"], help_text="filesz <file> - Shows size of a file.")
def c_filesz(arg): 
    if not arg:
        easysaxo.k_log("2")
        print("[red]Missing filepath.[/red]")
        return
    DirLocation.filesz(_resolve_target_args(arg))

@register_command("dirsz", aliases=["dsize", "dsizeof"], help_text="dirsz <dir> - Shows size of a directory.")
def c_dirsz(arg):
    if not arg: arg = "."
    DirLocation.dirsz(_resolve_target_args(arg))

@register_command("move", aliases=["mv", "filemv", "movef"], help_text="move [file] [dir] OR move (file1, file2) [dir] - Move file(s) to a directory.")
def c_move(arg):
    if not arg:
        easysaxo.k_log("2")
        print("[red]Usage: move [file] [dir] OR move (file1, file2) [dir][/red]")
        return
    DirLocation.filemove(arg)

@register_command("jsonrd", help_text="jsonrd <filepath> - Parses and pretty-prints JSON file contents.")
def c_jsonrd(arg): 
    if not arg:
        easysaxo.k_log("2")
        print("[red]Missing filepath.[/red]")
        return
    JsonData.jsonrd(_resolve_target_args(arg))

@register_command("regex", help_text="regex <pattern> <text> [-f] [-a] - Evaluates regex pattern (-f for file, -a for case-insensitive).")
def c_regex(arg):
    parts = arg.split() if arg else []
    if not parts:
        easysaxo.k_log("2")
        print("[red]Usage: regex <pattern> <text/file> [-f] [-a][/red]")
        return

    flags = [p for p in parts if p.startswith("-")]
    has_file = "-f" in flags
    has_ignorecase = "-a" in flags

    non_flags = [p for p in parts if not p.startswith("-")]

    if len(non_flags) < 2:
        easysaxo.k_log("2")
        print("[red]Usage: regex <pattern> <text/file> [-f] [-a][/red]")
        return

    pattern = non_flags[0]

    if has_file:
        textfile_path = _resolve_target_args(" ".join(non_flags[1:]))
        RegexData.match_file(pattern, textfile_path, ignore_case=has_ignorecase)
    else:
        text = " ".join(non_flags[1:])
        RegexData.match_pattern(pattern, text, ignore_case=has_ignorecase)

@register_command("playaudio", aliases=["playa"], help_text="playaudio <filepath> [destination_dir] - Plays an audio file asynchronously.")
def c_playaudio(arg): 
    if not arg:
        easysaxo.k_log("2")
        print("[red]Missing filepath.[/red]")
        return
    MediaData.playaudio(_resolve_target_args(arg))

@register_command("stopaudio", aliases=["stopa"], help_text="stopaudio - Stops currently playing audio playback.")
def c_stopaudio(arg): MediaData.stopaudio()

@register_command("pkm", aliases=["pianomode", "pmode"], help_text="pkm - Enters two-octave piano mode.")
def c_pkm(arg):
    from .esmodules.mamidi import run_piano
    run_piano()

@register_command("render", aliases=["asciiart", "art"], help_text="render <imagepath> [columnnum] - Renders an image in ASCII.")
def c_render(arg):
    if not arg:
        easysaxo.k_log("2")
        print("[red]Usage: render <imgpath> [colnum][/red]")
        return
    parts = arg.split()
    target_arg = parts[0]
    colnum = parts[1] if len(parts) > 1 else "80"
    
    if MediaData.render_preset(target_arg.lower()): return
        
    target_path = _resolve_target_args(target_arg)
    MediaData.render(target_path, colnum)

@register_command("banner", aliases=["tart", "amply"], help_text="banner <text> - Reprints the input text, bigger.")
def c_banner(arg):
    if not arg:
        print("[red]Missing text![/red]")
        return
    parts = arg.split()

    if parts[0].lower() in ["render", "-r"]:
        MediaData.renderbanner(parts[1].lower())
        return

    MediaData.txt2rt(arg)

@register_command("set", help_text="set <varfeature> <val> - Updates session settings or math variables.")
def c_set(arg):
    from .esmodules.heavyholder import set_stat
    set_stat(arg)

@register_command("reset", help_text="reset <name/password> - Changes user data back to default.")
def c_reset(arg):
    if not arg: 
        easysaxo.k_log("2")
        print("[red]Usage: reset <name/password>[/red]")
        return
    parts = arg.strip().split()

    if parts[0].lower() in ["name", "username"] and len(parts) == 1:
        ThreadData.current_user = "User"
        print("[green]User name set to User[/green]")
        SessionManager.save_session(ThreadData.current_user)
    elif parts[0].lower() in ["password", "pswd", "key"] and len(parts) == 1:
        ThreadData.current_pswd = None
        print("[green]Password cleared successfully.[/green]")
        SessionManager.save_session(ThreadData.current_user)
    elif parts[0].lower() in ["all", "user"] and len(parts) == 1:
        ThreadData.current_user = "User"
        ThreadData.current_pswd = None
        print("[green]User values resetted.[/green]")
        SessionManager.save_session(ThreadData.current_user)
    else:
        easysaxo.k_log("1")
        print("[red]Usage: reset <name/password>[/red]")

@register_command("timer", help_text="timer <seconds> [message] - Sets a non-blocking background countdown timer alert.")
def c_timer(arg):
    parts = arg.split(maxsplit=1) if arg else []
    if not parts:
        easysaxo.k_log("2")
        print("[red]Usage: timer <seconds> <message>[/red]")
        return
    elif parts[0].startswith("-"):
        easysaxo.k_log("6")
        print("[red]Seconds cannot be negative.[/red]")
        return

    ThreadData.set_timer(parts[0], parts[1] if len(parts) == 2 else None)

@register_command("math", aliases=["eq", "eval"], help_text="math <expression> - Evaluates mathematical expressions safely (e.g., math 2 + sqrt(16)).")
def c_math(arg): 
    if not arg:
        easysaxo.k_log("2")
        print("[red]Usage: math <expression>[/red]")
        return

    MathFunc.evaluate(arg)

@register_command("random", help_text="random [max] OR random [min] [max] - Generates a random integer.")
def c_rand(arg):
    if not arg:
        MathFunc.rtool()
        return

    try:
        nums = [int(x) for x in arg.split()]
        MathFunc.rtool(nums[0]) if len(nums) == 1 else MathFunc.rtool(nums[0], nums[1])
    except ValueError:
        easysaxo.k_log("6")
        print("[red]Provide valid integers.[/red]")

@register_command("mathhelp", aliases=["mhelp"], help_text="mathhelp <attribute> - Displays help details for a specific MathSet function or constant.")
def c_mathhelp(arg):
    if not arg:
        print(f"Available attributes: [cyan]{', '.join(MathList.mathset.keys())}[/cyan]")
        return

    MathFunc.help_attribute(arg)

@register_command("time", aliases=["date"], help_text="time - Displays current system date and time.")
def c_time(arg): hrs()

@register_command("changelog", aliases=["news", "upd", "updates", "whatsnew"], help_text="changelog - Displays software changelog highlights.")
def c_whatsnew(arg): whats_new()

@register_command("unzip", aliases=["extract", "uzip"], help_text="unzip <zip_path> [destination_folder] - Extracts a zip file to a specified or default folder.")
def c_unzip(arg):
    if not arg:
        easysaxo.k_log("2")
        print("[red]Usage: unzip <zip_path> [destination_folder][/red]")
        return

    parts = arg.split(maxsplit=1)
    zip_path = _resolve_target_args(parts[0])
    dest = _resolve_target_args(parts[1]) if len(parts) > 1 else None
    DirLocation.unzip(zip_path, dest)

@register_command("app", aliases=[f"{easysaxo.name.lower()}"], help_text="app [command] - Allows app manipulation.")
def b_app(arg):
    try:
        if not arg:
            g_app()
            return

        from .esmodules.misc import AppOper as Ao

        parts = arg.split()

        if parts[0] in ["unins", "uninstall"] and len(parts) == 1: Ao.unins_guide()
        elif parts[0] in ["reset", "restart"] and len(parts) == 1: Ao.restart_app()
        elif parts[0] == "update" and len(parts) == 1: Ao.handle_update()
        elif parts[0] == "log":
            if not parts[1]:
                print("[cyan]App logger is active.[/cyan]"
                      if ThreadData.log_muter else
                      "[cyan]App logger is turned off.[/cyan]")
                
            elif parts[1] == "mute" and len(parts) == 2:
                if ThreadData.log_muter:
                    print("[yellow]App logger already muted.[/yellow]")
                    return
                ThreadData.log_muter = True
                easysaxo.mute = ThreadData.log_muter
                SessionManager.save_session(ThreadData.current_user)
                print("[cyan]App logger muted.[/cyan]")

            elif parts[1] == "unmute" and len(parts) == 2:
                if not ThreadData.log_muter:
                    easysaxo.k_log("a1")
                    print("[yellow]App logger already unmuted.[/yellow]")
                    return
                ThreadData.log_muter = False
                easysaxo.mute = ThreadData.log_muter
                SessionManager.save_session(ThreadData.current_user)
                print("[cyan]App logger unmuted.[/cyan]")

            elif parts[1] == "codes" and len(parts) == 2:
                from .esmodules.lister import CommandList
                easysaxo.disclaim(CommandList.LOGlist)

            else:
                easysaxo.k_log("1")
                print("[red]Unknown or malformed subcommand.[/red]")

        elif parts[0] == "state" and len(parts) == 1: easysaxo.state()
        else:
            easysaxo.k_log("1")
            print("[red]Unknown or malformed subcommand.[/red]")
    except KeyboardInterrupt: easysaxo.k_log("11")
        
@register_command("shutdown", aliases=["turnoff", "shut"], help_text="shutdown [time/cancel] - Turns the computer off after a defined time, or aborts a shutdown.")
def s_shutdown(arg): ComputerOper.shut_down(arg)

@register_command("tempflush", aliases=["tmpclr", "tmpf"], help_text="tempflush - Clears the Temp directory in the system.")
def s_tempflush(arg): ComputerOper.clean_temp()

@register_command("restart", help_text="restart [time] - Restarts the computer after a defined time")
def s_restart(arg): ComputerOper.restart(arg)

@register_command("sleep", aliases=["suspend", "hiber"], help_text="sleep - Suspends the computer.")
def s_sleep(arg): ComputerOper.suspend()

@register_command("lock", aliases=["scrlock", "lockscreen"], help_text="lock - Locks the user session.")
def s_scrlock(arg): ComputerOper.lock_screen()

@register_command("requirements", aliases=["reqs", "sysreqs"], help_text="requirements - Shows the app requirements.")
def s_requirements(arg): ComputerOper.requirements()

@register_command("web", aliases=["request", "rq"], help_text="web <url> [method] [-d [filename]] - Sends a request or downloads files (supports GitHub links).")
def t_web(arg):
    if not arg:
        easysaxo.k_log("2")
        print("[red]Usage: web <url> [method] [-d [output_filename]][/red]")
        return
    
    parts = arg.split()
    raw_url = parts[0]
    method = "GET"
    download_path = None
    is_download = False

    if "-d" in parts:
        is_download = True
        download_idx = parts.index("-d")
        
        if download_idx + 1 < len(parts) and not parts[download_idx + 1].startswith("-"):
            download_path = _resolve_target_args(parts[download_idx + 1])
            parts.pop(download_idx + 1)
        
        parts.pop(download_idx)

    telemetry_operations = _telemetry_operations()
    target_url, suggested_filename = telemetry_operations.resolve_github_url(raw_url)

    if is_download:
        filename = download_path or suggested_filename
        download_dir = DirLocation._resolve_path("downloads")
        os.makedirs(download_dir, exist_ok=True)
        download_path = os.path.join(download_dir, filename)

    if len(parts) > 1 and not parts[1].startswith("-"): method = parts[1]
    telemetry_operations.w_request(url=target_url, method=method, download_path=download_path)

@register_command("dnsflush", aliases=["dnsf"], help_text="dnsflush - Flushes the system DNS resolver cache.")
def t_dnsflush(arg): _telemetry_operations().flush_dns()