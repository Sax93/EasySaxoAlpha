"""List, tuple and dict holder for EasySaxo"""

from rich import print  # noqa: F401

from ..config import easysaxo

# command list

class CommandList:
    """Command-related global lister for information display."""
    
    CMDlist = f"""
[cyan]|======= COMMAND LIST: =======|[/cyan]

  [cyan]help[/cyan]          : Shows this [cyan]Command List[/cyan].
  [cyan]changelog[/cyan]     : Shows the latest [cyan]app updates[/cyan].
  [cyan]requirements[/cyan]  : Shows minimum and recommended [cyan]device requirements[/cyan].
  [cyan]clear[/cyan]         : Clears the [cyan]terminal[/cyan] screen.
  [cyan]get[/cyan]           : Gets information of a [cyan]variable[/cyan] or an [cyan]attribute[/cyan].
  [cyan]set[/cyan]           : Sets storable information like [cyan]user name[/cyan] and [cyan]variables[/cyan].
  [cyan]reset[/cyan]         : Resets [cyan]user data[/cyan] (either [cyan]user name[/cyan] or [cyan]password[/cyan]).

  [green]save[/green]          : Creates/rewrites a [green]JSON file[/green] with [green]user[/green] data.
  [green]load[/green]          : Loads a [green]JSON file[/green] with [green]user[/green] data.
  [green]jsonrd[/green]        : Reads a [green]JSON file[/green].
  [green]regex[/green]         : Looks for [green]patterns[/green] in a text or textfile.

  [blue]math[/blue]          : Allows mathematical equations.
  [blue]mathhelp[/blue]      : Displays information about math-related functions.
  [blue]random[/blue]        : Shows a random [blue]number[/blue].
  [blue]time[/blue]          : Displays [blue]hour[/blue] and [blue]date[/blue].
  [blue]timer[/blue]         : Sets a timer in [blue]seconds[/blue] before displaying a message.
  [blue]delvar[/blue]        : Deletes a specified [blue]variable[/blue].

  [red]cd[/red]            : Shows current [red]path location[/red] and allows navigation.
  [red]check[/red]         : Checks if required [red]script files[/red] exist.
  [red]filelst[/red]       : Lists [red]files[/red] and [red]folders[/red] in a directory.
  [red]tree[/red]          : Renders [red]directory[/red] as a tree.
  [red]filecrt[/red]       : Creates a [red]file[/red] with specified extension.
  [red]filerd[/red]        : Reads and displays the content of a [red]file[/red].
  [red]filedel[/red]       : Deletes a [red]file[/red].
  [red]filewrt[/red]       : Writes content in a [red]file[/red].
  [red]move[/red]          : Moves [red]files[/red] to a directory.
  [red]fileopn[/red]       : Opens a [red]file[/red].
  [red]filecls[/red]       : Closes a [red]file[/red].
  [red]filesort[/red]      : Sorts and dumps [red]files[/red] in a directory by extension.
  [red]filesz[/red]        : Gets and shows the size of a [red]file[/red].
  [red]dirsz[/red]         : Gets and shows the size of a [red]directory[/red].
  [red]unzip[/red]         : Gets and extracts the content of a [red]ZIP file[/red].

  [magenta]playaudio[/magenta]     : Plays an [magenta]audio file[/magenta] (specify route).
  [magenta]stopaudio[/magenta]     : Stops the current [magenta]audio file[/magenta].
  [magenta]render[/magenta]        : Renders and draws a specified [magenta]image file[/magenta].
  [magenta]banner[/magenta]        : Renders and prints inputted [magenta]text[/magenta].
  [magenta]pkm[/magenta]           : Enters the [magenta]Piano Keyboard Mode[/magenta].

  [blue]web[/blue]           : Sends a [blue]request to an URL[/blue], thus installing files from links if requested.
  [blue]dnsflush[/blue]      : Clears the cache of the [blue]system DNS resolver[/blue].

  [lightblack]shutdown[/lightblack]      : [lightblack]Shuts the system down[/lightblack] or cancels such operation.
  [lightblack]restart[/lightblack]       : [lightblack]Restarts the system[/lightblack].
  [lightblack]sleep[/lightblack]         : [lightblack]Suspends the system[/lightblack].
  [lightblack]lock[/lightblack]          : [lightblack]Lock the user session[/lightblack] immediately.
  [lightblack]tempflush[/lightblack]     : Clears the [lightblack]system /Temp directory[/lightblack].
  [lightblack]app[/lightblack]           : Runs {easysaxo.name} base commands.
  [lightblack]exit[/lightblack]          : Exit {easysaxo.name}.
Remember you can search for command syntax and usage by using [cyan]help <cmd/attr>[/cyan] :)
    """

    ALIASList = f"""
[cyan]|======= ALIASES LIST: =======|[/cyan]

  [cyan]help[/cyan]          : (?), (-h).
  [cyan]changelog[/cyan]     : (news), (upd), (whatsnew), (updates).
  [cyan]requirements[/cyan]  : (reqs), (sysreqs).
  [cyan]clear[/cyan]         : (cls), (clrscr).
  [cyan]get[/cyan]           : No aliases.
  [cyan]set[/cyan]           : No aliases.
  [cyan]reset[/cyan]         : No aliases.

  [green]save[/green]          : No aliases.
  [green]load[/green]          : No aliases.
  [green]jsonrd[/green]        : No aliases.
  [green]regex[/green]         : No aliases.

  [blue]math[/blue]          : (eq), (eval).
  [blue]mathhelp[/blue]      : (mhelp).
  [blue]random[/blue]        : No aliases.
  [blue]time[/blue]          : (date).
  [blue]timer[/blue]         : No aliases.
  [blue]delvar[/blue]        : No aliases.

  [red]cd[/red]            : (chdir).
  [red]check[/red]         : (allowance), (checkf), (filechk).
  [red]filelst[/red]       : (ls), (dir), (lsdir), (dirls), (listdir), (dirlist).
  [red]tree[/red]          : (filetree), (dirtree).
  [red]filecrt[/red]       : (createf), (touch).
  [red]filerd[/red]        : (readf), (cat).
  [red]filedel[/red]       : (rm), (deletef).
  [red]filewrt[/red]       : (writef).
  [red]move[/red]          : (mv), (movef), (filemv).
  [red]fileopn[/red]       : (openf), (opn).
  [red]filecls[/red]       : (closef), (killproc), (clsf).
  [red]filesort[/red]      : (sortf).
  [red]filesz[/red]        : (sizef), (sizeof).
  [red]dirsz[/red]         : (dsize), (dsizeof).
  [red]unzip[/red]         : (extract), (uzip).

  [magenta]playaudio[/magenta]     : (playa).
  [magenta]stopaudio[/magenta]     : (stopa).
  [magenta]render[/magenta]        : (asciiart), (art).
  [magenta]banner[/magenta]        : (tart), (amply).
  [magenta]pkm[/magenta]           : (pianomode), (pmode).

  [blue]web[/blue]           : (request), (rq).
  [blue]dnsflush[/blue]      : (dnsf).

  [lightblack]shutdown[/lightblack]      : (turnoff), (shut).
  [lightblack]restart[/lightblack]       : No aliases.
  [lightblack]sleep[/lightblack]         : (suspend), (hiber).
  [lightblack]lock[/lightblack]          : (scrlock), (lockscreen).
  [lightblack]tempflush[/lightblack]     : (tmpf), (tmpclr).
  [lightblack]app[/lightblack]           : ({easysaxo.name.lower()}).
  [lightblack]exit[/lightblack]          : (quit), (kill).
    """


    FWRTlist = """
[yellow]Commands:[/yellow]
[green]:l[/green] -> List buffer with line numbers
[green]:d <line_num>[/green] -> Delete a line
[green]:i <line_num> <text>[/green] -> Insert text at line number
[green]:c[/green] -> Clear buffer entirely
[green]:w[/green] or [green]:x[/green] or [green]EOF[/green] -> Save & Exit
[green]:q[/green] -> Quit without saving
[green]:lt[/green] -> Lint current.
    """

    LOGlist = """
[cyan]Log code |>[/cyan]
  [lightblack]> No character before number indicates a general error message.[/lightblack]
    [cyan]1[/cyan] ------> Unknown/malformed command.
    [cyan]2[/cyan] ------> No arguments provided.
    [cyan]3[/cyan] ------> Operation failed.
    [cyan]4[/cyan] ------> Permission denied or access error.
    [cyan]5[/cyan] ------> File or directory not found.
    [cyan]6[/cyan] ------> Invalid input or value error.
    [cyan]7[/cyan] ------> Network or connection error.
    [cyan]8[/cyan] ------> Request or API error.
    [cyan]9[/cyan] ------> System command execution failed.
    [cyan]10[/cyan] -----> Unexpected error occurred.
    [cyan]11[/cyan] -----> Operation canceled.

  [lightblack]> 'a' before number indicates an info message.[/lightblack]
    [cyan]a0[/cyan] -----> Exiting app.

  [lightblack]> 'f' before number indicates specific file error.[/lightblack]
    [cyan]f1[/cyan] -----> Path or file is invalid.
    [cyan]f2[/cyan] -----> Path is a file.
    [cyan]f3[/cyan] -----> Path is a directory.
    [cyan]f4[/cyan] -----> Path exists.

  [lightblack]> 'p' before number indicates specific process error.[/lightblack]
    [cyan]p1[/cyan] -----> No such running process / Process does not exist.

  [lightblack]> 'm' before number indicates specific math error[/lightblack]
    [cyan]m1[/cyan] -----> Cannot operate over term.
    [cyan]m2[/cyan] -----> Variable does not exist.
    [cyan]m3[/cyan] -----> Term does not exist.
    """

