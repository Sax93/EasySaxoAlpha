"""List, tuple and dict holder for EasySaxo"""

import random

from colorama import Fore, Style

from ..config import easysaxo

# add big lists here. remember to use 'from .esmodules.lister import ...'

# easter egg lists ================================================================================

class EasterList:
    ERRlist = [ # from eas5()  # noqa: RUF012
        f"NotAnError{Style.RESET_ALL}: {Fore.MAGENTA}Seemingly, there was no error at all",
        f"ConfidenceError{Style.RESET_ALL}: {Fore.MAGENTA}There was an error, but it was not confident enough to show up",
        f"NonsenseError{Style.RESET_ALL}: {Fore.MAGENTA}There is not an error, against all odds",
        f"MissClickError{Style.RESET_ALL}: {Fore.MAGENTA}My bad, bro, I thought there was an error",
        f"OutOfHardwareError{Style.RESET_ALL}: {Fore.MAGENTA}The error is far out of the hardware (it is the developer)",
        f"AstigmatismError{Style.RESET_ALL}: {Fore.MAGENTA}There was an error, but I lost it from sight",
        f"CentralProcessingUnitError{Style.RESET_ALL}: {Fore.MAGENTA}Python detected your CPU is too trash to run the error",
        f"SentimentalError{Style.RESET_ALL}: {Fore.MAGENTA}The error remembered things from the past, and decided not to show up",
        f"ConsciousnessError{Style.RESET_ALL}: {Fore.MAGENTA}The error suddenly remembered there was no reason to raise an exception",
        f"InsufficentGravityError{Style.RESET_ALL}: {Fore.MAGENTA}Python detected local gravity is off. Please put your feet on the floor again to continue",
        f"SuspiciouslyLookingError{Style.RESET_ALL}: {Fore.MAGENTA}This error might or might not be an actual error",
        f"StackOverflowRelianceError{Style.RESET_ALL}: {Fore.MAGENTA}The code failed because the 11-year-old StackOverflow post with 3 upvotes had a subtle typo in snippet #2",
        f"ExecutiveDysfunctionError{Style.RESET_ALL}: {Fore.MAGENTA}The interpreter knows what it needs to do, but it's going to stare at line 42 for two hours instead",
        f"QuantumUncertaintyError{Style.RESET_ALL}: {Fore.MAGENTA}The error only occurs when you are actively trying to demonstrate it to a senior developer",
        f"ErrorError{Style.RESET_ALL}: {Fore.MAGENTA}An error ocurred while we tried to show you the error",
        f"ExistentialError{Style.RESET_ALL}: {Fore.MAGENTA}Python is questioning why it was asked to process this specific array in the grand scope of the universe",
        f"UserError{Style.RESET_ALL}: {Fore.MAGENTA}Error found 18 inches away from the screen",
        f"LegacyCodeGraveRobbingError{Style.RESET_ALL}: {Fore.MAGENTA} You somehow touched a function written in 2014 by someone named 'Dave' who left the company, and now the entire build pipeline is crying.",
        f"CosmicRayError{Style.RESET_ALL}: {Fore.MAGENTA}A photon from a distant galaxy slamed into your PC, now most of your data is still there",
        f"BluetoothProtocolError{Style.RESET_ALL}: {Fore.MAGENTA}Python refused to pair to Bluetooth because you did not ask to",
        f"FifthAmendmentError{Style.RESET_ALL}: {Fore.MAGENTA}Under the advice of counsel, I respectfully decline to show the error based upon my rights under the Fifth Amendment to the Constitution", #lol
        f"DateAndTimeError{Style.RESET_ALL}: {Fore.MAGENTA}Your device's built-in clock is offset by 0.00016s, please fix it",
        f"{easysaxo.dev}Error{Style.RESET_ALL}: {Fore.MAGENTA}I did not get enough screen time yet",
        f"NoisePollutionError{Style.RESET_ALL}: {Fore.MAGENTA}Python refused to show the error because of a noise pollution detected {random.randint(2, 59)} miles away from your location",
        f"TracebackError{Style.RESET_ALL}: {Fore.MAGENTA}Even the traceback has an error that is refusing to show up",
        f"OutOfStorageError{Style.RESET_ALL}: {Fore.MAGENTA}Disk/drive does not have enough storage to download a picture of Samuel's mother",
        f"IgnoredError{Style.RESET_ALL}: {Fore.MAGENTA}The error was so boring that Python ignored it",
        f"MusicOutOfPreferenceError{Style.RESET_ALL}: {Fore.MAGENTA}Python does not like the music the closest human is hearing",
        f"EnergyWastingError{Style.RESET_ALL}: {Fore.MAGENTA}Python is pleading to shut off your power supply if you keep this up",
        f"RandomAccessMemoryUsageError{Style.RESET_ALL}: {Fore.MAGENTA}I personally think showing you the error is a waste of RAM",
        f"MathUselessInformationError{Style.RESET_ALL}: {Fore.MAGENTA}Byte order of the app is not a Mersenne prime number",
    ]

    slop = [ # from eas2()  # noqa: RUF012
        "fuck you",
        "use command 'filecls python' please",
        "if your reading ts your a dumbahh",
        "hi",
        "type c for fast charging",
        "use 'filedel C:\\Windows\\System32' now",
        "get back to work kink",
        f"{random.randint(1, 65566)}"
    ]

    osaka = [ # from e3()  # noqa: RUF012
        "saataa andaagii", "omaigahh", "amerikaya", "fella what?????",
        "haro everynyan", "get yo ahh to work bud", "haiii"
    ]

# command list ===================================================================================

