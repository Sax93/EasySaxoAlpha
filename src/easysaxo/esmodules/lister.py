from colorama import Fore, Style
from ..config import easysaxo
import random

# add big lists here. remember to use 'from .esmodules.lister import ...'

# easter egg lists ================================================================================
ERRlist = [ # from eas5()
    f"NotAnError{Style.RESET_ALL}: {Fore.MAGENTA}Seemingly, there was no error at all",
    f"ConfidenceError{Style.RESET_ALL}: {Fore.MAGENTA}There was an error, but it was not confident enough to show up",
    f"NonsenseError{Style.RESET_ALL}: {Fore.MAGENTA}There is not an error, against all odds",
    f"MissClickError{Style.RESET_ALL}: {Fore.MAGENTA}My bad, bro, I thought there was an error",
    f"OutOfHardwareError{Style.RESET_ALL}: {Fore.MAGENTA}The error is far out of the hardware (it is the developer)",
    f"AstigmatismError{Style.RESET_ALL}: {Fore.MAGENTA}There was an error, but I lost it from sight",
    f"CentralProcessingUnitError{Style.RESET_ALL}: {Fore.MAGENTA}Python detected your CPU is too trash to run the error",
    f"SentimentalError{Style.RESET_ALL}: {Fore.MAGENTA}The error remembered things from the past, and decided not to show up",
    f"ConsciousnessError{Style.RESET_ALL}: {Fore.MAGENTA}The error suddenly remembered there was no reason to raise an exception",
    f"PythonChallengeToGeminiError{Style.RESET_ALL}: {Fore.MAGENTA}Python is so busy fighting Gemini that the error did not show up",
    f"InsufficentGravityError{Style.RESET_ALL}: {Fore.MAGENTA}Python detected local gravity is off. Please put your feet on the floor again to continue",
    f"DeepDiskError{Style.RESET_ALL}: {Fore.MAGENTA}Disk/drive failed while trying to save the promises that were not going to happen",
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
    f"MathUselessInformationError{Style.RESET_ALL}: {Fore.MAGENTA}Byte order of the app is not a Mersenne prime number"
]

slop = [ # from eas2()
    "fuck you", 
    "use command 'filecls python' please", 
    "if your reading ts your a dumbahh",
    "hi", 
    "type c for fast charging", 
    "use 'filedel C:\\Windows\\System32' now", 
    "get back to work kink",
    f"{random.randint(1, 65566)}"
]

osaka = [ # from e3()
        "sataa andagi", "omaiga", "amerikaya",
        "haro everynyan", "get yo ahh to work bud", "haiii"
    ]

