# this is gonna be horrendeous

import sys, pygame
import numpy as np
from .lister import note_freqs, note_k_bindings
from colorama import Fore, Style

pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)

class MusicIns:
    def p_note(frequency, duration = 0.4):
        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        wave = np.sin(2 * np.pi * frequency * t)
        
        fade = int(sample_rate * 0.05)
        env = np.ones(len(wave))
        env[-fade:] = np.linspace(1.0, 0.0, fade)
        
        buf = (wave * env * 16384).astype(np.int16)
        sound = pygame.mixer.Sound(buffer=buf)
        sound.play()
    
def draw_piano(highlight_note=None):
    print("\033[H\033[J", end="")
    print(f"{Fore.CYAN}=== Piano keyboard mode ==={Style.RESET_ALL}\n"
          f"{Fore.LIGHTBLACK_EX}`Ctrl` + `C` to exit PK mode.{Style.RESET_ALL}\n")
    
    b_layer = "    | 2 | 3 |   | 5 | 6 | 7 |   | 9 | 0 |   | S | D | F |   "
    w_layer = "  | Q | W | E | R | T | Y | U | I | O | P | Z | X | C | V | B |"
    
    if highlight_note:
        b_layer = b_layer.replace(f" {highlight_note} ", f" {Fore.GREEN}{highlight_note}{Style.RESET_ALL} ")
        w_layer = w_layer.replace(f" {highlight_note} ", f" {Fore.GREEN}{highlight_note}{Style.RESET_ALL} ")
            
    print("      #   #       #   #   #       #   #       #   #   #\n"
          f"{b_layer}\n"
          "    |___|___|   |___|___|___|   |___|___|   |___|___|___|\n"
          f"{w_layer}\n"
          "  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |\n"
          "  | C4| D | E | F | G | A | B | C5| D | E | F | G | A | B | C6|\n"
          "  |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|\n"
          )
    
def get_key_nonblocking():
    if sys.platform == 'win32':
        import msvcrt
        if msvcrt.kbhit():
            return msvcrt.getch().decode('utf-8', errors='ignore').lower()
    else:
        import tty, termios, select
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
            if rlist:
                return sys.stdin.read(1).lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return None
    
def run_piano():
    draw_piano()
    while True:
        try:
            key = get_key_nonblocking()
            if key in note_k_bindings:
                note_name, freq = note_k_bindings[key]
                draw_piano(highlight_note=key.upper())
                MusicIns.p_note(freq)
        except KeyboardInterrupt:
            print(f"{Fore.LIGHTBLACK_EX}Exiting PK.{Style.RESET_ALL}")
            break