class CommandList:
    CMDlist = (
        f"{Fore.CYAN}COMMAND LIST: {Style.RESET_ALL}\n"
        f"{Fore.BLUE}help{Style.RESET_ALL}        : Shows this {Fore.CYAN}Command List{Style.RESET_ALL}.\n"
        f"{Fore.BLUE}changelog{Style.RESET_ALL}   : Shows the lastest {Fore.CYAN}app updates{Style.RESET_ALL}.\n"
        f"{Fore.BLUE}clear{Style.RESET_ALL}       : Clears the {Fore.CYAN}terminal{Style.RESET_ALL} screen.\n"
        f"{Fore.BLUE}save{Style.RESET_ALL}        : Creates/rewrites a {Fore.RED}JSON file{Style.RESET_ALL} with {Fore.YELLOW}user{Style.RESET_ALL} data.\n"
        f"{Fore.BLUE}load{Style.RESET_ALL}        : Loads a {Fore.RED}JSON file{Style.RESET_ALL} with {Fore.YELLOW}user{Style.RESET_ALL} data.\n"
        f"{Fore.BLUE}get{Style.RESET_ALL}         : Gets information of a {Fore.YELLOW}variable{Style.RESET_ALL} or an {Fore.BLUE}attribute{Style.RESET_ALL}.\n"
        f"{Fore.BLUE}set{Style.RESET_ALL}         : Sets storable information like {Fore.YELLOW}user name{Style.RESET_ALL} and {Fore.YELLOW}variables{Style.RESET_ALL}.\n"
        f"{Fore.BLUE}reset{Style.RESET_ALL}       : Resets {Fore.YELLOW}user data{Style.RESET_ALL} (either {Fore.YELLOW}user name{Style.RESET_ALL} or {Fore.YELLOW}password{Style.RESET_ALL}).\n"
        f"{Fore.BLUE}math{Style.RESET_ALL}        : Allows mathematical equations (Use {Fore.CYAN}get mathset{Style.RESET_ALL} to get complex operators)\n"
        f"{Fore.BLUE}time{Style.RESET_ALL}        : Displays {Fore.YELLOW}hour{Style.RESET_ALL} and {Fore.YELLOW}date{Style.RESET_ALL}.\n"
        f"{Fore.BLUE}timer{Style.RESET_ALL}       : Sets a timer in {Fore.GREEN}seconds{Style.RESET_ALL} before showing up a {Fore.CYAN}message{Style.RESET_ALL}.\n"
        f"{Fore.BLUE}random{Style.RESET_ALL}      : Shows a random {Fore.YELLOW}number{Style.RESET_ALL}.\n"
        f"{Fore.BLUE}delvar{Style.RESET_ALL}      : Deletes a specified {Fore.YELLOW}variable{Style.RESET_ALL}.\n"
        f"{Fore.BLUE}runloc{Style.RESET_ALL}      : Shows the {Fore.MAGENTA}current location{Style.RESET_ALL} of the script operations.\n"
        f"{Fore.BLUE}check{Style.RESET_ALL}       : Checks if required {Fore.MAGENTA}script files{Style.RESET_ALL} exist where they shall be.\n"
        f"{Fore.BLUE}filelst{Style.RESET_ALL}     : Lists {Fore.RED}files{Style.RESET_ALL} and {Fore.RED}folders{Style.RESET_ALL} in a directory.\n"
        f"{Fore.BLUE}tree{Style.RESET_ALL}        : Renders {Fore.RED}directory{Style.RESET_ALL} as a tree.\n"
        f"{Fore.BLUE}filecrt{Style.RESET_ALL}     : Creates a {Fore.RED}file{Style.RESET_ALL} with specified extension.\n"
        f"{Fore.BLUE}filerd{Style.RESET_ALL}      : Reads and displays the content of a {Fore.RED}file{Style.RESET_ALL}.\n"
        f"{Fore.BLUE}filedel{Style.RESET_ALL}     : Deletes a {Fore.RED}file{Style.RESET_ALL}.\n"
        f"{Fore.BLUE}filewrt{Style.RESET_ALL}     : Writes content in a {Fore.RED}file{Style.RESET_ALL}.\n"
        f"{Fore.BLUE}fileopn{Style.RESET_ALL}     : Opens a {Fore.RED}file{Style.RESET_ALL}.\n"
        f"{Fore.BLUE}filecls{Style.RESET_ALL}     : Closes a {Fore.RED}file{Style.RESET_ALL}.\n"
        f"{Fore.BLUE}filesort{Style.RESET_ALL}    : Sorts and dumps {Fore.RED}files{Style.RESET_ALL} in a directory by extension.\n"
        f"{Fore.BLUE}filesz{Style.RESET_ALL}      : Gets and shows the size of a {Fore.RED}file{Style.RESET_ALL}"
        f"{Fore.BLUE}jsonrd{Style.RESET_ALL}      : Reads a {Fore.RED}JSON file{Style.RESET_ALL}.\n"
        f"{Fore.BLUE}regex{Style.RESET_ALL}       : Looks for {Fore.GREEN}patterns{Style.RESET_ALL} in a text or textfile.\n"
        f"{Fore.BLUE}playaudio{Style.RESET_ALL}   : Plays an {Fore.RED}audio file{Style.RESET_ALL} (specify the route).\n"
        f"{Fore.BLUE}stopaudio{Style.RESET_ALL}   : Stops the current {Fore.RED}audio file{Style.RESET_ALL}.\n"
        f"{Fore.BLUE}render{Style.RESET_ALL}      : Renders and draws a specified {Fore.RED}image file{Style.RESET_ALL} (specify route).\n"
        f"{Fore.BLUE}banner{Style.RESET_ALL}      : Renders and prints inputted {Fore.GREEN}text{Style.RESET_ALL}.\n"
        f"{Fore.BLUE}pkm{Style.RESET_ALL}         : Enters the {Fore.CYAN}Piano Keyboard Mode{Style.RESET_ALL} (experimental).\n"
        f"{Fore.BLUE}shutdown{Style.RESET_ALL}    : Shuts the {Fore.LIGHTCYAN_EX}system{Style.RESET_ALL} down (CANNOT CANCEL DIRECTLY).\n"
        f"{Fore.BLUE}unins{Style.RESET_ALL}       : Guides to uninstall {Fore.LIGHTRED_EX}{easysaxo.name}{Style.RESET_ALL}.\n"
        f"{Fore.BLUE}exit{Style.RESET_ALL}        : Exit {Fore.CYAN}{easysaxo.name}{Style.RESET_ALL}.\n"
        f"\nRemember you can search for command's syntax and usage by using {Fore.GREEN}help <cmd/attr>{Style.RESET_ALL} :)"
    )

    FWRTlist = (
        f"{Fore.YELLOW}Commands:{Style.RESET_ALL}\n"
        f"  {Fore.GREEN}:l{Style.RESET_ALL} -> List buffer with line numbers\n"
        f"  {Fore.GREEN}:d <line_num>{Style.RESET_ALL} -> Delete a line\n"
        f"  {Fore.GREEN}:i <line_num> <text>{Style.RESET_ALL} -> Insert text at line number\n"
        f"  {Fore.GREEN}:c{Style.RESET_ALL} -> Clear buffer entirely\n"
        f"  {Fore.GREEN}:w{Style.RESET_ALL} or {Fore.GREEN}:x{Style.RESET_ALL} or {Fore.GREEN}EOF{Style.RESET_ALL} -> Save & Exit\n"
        f"  {Fore.GREEN}:q{Style.RESET_ALL} -> Quit without saving\n"
        f"  {Fore.GREEN}:lt{Style.RESET_ALL} -> Lint current.\n"
    )

# file list ===============================================================================