# command list ===================================================================================
CMDlist = (
    f"{Fore.CYAN}COMMAND LIST: {Style.RESET_ALL}\n"
    f"{Fore.BLUE}help{Style.RESET_ALL}        : Access to {Fore.CYAN}Command List{Style.RESET_ALL} and description.\n"
    f"{Fore.BLUE}news{Style.RESET_ALL}        : Shows the lastest {Fore.CYAN}app updates{Style.RESET_ALL}.\n"
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
    f"{Fore.BLUE}filelst{Style.RESET_ALL}     : Lists files and folders in a directory.\n"
    f"{Fore.BLUE}filecrt{Style.RESET_ALL}     : Creates a {Fore.RED}file{Style.RESET_ALL} with specified extension.\n"
    f"{Fore.BLUE}filerd{Style.RESET_ALL}      : Reads and displays the content of a {Fore.RED}file{Style.RESET_ALL}.\n"
    f"{Fore.BLUE}filedel{Style.RESET_ALL}     : Deletes a {Fore.RED}file{Style.RESET_ALL}.\n"
    f"{Fore.BLUE}filewrt{Style.RESET_ALL}     : Writes over a {Fore.RED}file{Style.RESET_ALL}.\n"
    f"{Fore.BLUE}fileopn{Style.RESET_ALL}     : Opens a {Fore.RED}file{Style.RESET_ALL}.\n"
    f"{Fore.BLUE}filecls{Style.RESET_ALL}     : Closes a {Fore.RED}file{Style.RESET_ALL}.\n"
    f"{Fore.BLUE}jsonrd{Style.RESET_ALL}      : Reads a {Fore.RED}JSON file{Style.RESET_ALL}.\n"
    f"{Fore.BLUE}regex{Style.RESET_ALL}       : Looks for {Fore.GREEN}patterns{Style.RESET_ALL} in a text or textfile.\n"
    f"{Fore.BLUE}playaudio{Style.RESET_ALL}   : Plays an {Fore.RED}audio file{Style.RESET_ALL} (specify the route).\n"
    f"{Fore.BLUE}stopaudio{Style.RESET_ALL}   : Stops the current {Fore.RED}audio file{Style.RESET_ALL}.\n"
    f"{Fore.BLUE}render{Style.RESET_ALL}      : Renders and draws a specified {Fore.RED}image file{Style.RESET_ALL} (specify route).\n"
    f"{Fore.BLUE}banner{Style.RESET_ALL}      : Renders and prints inputted {Fore.GREEN}text{Style.RESET_ALL}.\n"
    f"{Fore.BLUE}pkm{Style.RESET_ALL}         : Enters the {Fore.CYAN}Piano Keyboard Mode{Style.RESET_ALL} (experimental).\n"
    f"{Fore.BLUE}unins{Style.RESET_ALL}       : Guides to uninstall {Fore.LIGHTRED_EX}{easysaxo.name}{Style.RESET_ALL}.\n"
    f"{Fore.BLUE}boot{Style.RESET_ALL}        : Auto-checks if {Fore.LIGHTRED_EX}app{Style.RESET_ALL} has all recourses, as a reboot.\n"
    f"{Fore.BLUE}exit{Style.RESET_ALL}        : Exit {Fore.CYAN}{easysaxo.name}{Style.RESET_ALL}.\n"
    f"\nRemember you can search for command's syntax and usage by using {Fore.GREEN}help <cmd/attr>{Style.RESET_ALL} :)"
)

# render list ====================================================================================
RENlist = [
    "SXF",
    "EASYSAXO",
    "PYTHON",
    "LINUX", "TUX",
    "LOSS",
    "WINDOWS",
    "GITHUB",
]

# dirlocation list ===============================================================================

# from allowance
files_to_allow = [
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

# math lists =====================================================================================
import math, ast, operator

MATHSET_HELP = {
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

mathset = {
    "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, 
    "tan": math.tan, "log": math.log, "log10": math.log10, 
    "abs": abs, "pi": math.pi, "e": math.e, "fact": math.factorial,
    "gamma": math.gamma,
}

_reserved = {
    "sqrt", "sin", "cos",
    "tan", "log", "log10",
    "abs", "pi", "e", "fact",
    "gamma"
}

_allowed_operators = {
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

# misc lists ======================================================================================

# modlist
required_modules = [
    "os", "sys", "re", "time", "subprocess", "platform", "random", "locale",
    "psutil", "json", "math", "pygame", "threading", "socket", "colorama", "rich", "prompt_toolkit",
    "cpuinfo", "importlib", "ascii_magic"
]

# unins (files)
files_to_delete = [
    "config.py", "session.json", "translations.json", 
    "main.py", "commands.py"
]

# colorama color list ==============================================================================

colors = [
    "RED", "BLUE", "GREEN", "BLACK", "MAGENTA", "YELLOW", "CYAN", "WHITE",
    "LIGHTRED_EX", "LIGHTBLUE_EX", "LIGHTGREEN_EX", "LIGHTBLACK_EX",
    "LIGHTMAGENTA_EX", "LIGHTYELLOW_EX", "LIGHTCYAN_EX", "LIGHTWHITE_EX"
]

# mamidi ============================================================================================

note_freqs = {
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

note_k_bindings = {
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