# file list

class FileList:
    """File verifier list for file viewing and handling."""
    _allow = [  # noqa: RUF012
        "__init__",
        "main",
        "config",
        "commands",
        "esmodules/__init__",
        "esmodules/computer",
        "esmodules/heavyholder",
        "esmodules/telemetry",
        "esmodules/jsonregex",
        "esmodules/mathf",
        "esmodules/medi",
        "esmodules/misc",
        "esmodules/builtinrender",
        "esmodules/lister",
        "esmodules/easters",
        "esmodules/mamidi"
    ]

    _delete = [  # noqa: RUF012
        "config.py", "session.json", "translations.json",
        "main.py", "commands.py"
    ]

    EXTENSION_COLORS = {  # noqa: RUF012
        # scripts
        ".py": "[lightyellow]",
        ".js": "[yellow]",
        ".jar": "[red]", ".jav": "[red]",
        ".html": "[lightred]",
        ".css": "[cyan]",
        ".json": "[lightyellow]",
        ".xml": "[lightgreen]",
        ".c": "[cyan]",
        ".toml": "[blue]",
        ".lua": "[blue]",
        # docs
        ".md": "[cyan]",
        ".txt": "[white] + [dim]",
        ".doc": "[blue]",".docx": "[blue]",
        ".xls": "[green]", ".xlsx": "[green]",
        ".pdf": "[red]",
        ".pptx": "[red]",
        # media
        ".png": "[magenta]",
        ".ico": "[magenta]",
        ".jpg": "[magenta]", ".jpe": "[magenta]",".jfif": "[magenta]", ".jpeg": "[magenta]",
        ".svg": "[magenta]",
        ".webp": "[magenta]",
        ".mp3": "[lightmagenta]",
        ".flac": "[lightmagenta]",
        ".ogg": "[lightmagenta]",
        ".wav": "[lightmagenta]",
        ".mid": "[lightmagenta]",
        ".mp4": "[lightcyan]",
        ".gif": "[lightcyan]",
        # fls
        ".zip": "[lightred]", ".rar": "[lightred]",
        ".exe": "[red]", ".bat": "[red]", ".sh": "[red]",
        ".bak": "[lightyellow]", ".pak": "[lightyellow]",
        ".ini": "[lightblack]",
        ".dat": "[lightblack]",
        ".dll": "[lightblack]",
        ".pkg": "[lightblack]",
        ".bin": "[lightblack]",
        ".cmd": "[lightblack]",
        # misc
        ".lnk": "[green]",
        ".url": "[green]",
        ".tmp": "[lightblack]",
        ".gitignore": "[lightblack]",
        ".gitconfig": "[lightblack]",
        ".ttf": "[cyan]",
    }