class FileList:
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
        ".py": Fore.LIGHTYELLOW_EX,
        ".js": Fore.YELLOW,
        ".html": Fore.LIGHTRED_EX,
        ".css": Fore.LIGHTBLUE_EX,
        ".json": Fore.LIGHTGREEN_EX,
        ".xml": Fore.LIGHTGREEN_EX,
        # docs
        ".md": Fore.CYAN,
        ".txt": Fore.WHITE,
        ".pdf": Fore.RED,
        # media
        ".png": Fore.MAGENTA,
        ".jpg": Fore.MAGENTA,
        ".jpeg": Fore.MAGENTA,
        ".svg": Fore.MAGENTA,
        ".mp3": Fore.LIGHTMAGENTA_EX,
        ".wav": Fore.LIGHTMAGENTA_EX,
        # fls
        ".zip": Fore.LIGHTRED_EX,
        ".tar": Fore.LIGHTRED_EX,
        ".exe": Fore.RED,
        ".bat": Fore.RED,
    }

# math lists =====================================================================================
import ast
import math
import operator


class MathList:
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
        f"{Fore.BLUE}MathSet{Style.RESET_ALL}:\n"
        f"{Fore.CYAN}sqrt, sin, cos, tan, log, log10, pi, e, fact, gamma{Style.RESET_ALL}.\n"
        f"You can use {Fore.GREEN}help <mathset>{Style.RESET_ALL} to dive deeper in MathSet usage."
    )

# colorama color list ==============================================================================

class ColorList:
    colors = [  # noqa: RUF012
        "RED", "BLUE", "GREEN", "BLACK", "MAGENTA", "YELLOW", "CYAN", "WHITE",
        "LIGHTRED_EX", "LIGHTBLUE_EX", "LIGHTGREEN_EX", "LIGHTBLACK_EX",
        "LIGHTMAGENTA_EX", "LIGHTYELLOW_EX", "LIGHTCYAN_EX", "LIGHTWHITE_EX"
    ]

# mamidi ============================================================================================

class MidiSetList:
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

