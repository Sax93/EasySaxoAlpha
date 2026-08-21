"""Easter Egg holder for EasySaxo"""

import os
import random
import sys
import time

from colorama import Fore, Style

from .misc import talk


def eas1():
    from ..commands import c_set
    case_number = random.randint(1, 4)
    match case_number:
        case 1:
            print(f"{Fore.LIGHTBLUE_EX}omg easter egg??/?/?{Style.RESET_ALL}")
            c_set("name lol")
        case 2:
            print(f"{Fore.LIGHTRED_EX}omg easter egg??/?/?{Style.RESET_ALL}")
            c_set("name hehe")
        case 3:
            print(f"{Fore.LIGHTGREEN_EX}omg easter egg??/?/?{Style.RESET_ALL}")
            c_set("name IAmTheKinkiest")
        case 4: # dont stare at me
            print(f"{Fore.LIGHTMAGENTA_EX}tuffest easter egg def{Style.RESET_ALL}")
            c_set("name tuffguy")
            c_set("var tuffvariable 67")
            c_set("var tuffvariable2 41")
        case _: pass

def eas2():
    case_number = random.randint(1, 4)

    match case_number:
        case 1:
            from ..commands import c_filecrt, c_filewrt
            from .lister import EasterList
            print("js use the app bud...")
            c_filecrt("slop.txt")
            c_filewrt(f"slop.txt {random.choice(EasterList.slop)}")

        case 2:
            from .dirloct import DirLocation
            print("Generating your one-use waste of time...")
            time.sleep(random.randint(1, 69))
            if os.name == 'nt':
                if os.path.exists("C:\\Windows"):
                    DirLocation.ls("C:\\Windows")
                    DirLocation.filerd("C:\\Windows\\win.ini")
                    print("interesting info yk")
            else: print("done")

        case 3:
            from ..commands import easysaxo
            do_nothing = easysaxo.name == "EasySaxo"
            if not do_nothing:
                print("Don't move my code buddy")
                easysaxo.name = "EasySaxo"
            else: print(f"you a nice one actually {Fore.GREEN}:){Style.RESET_ALL}")

        case 4:
            from ..commands import easysaxo
            do_nothing = easysaxo.dev == "SXF"
            if not do_nothing:
                talk("who am i then", 1)
                talk("no dont do that", 1)
                talk("no wait", 0.9)
                talk("waait")
                talk("noo", 0.3)
                sys.exit()
            else: talk("im watching you bud", 2)

        case _: pass

def eas4():
    from .dirloct import DirLocation
    talk("the sauce", 0.4)
    talk("flexing")
    talk("no ketchup")
    talk("none")
    talk("just sauce")
    talk("saucy")
    talk("raw sauce")
    talk("bah")
    talk("yo")
    talk("boom")
    talk("ah")
    talk("the thing goes")
    if os.name == 'nt':
        DirLocation.ls("C:\\Windows\\System32")
        DirLocation.ls("C:\\Windows\\SysWOW64")
    elif os.name == 'posix':
        DirLocation.ls("/usr/bin")
        DirLocation.ls("/bin")

def eas5():
    from .lister import EasterList
    from .misc import traceback
    ranerror = random.choice(EasterList.ERRlist)
    traceback(ranerror)

def eas6(question):
    def anser(txt):
        print(f"{Fore.CYAN}{txt}{Style.RESET_ALL}")
    
    import random

    from .lister import EasterList as Ans

    if not question:
        anser("I dont know bru")
        return
    
    if isinstance(question, list):
        question = " ".join(question)
    
    parts = question.strip().split(maxsplit=1)
    first_word = parts[0].lower()
    
    if first_word in ["is", "am", "are", "really"]:
        response = random.choice(Ans.l_is_are)
        anser(response)
    elif first_word == "why":
        response = random.choice(Ans.l_why)
        anser(f"Because {response}")
    elif first_word == "who":
        response = random.choice(Ans.l_who)
        anser(response)
    elif first_word == "what":
        response = random.choice(Ans.l_what)
        anser(response)
    elif first_word == "how":
        response = random.choice(Ans.l_how)
        anser(response)
    else: anser("I dont know bru")