class FileDisclaimer:
    """Hint disclaimer for exceptions during path resolving."""
    _strinit = "[lightblack] + [dim]"
    _rstr = "[lightblack]"
    _strend = "[/dim]"
    _hint = "[cyan]"

    cd_d_flag = f"{_strinit}{_hint}'/d'{_rstr} in this command is automated, you do not need to type it!{_strend}"

    res_flag_typo = f"{_strinit}Make sure you typed exactly {_hint}\"-<\"{_rstr} right before the flag name.{_strend}"
    res_flag_typo_2 = f"{_strinit}Make sure the {_hint}flag name{_rstr} you typed exists.{_strend}"

    utf_evaluator = f"{_strinit}Make sure the {_hint}file{_rstr} is encoded in {_hint}UTF-8{_rstr} or {_hint}UTF-16{_rstr}.{_strend}"

# math lists
import ast
import math
import operator


class MathList:
    """Lister for math utilities and help display."""
    MATHSET_HELP = {  # noqa: RUF012
        "sqrt": "sqrt(x) - Returns the square root of x.",
        "sin": "sin(x) - Returns the sine of x in radians.",
        "cos": "cos(x) - Returns the cosine of x in radians.",
        "tan": "tan(x) - Returns the tangent of x in radians.",
        "log": "log(x, [base]) - Returns the natural logarithm of x (or logarithm with specified base).",
        "log10": "log10(x) - Returns the base-10 logarithm of x.",
        "abs": "abs(x) - Returns the absolute value of x.",
        "pi": "pi - Mathematical constant for π (~3.14159).",
        "e": "e - Mathematical constant for e (~2.71828).",
        "fact": "fact(x) - Returns the factorial approximation of x (for integers).",
        "gamma": "gamma(x) - Returns the factorial approximation of x (for variables and floats)."
    }

    mathset = {  # noqa: RUF012
        "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos,
        "tan": math.tan, "log": math.log, "log10": math.log10,
        "abs": abs, "pi": math.pi, "e": math.e, "fact": math.factorial,
        "gamma": math.gamma,
    }

    _reserved = {  # noqa: RUF012
        "sqrt", "sin", "cos",
        "tan", "log", "log10",
        "abs", "pi", "e", "fact",
        "gamma"
    }
    
    _uncallable = {  # noqa: RUF012
        "pi", "e",
        }

    _allowed_operators = {  # noqa: RUF012
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    math_funcslist = (
        "[blue]MathSet[/blue]:\n"
        "[cyan]sqrt, sin, cos, tan, log, log10, pi, e, fact, gamma[/cyan].\n"
        "You can use [green]mathhelp <mathset>[/green] to dive deeper in MathSet usage."
    )

# mamidi

class MidiSetList:
    """Keybinds and note assigning list for Piano Keyboard."""
    note_freqs = {  # noqa: RUF012
        'C4': 261.63, 'C#4': 277.18,
        'D4': 293.66, 'D#4': 311.13,
        'E4': 329.63,
        'F4': 349.23, 'F#4': 369.99,
        'G4': 392.00, 'G#4': 415.30,
        'A4': 440.00, 'A#4': 466.16,
        'B4': 493.88,
        'C5': 523.25, 'C#5': 554.37,
        'D5': 587.33, 'D#5': 622.25,
        'E5': 659.26,
        'F5': 698.46, 'F#5': 739.99,
        'G5': 783.99, 'G#5': 830.61,
        'A5': 880.00, 'A#5': 932.33,
        'B5': 987.77,
        'C6': 1046.50
    }

    note_k_bindings = {  # noqa: RUF012
        'q': ('C', note_freqs['C4']), '2': ('C#4', note_freqs['C#4']),
        'w': ('D', note_freqs['D4']), '3': ('D#4', note_freqs['D#4']),
        'e': ('E', note_freqs['E4']),
        'r': ('F', note_freqs['F4']), '5': ('F#4', note_freqs['F#4']),
        't': ('G', note_freqs['G4']), '6': ('G#4', note_freqs['G#4']),
        'y': ('A', note_freqs['A4']), '7': ('A#4', note_freqs['A#4']),
        'u': ('B', note_freqs['B4']),
        'i': ('C5', note_freqs['C5']), '9': ('C#5', note_freqs['C#5']),
        'o': ('D5', note_freqs['D5']), '0': ('D#5', note_freqs['D#5']),
        'p': ('E5', note_freqs['E5']),
        'z': ('F5', note_freqs['F5']), 's': ('F#5', note_freqs['F#5']),
        'x': ('G5', note_freqs['G5']), 'd': ('G#5', note_freqs['G#5']),
        'c': ('A5', note_freqs['A5']), 'f': ('A#5', note_freqs['A#5']),
        'v': ('B5', note_freqs['B5']),
        'b': ('C6', note_freqs['C6'])
    }


class SystemList:
    """System global list for requirements and miscellaneous system information."""
    min_req = """
  [blue]OS[/blue]        : [cyan]Windows 10 / Linux (kernel 4.19+)[/cyan]
  [blue]CPU[/blue]       : [cyan]Single-Core 1.5 GHz (x86-64)[/cyan]
  [blue]RAM[/blue]       : [cyan]128MB free memory[/cyan]
  [blue]Storage[/blue]   : [cyan]200MB free space (including dependencies)[/cyan]
  [blue]Python[/blue]    : [cyan]3.10+ Python version[/cyan]
"""

    rec_req = """
  [blue]OS[/blue]        : [cyan]Windows 10 / Linux (kernel 4.19+)[/cyan]
  [blue]CPU[/blue]       : [cyan]Dual-Core 2.0 GHz (x86-64 / ARM64)[/cyan]
  [blue]RAM[/blue]       : [cyan]1024MB free memory[/cyan]
  [blue]Storage[/blue]   : [cyan]400MB free space[/cyan]
  [blue]Python[/blue]    : [cyan]3.13 Python version[/cyan]
"""