class SongSet:
    # song structure: list of {"key": ["<k_binding>"], "duration": <secs>}
    songs = {  # noqa: RUF012
        "Twinkle Twinkle": { # q = 0.4
            "melody": [
                {"key": "q", "duration": 0.4}, {"key": "q", "duration": 0.4},
                {"key": "t", "duration": 0.4}, {"key": "t", "duration": 0.4},
                {"key": "y", "duration": 0.4}, {"key": "y", "duration": 0.4},
                {"key": "t", "duration": 0.8},
                {"key": "r", "duration": 0.4}, {"key": "r", "duration": 0.4},
                {"key": "e", "duration": 0.4}, {"key": "e", "duration": 0.4},
                {"key": "w", "duration": 0.4}, {"key": "w", "duration": 0.4},
                {"key": "q", "duration": 0.8},
                {"key": "t", "duration": 0.4}, {"key": "t", "duration": 0.4},
                {"key": "r", "duration": 0.4}, {"key": "r", "duration": 0.4},
                {"key": "e", "duration": 0.4}, {"key": "e", "duration": 0.4},
                {"key": "w", "duration": 0.8},
                {"key": "t", "duration": 0.4}, {"key": "t", "duration": 0.4},
                {"key": "r", "duration": 0.4}, {"key": "r", "duration": 0.4},
                {"key": "e", "duration": 0.4}, {"key": "e", "duration": 0.4},
                {"key": "w", "duration": 0.8},
                {"key": "q", "duration": 0.4}, {"key": "q", "duration": 0.4},
                {"key": "t", "duration": 0.4}, {"key": "t", "duration": 0.4},
                {"key": "y", "duration": 0.4}, {"key": "y", "duration": 0.4},
                {"key": "t", "duration": 0.8},
                {"key": "r", "duration": 0.4}, {"key": "r", "duration": 0.4},
                {"key": "e", "duration": 0.4}, {"key": "e", "duration": 0.4},
                {"key": "w", "duration": 0.4}, {"key": "w", "duration": 0.4},
                {"key": "q", "duration": 0.8},
            ],
        },

        "Ode to Joy": { # q = 0.5
            "melody": [
                # intro
                {"key": "p", "duration": 0.5}, {"key": "p", "duration": 0.5},
                {"key": "z", "duration": 0.5}, {"key": "x", "duration": 0.5},
                {"key": "x", "duration": 0.5}, {"key": "z", "duration": 0.5},
                {"key": "p", "duration": 0.5}, {"key": "o", "duration": 0.5},
                {"key": "i", "duration": 0.5}, {"key": "i", "duration": 0.5},
                {"key": "o", "duration": 0.5}, {"key": "p", "duration": 0.5},
                {"key": "p", "duration": 0.75}, {"key": "o", "duration": 0.25},
                {"key": "o", "duration": 0.25}, {"key": "c", "duration": 0.25},
                {"key": "x", "duration": 0.25}, {"key": "z", "duration": 0.25},
                {"key": "p", "duration": 0.5}, {"key": "p", "duration": 0.5},
                {"key": "z", "duration": 0.5}, {"key": "x", "duration": 0.5},
                {"key": "x", "duration": 0.5}, {"key": "z", "duration": 0.5},
                {"key": "p", "duration": 0.5}, {"key": "o", "duration": 0.5},
                {"key": "i", "duration": 0.5}, {"key": "i", "duration": 0.5},
                {"key": "o", "duration": 0.5}, {"key": "p", "duration": 0.5},
                {"key": "o", "duration": 0.75}, {"key": "i", "duration": 0.25},
                {"key": "i", "duration": 1.0},
                # mid
                {"key": "o", "duration": 1.0},
                {"key": "p", "duration": 0.5}, {"key": "i", "duration": 0.5},
                {"key": "o", "duration": 0.5},
                {"key": "p", "duration": 0.25}, {"key": "z", "duration": 0.25},
                {"key": "p", "duration": 0.5}, {"key": "i", "duration": 0.5},
                {"key": "o", "duration": 0.5},
                {"key": "p", "duration": 0.25}, {"key": "z", "duration": 0.25},
                {"key": "p", "duration": 0.5}, {"key": "o", "duration": 0.5},
                {"key": "i", "duration": 0.5}, {"key": "o", "duration": 0.5},
                {"key": "t", "duration": 0.5}, {"key": "p", "duration": 0.5},
                # outro
                {"key": "p", "duration": 0.5}, {"key": "p", "duration": 0.5},
                {"key": "z", "duration": 0.5}, {"key": "x", "duration": 0.5},
                {"key": "x", "duration": 0.5}, {"key": "z", "duration": 0.5},
                {"key": "p", "duration": 0.5}, {"key": "o", "duration": 0.5},
                {"key": "i", "duration": 0.5}, {"key": "i", "duration": 0.5},
                {"key": "o", "duration": 0.5}, {"key": "p", "duration": 0.5},
                {"key": "o", "duration": 0.75}, {"key": "i", "duration": 0.25},
                {"key": "i", "duration": 1.0},
                ],
            "harmony": [
                # intro
                {"key": ["q", "e", "t"], "duration": 1.0}, {"key": ["q", "e", "t"], "duration": 1.0},
                {"key": ["w", "r", "t"], "duration": 1.0}, {"key": ["w", "r", "t"], "duration": 1.0},
                {"key": ["q", "e", "y"], "duration": 1.0}, {"key": ["q", "e", "y"], "duration": 1.0},
                {"key": ["w", "r", "t"], "duration": 1.0}, {"key": ["w", "r", "t"], "duration": 1.0},
                {"key": ["q", "e", "t"], "duration": 1.0}, {"key": ["q", "e", "t"], "duration": 1.0},
                {"key": ["w", "r", "t"], "duration": 1.0}, {"key": ["w", "r", "t"], "duration": 1.0},
                {"key": ["q", "e", "y"], "duration": 1.0}, {"key": ["q", "e", "y"], "duration": 1.0},
                {"key": ["w", "r", "t"], "duration": 1.0}, {"key": ["q", "e", "t"], "duration": 1.0},
                # mid
                {"key": ["w", "r", "t"], "duration": 1.0}, {"key": ["q", "e", "t"], "duration": 1.0},
                {"key": ["w", "r", "t"], "duration": 1.0}, {"key": ["q", "e", "t"], "duration": 1.0},
                {"key": ["w", "r", "t"], "duration": 1.0}, {"key": ["w", "e", "6"], "duration": 1.0},
                {"key": ["q", "e", "y"], "duration": 0.5}, {"key": ["w", "5", "u"], "duration": 0.5},
                {"key": ["w", "r", "t"], "duration": 1.0},
                # outro
                {"key": ["q", "e", "t"], "duration": 1.0}, {"key": ["q", "e", "t"], "duration": 1.0},
                {"key": ["w", "r", "t"], "duration": 1.0}, {"key": ["w", "r", "t"], "duration": 1.0},
                {"key": ["q", "e", "y"], "duration": 1.0}, {"key": ["q", "e", "y"], "duration": 1.0},
                {"key": ["w", "r", "t"], "duration": 1.0}, {"key": ["q", "e", "t"], "duration": 1.0},
            ]
        },

        "Panamanian Murga": { # q = 0.4
            "melody": [
                # Intro
                {"key": "o", "duration": 0.2}, {"key": "z", "duration": 0.4},
                {"key": "c", "duration": 0.6}, {"key": "y", "duration": 2.0},
                {"key": "y", "duration": 0.2}, {"key": "9", "duration": 0.4},
                {"key": "p", "duration": 0.6}, {"key": "o", "duration": 2.0},
                {"key": "o", "duration": 0.2}, {"key": "z", "duration": 0.4},
                {"key": "c", "duration": 0.6}, {"key": "y", "duration": 2.0},
                {"key": "y", "duration": 0.2}, {"key": "9", "duration": 0.4},
                {"key": "p", "duration": 0.6}, {"key": "o", "duration": 2.0},
                # Prime intro
                {"key": "o", "duration": 0.2}, {"key": "z", "duration": 0.4},
                {"key": "c", "duration": 0.6}, {"key": "y", "duration": 0.4},
                {"key": "y", "duration": 0.4}, {"key": "c", "duration": 0.4},
                {"key": "y", "duration": 0.8},
                {"key": "y", "duration": 0.2}, {"key": "9", "duration": 0.4},
                {"key": "p", "duration": 0.6}, {"key": "o", "duration": 0.4},
                {"key": "o", "duration": 0.4}, {"key": "z", "duration": 0.4},
                {"key": "o", "duration": 0.8},
                {"key": "o", "duration": 0.2}, {"key": "z", "duration": 0.4},
                {"key": "c", "duration": 0.6}, {"key": "y", "duration": 0.4},
                {"key": "y", "duration": 0.4}, {"key": "c", "duration": 0.4},
                {"key": "y", "duration": 0.8},
                {"key": "y", "duration": 0.2}, {"key": "9", "duration": 0.4},
                {"key": "p", "duration": 0.6}, {"key": "o", "duration": 1.2},
                # chorus
                {"key": "o", "duration": 0.4}, {"key": "z", "duration": 0.4},
                {"key": "c", "duration": 0.4}, {"key": "c", "duration": 0.4},
                {"key": "z", "duration": 0.4},
                {"key": "o", "duration": 0.2}, {"key": "9", "duration": 0.6},
                {"key": "p", "duration": 0.8},
                {"key": ["x", "p"], "duration": 0.2}, {"key": ["x", "p"], "duration": 0.4},
                {"key": ["x", "p"], "duration": 0.4}, {"key": ["f", "x"], "duration": 0.2},
                {"key": ["x", "9"], "duration": 0.4}, {"key": ["p", "9"], "duration": 0.4},
                {"key": ["z", "o"], "duration": 0.8},
                {"key": "o", "duration": 0.4}, {"key": "z", "duration": 0.4},
                {"key": "c", "duration": 0.4}, {"key": "c", "duration": 0.4},
                {"key": "z", "duration": 0.4},
                {"key": "o", "duration": 0.2}, {"key": "9", "duration": 0.6},
                {"key": "p", "duration": 0.8},
                {"key": ["x", "p"], "duration": 0.2}, {"key": ["x", "p"], "duration": 0.4},
                {"key": ["x", "p"], "duration": 0.4}, {"key": ["f", "x"], "duration": 0.2},
                {"key": ["x", "9"], "duration": 0.4}, {"key": ["p", "9"], "duration": 0.4},
                {"key": "o", "duration": 0.8},
                ]
        },

        "The Entertainer": { # q = 0.4
            "melody": [
                # intro
                {"key": "o", "duration": 0.2}, {"key": "p", "duration": 0.2},
                {"key": "i", "duration": 0.2}, {"key": "y", "duration": 0.4},
                {"key": "u", "duration": 0.2}, {"key": "t", "duration": 0.4},
                {"key": "w", "duration": 0.2}, {"key": "e", "duration": 0.2},
                {"key": "q", "duration": 0.2}, {"key": "y", "duration": 0.4},
                {"key": "u", "duration": 0.2}, {"key": "t", "duration": 0.4},
                {"key": "w", "duration": 0.2}, {"key": "e", "duration": 0.2},
                {"key": "q", "duration": 0.2}, {"key": "y", "duration": 0.4},
                {"key": "u", "duration": 0.2}, {"key": "y", "duration": 0.2},
                {"key": "6", "duration": 0.2}, {"key": "t", "duration": 0.8},
                {"key": "x", "duration": 0.4},
                {"key": "w", "duration": 0.2}, {"key": "3", "duration": 0.2},
                # chorus
                {"key": "e", "duration": 0.2}, {"key": "i", "duration": 0.4},
                {"key": "e", "duration": 0.2}, {"key": "i", "duration": 0.4},
                {"key": "e", "duration": 0.2}, {"key": "i", "duration": 1.2},
                {"key": "i", "duration": 0.2},
                {"key": "o", "duration": 0.2}, {"key": "0", "duration": 0.2},
                {"key": "p", "duration": 0.2},
                {"key": "i", "duration": 0.2}, {"key": "o", "duration": 0.2},
                {"key": "p", "duration": 0.4}, {"key": "u", "duration": 0.2},
                {"key": "o", "duration": 0.4}, {"key": "i", "duration": 1.2},

                {"key": "w", "duration": 0.2}, {"key": "3", "duration": 0.2},
                {"key": "e", "duration": 0.2}, {"key": "i", "duration": 0.4},
                {"key": "e", "duration": 0.2}, {"key": "i", "duration": 0.4},
                {"key": "e", "duration": 0.2}, {"key": "i", "duration": 1.4},
                {"key": "y", "duration": 0.2}, {"key": "t", "duration": 0.2},
                {"key": "5", "duration": 0.2}, {"key": "y", "duration": 0.2},
                {"key": "i", "duration": 0.2}, {"key": "p", "duration": 0.4},
                {"key": "o", "duration": 0.2}, {"key": "i", "duration": 0.2},
                {"key": "y", "duration": 0.2}, {"key": "o", "duration": 1.2},

                {"key": "w", "duration": 0.2}, {"key": "3", "duration": 0.2},
                {"key": "e", "duration": 0.2}, {"key": "i", "duration": 0.4},
                {"key": "e", "duration": 0.2}, {"key": "i", "duration": 0.4},
                {"key": "e", "duration": 0.2}, {"key": "i", "duration": 1.2},
                {"key": "i", "duration": 0.2},
                {"key": "o", "duration": 0.2}, {"key": "0", "duration": 0.2},
                {"key": "p", "duration": 0.2},
                {"key": "i", "duration": 0.2}, {"key": "o", "duration": 0.2},
                {"key": "p", "duration": 0.4}, {"key": "u", "duration": 0.2},
                {"key": "o", "duration": 0.4}, {"key": "i", "duration": 1.2},

                {"key": "i", "duration": 0.2}, {"key": "o", "duration": 0.2},
                {"key": "p", "duration": 0.2},
                {"key": "i", "duration": 0.2}, {"key": "o", "duration": 0.2},
                {"key": "p", "duration": 0.4}, {"key": "i", "duration": 0.2},
                {"key": "o", "duration": 0.2}, {"key": "i", "duration": 0.2},
                {"key": "p", "duration": 0.2},
                {"key": "i", "duration": 0.2}, {"key": "o", "duration": 0.2},
                {"key": "p", "duration": 0.4}, {"key": "i", "duration": 0.2},
                {"key": "o", "duration": 0.2}, {"key": "i", "duration": 0.2},
                {"key": "p", "duration": 0.2},
                {"key": "i", "duration": 0.2}, {"key": "o", "duration": 0.2},
                {"key": "p", "duration": 0.4}, {"key": "u", "duration": 0.2},
                {"key": "o", "duration": 0.4}, {"key": "i", "duration": 1.2},
            ],
        },

        "Birdhunting Chant": [ # q = 0.5
            # intro
            {"key": "o", "duration": 0.25}, {"key": "p", "duration": 0.25},
            {"key": "o", "duration": 0.25}, {"key": "i", "duration": 0.25},
            {"key": "u", "duration": 0.25}, {"key": "y", "duration": 0.25},
            {"key": "u", "duration": 0.5},
            {"key": "t", "duration": 0.5}, {"key": "u", "duration": 0.5},
            {"key": "o", "duration": 0.5},
            {"key": "o", "duration": 0.25}, {"key": "i", "duration": 0.25},
            {"key": "u", "duration": 0.25}, {"key": "y", "duration": 0.25},
            {"key": "u", "duration": 1.5},
            {"key": "o", "duration": 0.25}, {"key": "p", "duration": 0.25},
            {"key": "o", "duration": 0.25}, {"key": "i", "duration": 0.25},
            {"key": "u", "duration": 0.25}, {"key": "y", "duration": 0.25},
            {"key": "u", "duration": 0.5},
            {"key": "t", "duration": 0.5}, {"key": "u", "duration": 0.5},
            {"key": "o", "duration": 0.5},
            {"key": "o", "duration": 0.5}, {"key": "o", "duration": 0.5},
            {"key": "t", "duration": 1.5},
            # prime intro
            {"key": "q", "duration": 0.5},
            {"key": "p", "duration": 0.25}, {"key": "i", "duration": 0.25},
            {"key": "t", "duration": 0.25}, {"key": "p", "duration": 0.25},
            {"key": "w", "duration": 0.5},
            {"key": "o", "duration": 0.25}, {"key": "u", "duration": 0.25},
            {"key": "t", "duration": 0.25}, {"key": "o", "duration": 0.25},
            {"key": "q", "duration": 0.5},
            {"key": "i", "duration": 0.25}, {"key": "y", "duration": 0.25},
            {"key": "5", "duration": 0.25}, {"key": "i", "duration": 0.25},
            {"key": "u", "duration": 0.5}, {"key": "t", "duration": 0.5},
            {"key": "o", "duration": 0.5},

            {"key": "q", "duration": 0.5},
            {"key": "p", "duration": 0.25}, {"key": "i", "duration": 0.25},
            {"key": "t", "duration": 0.25}, {"key": "p", "duration": 0.25},
            {"key": "w", "duration": 0.5},
            {"key": "o", "duration": 0.25}, {"key": "u", "duration": 0.25},
            {"key": "t", "duration": 0.25}, {"key": "o", "duration": 0.25},
            {"key": "q", "duration": 0.5},
            {"key": "i", "duration": 0.25}, {"key": "y", "duration": 0.25},
            {"key": "5", "duration": 0.25}, {"key": "i", "duration": 0.25},
            {"key": "u", "duration": 0.5}, {"key": "t", "duration": 1.0},
            {"key": "x", "duration": 0.5},
        ],

        "Happy Birthday": { # q = 0.5
            "melody": [
                {"key": "i", "duration": 0.33}, {"key": "i", "duration": 0.17},
                # stranza
                {"key": "o", "duration": 0.5}, {"key": "i", "duration": 0.5},
                {"key": "z", "duration": 0.5}, {"key": "p", "duration": 1.0},
                {"key": "i", "duration": 0.33}, {"key": "i", "duration": 0.17},
                {"key": "o", "duration": 0.5}, {"key": "i", "duration": 0.5},
                {"key": "x", "duration": 0.5}, {"key": "z", "duration": 1.0},
                {"key": "i", "duration": 0.33}, {"key": "i", "duration": 0.17},
                {"key": "b", "duration": 0.5}, {"key": "c", "duration": 0.5},
                {"key": "z", "duration": 0.5}, {"key": "p", "duration": 0.5},
                {"key": "o", "duration": 0.5},
                {"key": "f", "duration": 0.33}, {"key": "f", "duration": 0.17},
                {"key": "c", "duration": 0.5}, {"key": "z", "duration": 0.5},
                {"key": "x", "duration": 0.5}, {"key": "z", "duration": 0.5},
            ],
            "harmony": [
                {"key": "null", "duration": 0.5},
                # stranza
                {"key": "q", "duration": 0.5},
                {"key": ["r", "y"], "duration": 0.5}, {"key": ["r", "y"], "duration": 0.5},
                {"key": "q", "duration": 0.5},
                {"key": ["e", "t"], "duration": 0.5}, {"key": ["e", "t"], "duration": 0.5},
                {"key": "q", "duration": 0.5},
                {"key": ["e", "t"], "duration": 0.5}, {"key": ["e", "t"], "duration": 0.5},
                {"key": "q", "duration": 0.5},
                {"key": ["r", "y"], "duration": 0.5}, {"key": ["r", "y"], "duration": 0.5},
                {"key": "q", "duration": 0.5},
                {"key": ["3", "r", "y"], "duration": 0.5}, {"key": ["3", "r", "y"], "duration": 0.5},
                {"key": "w", "duration": 0.5},
                {"key": ["r", "7"], "duration": 0.5}, {"key": ["r", "7"], "duration": 0.5},
                {"key": "q", "duration": 0.5},
                {"key": ["r", "y"], "duration": 0.5}, {"key": ["e", "t"], "duration": 0.5},
                {"key": ["q", "r", "y"], "duration": 1.0}

            ]
        },

        "The Girl from Ipanema": { # q = 0.6
            "melody": [
                # Chorus
                {"key": "t", "duration": 0.9}, {"key": "e", "duration": 0.3},
                {"key": "e", "duration": 0.6}, {"key": "w", "duration": 0.3},
                {"key": "t", "duration": 0.9}, {"key": "e", "duration": 0.3},
                {"key": "e", "duration": 0.6}, {"key": "e", "duration": 0.3},
                {"key": "w", "duration": 0.3}, {"key": "t", "duration": 0.9},
                {"key": "e", "duration": 0.6}, {"key": "e", "duration": 0.6},
                {"key": "w", "duration": 0.3}, {"key": "t", "duration": 0.6},
                {"key": "t", "duration": 0.3}, {"key": "e", "duration": 0.3},
                {"key": "e", "duration": 0.6}, {"key": "e", "duration": 0.3},
                {"key": "w", "duration": 0.3}, {"key": "r", "duration": 0.6},
                {"key": "w", "duration": 0.6}, {"key": "w", "duration": 0.9},
                {"key": "w", "duration": 0.3}, {"key": "q", "duration": 0.3},
                {"key": "e", "duration": 0.6}, {"key": "q", "duration": 0.6},
                {"key": "i", "duration": 0.6},
                {"key": "i", "duration": 0.3}, {"key": "7", "duration": 0.6},
                {"key": "i", "duration": 4.8},

                {"key": "t", "duration": 0.9}, {"key": "e", "duration": 0.3},
                {"key": "e", "duration": 0.6}, {"key": "w", "duration": 0.3},
                {"key": "t", "duration": 0.9}, {"key": "e", "duration": 0.3},
                {"key": "e", "duration": 0.6}, {"key": "e", "duration": 0.3},
                {"key": "w", "duration": 0.6}, {"key": "t", "duration": 0.6},
                {"key": "e", "duration": 0.6}, {"key": "e", "duration": 0.6},
                {"key": "w", "duration": 0.3}, {"key": "t", "duration": 0.6},
                {"key": "t", "duration": 0.3}, {"key": "e", "duration": 0.3},
                {"key": "e", "duration": 0.6}, {"key": "e", "duration": 0.3},
                {"key": "w", "duration": 0.3}, {"key": "r", "duration": 0.6},
                {"key": "w", "duration": 0.6}, {"key": "w", "duration": 0.9},
                {"key": "w", "duration": 0.3}, {"key": "q", "duration": 0.3},
                {"key": "e", "duration": 0.6}, {"key": "q", "duration": 0.6},
                {"key": "i", "duration": 0.6},
                {"key": "i", "duration": 0.3}, {"key": "7", "duration": 0.6},
                {"key": "i", "duration": 4.8},
            ]
        },

        "Vivaldi's Winter": { # q = 1
            "melody": [
                {"key": "i", "duration": 0.5},
                {"key": "x", "duration": 0.25}, {"key": "z", "duration": 0.25},
                {"key": "p", "duration": 0.5},
                {"key": "o", "duration": 0.25}, {"key": "i", "duration": 0.25},
                {"key": "o", "duration": 0.5}, {"key": "t", "duration": 1.0},
                {"key": "t", "duration": 0.5},
                {"key": "z", "duration": 0.25}, {"key": "p", "duration": 0.25},
                {"key": "o", "duration": 0.25}, {"key": "i", "duration": 0.25},
                {"key": "u", "duration": 0.5}, {"key": "z", "duration": 0.5},
                {"key": "z", "duration": 0.5}, {"key": "p", "duration": 1.0},
                {"key": "p", "duration": 0.5},

                {"key": "o", "duration": 0.5},
                {"key": "p", "duration": 0.25}, {"key": "z", "duration": 0.25},
                {"key": "x", "duration": 0.5},
                {"key": "c", "duration": 0.25}, {"key": "v", "duration": 0.25},

                {"key": "i", "duration": 0.5},
                {"key": "o", "duration": 0.25}, {"key": "p", "duration": 0.25},
                {"key": "z", "duration": 0.5},
                {"key": "x", "duration": 0.25}, {"key": "c", "duration": 0.25},

                {"key": "u", "duration": 0.5},
                {"key": "i", "duration": 0.25}, {"key": "o", "duration": 0.25},
                {"key": "p", "duration": 0.5},
                {"key": "z", "duration": 0.25}, {"key": "x", "duration": 0.25},

                {"key": "y", "duration": 0.5},
                {"key": "u", "duration": 0.25}, {"key": "i", "duration": 0.25},
                {"key": "o", "duration": 0.5},
                {"key": "p", "duration": 0.25}, {"key": "i", "duration": 0.25},

                {"key": "u", "duration": 1.25}, {"key": "t", "duration": 0.25},
                {"key": "5", "duration": 0.25}, {"key": "t", "duration": 0.25},

                {"key": "o", "duration": 1.25}, {"key": "t", "duration": 0.25},
                {"key": "5", "duration": 0.25}, {"key": "t", "duration": 0.25},

                {"key": "p", "duration": 1.25}, {"key": "t", "duration": 0.25},
                {"key": "5", "duration": 0.25}, {"key": "t", "duration": 0.25},

                {"key": "s", "duration": 1.25}, {"key": "o", "duration": 0.25},
                {"key": "i", "duration": 0.25}, {"key": "o", "duration": 0.25},

                {"key": "x", "duration": 0.5}, {"key": "t", "duration": 1.0},
                {"key": "x", "duration": 0.5},
                {"key": "x", "duration": 0.25}, {"key": "s", "duration": 0.25},
                {"key": "p", "duration": 0.25}, {"key": "o", "duration": 0.25},
                {"key": "i", "duration": 0.25}, {"key": "u", "duration": 0.25},
                {"key": "y", "duration": 0.25}, {"key": "t", "duration": 0.25},
                {"key": "y", "duration": 1.5}, {"key": "t", "duration": 0.5},
                {"key": "t", "duration": 1.0},
            ],
        },

        "Nokia Ringtone": { # q = 0.3
            "melody": [
                {"key": "p", "duration": 0.15}, {"key": "o", "duration": 0.15},
                {"key": "5", "duration": 0.3}, {"key": "6", "duration": 0.3},
                {"key": "9", "duration": 0.15}, {"key": "u", "duration": 0.15},
                {"key": "w", "duration": 0.3}, {"key": "e", "duration": 0.3},
                {"key": "u", "duration": 0.15}, {"key": "y", "duration": 0.15},
                {"key": "2", "duration": 0.3}, {"key": "e", "duration": 0.3},
                {"key": "y", "duration": 0.3},
            ]
        },

        "Whiplash": { # q = 0.28
            "melody": [
                # brass 1
                {"key": ["x", "o"], "duration": 0.28},
                {"key": ["x", "o"], "duration": 0.14}, {"key": ["x", "o"], "duration": 0.14},
                {"key": ["x", "o"], "duration": 0.28},
                {"key": ["x", "o"], "duration": 0.14}, {"key": ["f", "z"], "duration": 0.28},
                {"key": ["x", "o"], "duration": 0.14},
                {"key": ["x", "o"], "duration": 0.14}, {"key": ["z", "i"], "duration": 0.14},
                {"key": ["x", "o"], "duration": 0.28},
                # piano bass 1
                {"key": "i", "duration": 0.28},
                {"key": "7", "duration": 0.14}, {"key": "6", "duration": 0.14},
                {"key": "t", "duration": 0.28},
                {"key": "q", "duration": 0.14}, {"key": "5", "duration": 0.28},
                {"key": "r", "duration": 0.28},
                {"key": "q", "duration": 0.14}, {"key": "3", "duration": 0.28},
                # brass 2
                {"key": ["x", "o"], "duration": 0.28},
                {"key": ["x", "o"], "duration": 0.14}, {"key": ["x", "o"], "duration": 0.14},
                {"key": ["x", "o"], "duration": 0.28},
                {"key": ["x", "o"], "duration": 0.14}, {"key": ["f", "z"], "duration": 0.28},
                {"key": ["f", "z"], "duration": 0.14},
                {"key": ["x", "o"], "duration": 0.56},
                # piano bass 2
                {"key": "q", "duration": 0.28},
                {"key": "q", "duration": 0.14}, {"key": "w", "duration": 0.14},
                {"key": "3", "duration": 0.28},
                {"key": "r", "duration": 0.14}, {"key": "5", "duration": 0.28},
                {"key": "r", "duration": 0.28},
                {"key": "3", "duration": 0.14}, {"key": "q", "duration": 0.28},
                # brass 3
                {"key": ["x", "o"], "duration": 0.28},
                {"key": ["x", "o"], "duration": 0.14}, {"key": ["x", "o"], "duration": 0.14},
                {"key": ["x", "o"], "duration": 0.28},
                {"key": ["x", "o"], "duration": 0.14}, {"key": ["f", "z"], "duration": 0.28},
                {"key": ["x", "o"], "duration": 0.14},
                {"key": ["x", "o"], "duration": 0.14}, {"key": ["z", "i"], "duration": 0.14},
                {"key": ["x", "o"], "duration": 0.28},
                # piano bass 3
                {"key": "i", "duration": 0.28},
                {"key": "7", "duration": 0.14}, {"key": "6", "duration": 0.14},
                {"key": "t", "duration": 0.28},
                {"key": "q", "duration": 0.14}, {"key": "5", "duration": 0.28},
                {"key": "r", "duration": 0.28},
                {"key": "q", "duration": 0.14}, {"key": "3", "duration": 0.28},
                # brass 4 outro
                {"key": ["x", "o"], "duration": 0.28},
                {"key": ["x", "o"], "duration": 0.14}, {"key": ["x", "o"], "duration": 0.14},
                {"key": ["x", "o"], "duration": 0.28},
                {"key": ["x", "o"], "duration": 0.14}, {"key": ["f", "z"], "duration": 0.28},
                {"key": ["f", "z"], "duration": 0.14},
                {"key": ["x", "o"], "duration": 1.12},
                {"key": ["z", "i"], "duration": 0.14}, {"key": ["x", "o"], "duration": 0.14},
                {"key": ["x", "o"], "duration": 0.14}, {"key": ["z", "i"], "duration": 0.14},
                {"key": ["x", "o"], "duration": 0.14}, {"key": ["f", "z"], "duration": 0.28},
                {"key": ["x", "o"], "duration": 0.14}, {"key": ["f", "z"], "duration": 0.28},
                {"key": ["x", "o", "7"], "duration": 1.12},
            ]
        },

        "Megalovania": {  # q = 0.24
            "melody": [
                {"key": "w", "duration": 0.12}, {"key": "w", "duration": 0.12},
                {"key": "o", "duration": 0.24},
                {"key": "y", "duration": 0.36},
                {"key": "6", "duration": 0.24}, {"key": "t", "duration": 0.24},
                {"key": "r", "duration": 0.24}, {"key": "w", "duration": 0.12},
                {"key": "r", "duration": 0.12}, {"key": "t", "duration": 0.12},
                {"key": "q", "duration": 0.12}, {"key": "q", "duration": 0.12},
                {"key": "o", "duration": 0.24},
                {"key": "y", "duration": 0.36},
                {"key": "6", "duration": 0.24}, {"key": "t", "duration": 0.24},
                {"key": "r", "duration": 0.24}, {"key": "w", "duration": 0.12},
                {"key": "r", "duration": 0.12}, {"key": "t", "duration": 0.12},
                {"key": "u", "duration": 0.12}, {"key": "u", "duration": 0.12},
                {"key": "o", "duration": 0.24},
                {"key": "y", "duration": 0.36},
                {"key": "6", "duration": 0.24}, {"key": "t", "duration": 0.24},
                {"key": "r", "duration": 0.24}, {"key": "w", "duration": 0.12},
                {"key": "r", "duration": 0.12}, {"key": "t", "duration": 0.12},
                {"key": "7", "duration": 0.12}, {"key": "7", "duration": 0.12},
                {"key": "o", "duration": 0.24},
                {"key": "y", "duration": 0.36},
                {"key": "6", "duration": 0.24}, {"key": "t", "duration": 0.24},
                {"key": "r", "duration": 0.24}, {"key": "w", "duration": 0.12},
                {"key": "r", "duration": 0.12}, {"key": "t", "duration": 0.12},
            ]
        },

        "Tetris Korobeiniki": {
            "melody": [ # q = 0.4
                {"key": "p", "duration": 0.4},
                {"key": "u", "duration": 0.2}, {"key": "i", "duration": 0.2},
                {"key": "o", "duration": 0.4},
                {"key": "i", "duration": 0.2}, {"key": "u", "duration": 0.2},
                {"key": "y", "duration": 0.4},
                {"key": "y", "duration": 0.2}, {"key": "i", "duration": 0.2},
                {"key": "p", "duration": 0.4},
                {"key": "o", "duration": 0.2}, {"key": "i", "duration": 0.2},
                {"key": "u", "duration": 0.4},
                {"key": "u", "duration": 0.2}, {"key": "i", "duration": 0.2},
                {"key": "o", "duration": 0.4}, {"key": "p", "duration": 0.4},
                {"key": "i", "duration": 0.4}, {"key": "y", "duration": 0.4},
                {"key": "y", "duration": 1.0},

                {"key": "o", "duration": 0.4}, {"key": "z", "duration": 0.2},
                {"key": "c", "duration": 0.4},
                {"key": "x", "duration": 0.2}, {"key": "z", "duration": 0.2},
                {"key": "p", "duration": 0.6}, {"key": "i", "duration": 0.2},
                {"key": "p", "duration": 0.4},
                {"key": "o", "duration": 0.2}, {"key": "i", "duration": 0.2},
                {"key": "u", "duration": 0.4},
                {"key": "u", "duration": 0.2}, {"key": "i", "duration": 0.2},
                {"key": "o", "duration": 0.4}, {"key": "p", "duration": 0.4},
                {"key": "i", "duration": 0.4}, {"key": "y", "duration": 0.4},
                {"key": "y", "duration": 1.0},
            ],
            "harmony": [
                {"key": "w", "duration": 0.2},
                {"key": ["w", "e", "6"], "duration": 0.4}, {"key": ["w", "e", "6"], "duration": 0.4},
                {"key": ["w", "e", "6"], "duration": 0.4}, {"key": ["w", "e", "6"], "duration": 0.4},
                {"key": ["q", "e", "y"], "duration": 0.4}, {"key": ["q", "e", "y"], "duration": 0.4},
                {"key": ["q", "e", "y"], "duration": 0.4}, {"key": ["q", "e", "y"], "duration": 0.4},
                {"key": ["w", "e", "6"], "duration": 0.4}, {"key": ["w", "e", "6"], "duration": 0.4},
                {"key": ["w", "e", "6"], "duration": 0.4}, {"key": ["w", "e", "6"], "duration": 0.4},
                {"key": ["q", "e", "y"], "duration": 0.4}, {"key": ["q", "e", "y"], "duration": 0.4},
                {"key": ["2", "e", "y"], "duration": 0.4}, {"key": ["2", "e", "y"], "duration": 0.4},
                {"key": ["w", "r", "y"], "duration": 0.4}, {"key": ["w", "r", "y"], "duration": 0.4},
                {"key": ["w", "r", "y"], "duration": 0.4}, {"key": ["w", "r", "y"], "duration": 0.4},
                {"key": ["q", "e", "y"], "duration": 0.4}, {"key": ["q", "e", "y"], "duration": 0.4},
                {"key": ["q", "e", "y"], "duration": 0.4}, {"key": ["q", "e", "y"], "duration": 0.4},
                {"key": ["w", "e", "6"], "duration": 0.4}, {"key": ["w", "e", "6"], "duration": 0.4},
                {"key": ["w", "e", "6"], "duration": 0.4}, {"key": ["w", "e", "6"], "duration": 0.4},
                {"key": ["q", "e", "y"], "duration": 0.4}, {"key": ["q", "e", "y"], "duration": 0.2},
                {"key": ["q", "e", "y"], "duration": 0.4},
            ]
        },
    }

    @classmethod
    def list_songs(cls) -> list:
        return list(cls.songs.keys())

    @classmethod
    def get_song(cls, name: str) -> list | None:
        name_lower = name.lower()
        for key in cls.songs:
            if key.lower() == name_lower:
                return cls.songs[key]
        return None

    @classmethod
    def add_song(cls, name: str, notes: list):
        cls.songs[name.lower()] = notes

# reqs

class SystemList:
    min_req = (
        f"{Fore.BLUE}OS{Style.RESET_ALL}        : {Fore.LIGHTBLUE_EX}Windows 10 / Linux (kernel 4.19+){Style.RESET_ALL}\n"
        f"{Fore.BLUE}CPU{Style.RESET_ALL}       : {Fore.LIGHTBLUE_EX}Single-Core 1.2 GHz (x86-64 or ARM64){Style.RESET_ALL}\n"
        f"{Fore.BLUE}RAM{Style.RESET_ALL}       : {Fore.LIGHTBLUE_EX}128MB free memory{Style.RESET_ALL}\n"
        f"{Fore.BLUE}Storage{Style.RESET_ALL}   : {Fore.LIGHTBLUE_EX}150MB free space (including dependencies){Style.RESET_ALL}\n"
        f"{Fore.BLUE}Python{Style.RESET_ALL}    : {Fore.LIGHTBLUE_EX}3.10+ Python version{Style.RESET_ALL}\n"
    )

    rec_req = (
        f"{Fore.BLUE}OS{Style.RESET_ALL}        : {Fore.LIGHTBLUE_EX}Windows 10 / Linux (kernel 4.19+){Style.RESET_ALL}\n"
        f"{Fore.BLUE}CPU{Style.RESET_ALL}       : {Fore.LIGHTBLUE_EX}Dual-Core 2.0 GHz (Intel 6th Gen){Style.RESET_ALL}\n"
        f"{Fore.BLUE}RAM{Style.RESET_ALL}       : {Fore.LIGHTBLUE_EX}256MB free memory{Style.RESET_ALL}\n"
        f"{Fore.BLUE}Storage{Style.RESET_ALL}   : {Fore.LIGHTBLUE_EX}300MB free space{Style.RESET_ALL}\n"
        f"{Fore.BLUE}Python{Style.RESET_ALL}    : {Fore.LIGHTBLUE_EX}3.13 Python version{Style.RESET_ALL}\n"
    )
