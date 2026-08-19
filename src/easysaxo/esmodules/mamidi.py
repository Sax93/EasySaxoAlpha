"""MIDI execution holder for EasySaxo"""

# this is gonna be horrendeous

import sys
import time

import numpy as np
import pygame
from colorama import Fore, Style

pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)

class MusicIns:
    @staticmethod
    def p_note(frequencies, duration=0.4):
        if isinstance(frequencies, (int, float)):
            frequencies = [frequencies]

        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration), False)

        wave = np.zeros_like(t)
        for freq in frequencies:
            wave += np.sin(2 * np.pi * freq * t)

        if len(frequencies) > 0:
            wave /= len(frequencies)

        fade = min(int(sample_rate * 0.05), len(wave) // 2)
        env = np.ones(len(wave))
        if fade > 0:
            env[-fade:] = np.linspace(1.0, 0.0, fade)

        buf = (wave * env * 16384).astype(np.int16)
        sound = pygame.mixer.Sound(buffer=buf)
        sound.play()

# song playback support ==============================================================================

import threading


def _play_track(track_notes):
    from .lister import MidiSetList

    for note_entry in track_notes:
        keys = note_entry.get("key", [])
        duration = note_entry.get("duration", 0.4)

        if isinstance(keys, str):
            keys = [keys]

        freqs = []
        for k in keys:
            k_lower = k.lower()
            if k_lower in MidiSetList.note_k_bindings:
                _, freq = MidiSetList.note_k_bindings[k_lower]
                freqs.append(freq)

        if freqs:
            MusicIns.p_note(freqs, duration)

        time.sleep(duration)

def play_song(song_name: str) -> bool:
    from .lister import SongSet

    song_data = SongSet.get_song(song_name)
    if not song_data:
        print(f"{Fore.RED}Song '{song_name}' not found.{Style.RESET_ALL}")
        return False

    draw_piano()
    print(f"Playing: {Fore.CYAN}{song_name}{Style.RESET_ALL}")

    if isinstance(song_data, list):
        song_data = {"track_1": song_data}

    threads = []
    for track_notes in song_data.values():
        t = threading.Thread(target=_play_track, args=(track_notes,), daemon=True)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return True

def prompt_song_selection():
    from .lister import SongSet

    songs = SongSet.list_songs()
    if not songs:
        print(f"{Fore.RED}No songs available.{Style.RESET_ALL}")
        return None

    print(f"\n{Fore.CYAN}Available songs:{Style.RESET_ALL}")
    for i, song_name in enumerate(songs, 1):
        print(f"  {i}. {song_name}")
    print(f"  {Fore.LIGHTBLACK_EX}Enter number or name (or press Enter to cancel): {Style.RESET_ALL}", end="")

    try:
        choice = input().strip()
        if not choice:
            return None

        # Try as number first
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(songs):
                return songs[idx]

        # Try as song name
        if choice.lower() in [s.lower() for s in songs]:
            return choice.lower()

        # Try fuzzy match
        for s in songs:
            if choice.lower() in s.lower():
                return s

        print(f"{Fore.RED}Song '{choice}' not found.{Style.RESET_ALL}")
        return None
    except (EOFError, KeyboardInterrupt):
        return None

def draw_piano(highlight_note=None, mode_info=None):
    print("\033[H\033[J", end="")
    print(f"{Fore.CYAN}=== Piano keyboard mode ==={Style.RESET_ALL}\n"
          f"{Fore.LIGHTBLACK_EX}`Ctrl` + `C` to exit | Press 'M' to play a song{Style.RESET_ALL}\n")

    if mode_info:
        print(f"{Fore.YELLOW}{mode_info}{Style.RESET_ALL}\n")

    b_layer = "  | | 2 | 3 | | | 5 | 6 | 7 | | | 9 | 0 | | | S | D | F | |   |"
    w_layer = "  | Q | W | E | R | T | Y | U | I | O | P | Z | X | C | V | B |"

    if highlight_note:
        b_layer = b_layer.replace(f" {highlight_note} ", f" {Fore.GREEN}{highlight_note}{Style.RESET_ALL} ")
        w_layer = w_layer.replace(f" {highlight_note} ", f" {Fore.GREEN}{highlight_note}{Style.RESET_ALL} ")

    print("  _____________________________________________________________\n"
          "  | |■■■|■■■| | |■■■|■■■|■■■| | |■■■|■■■| | |■■■|■■■|■■■| |   |\n"
          f"{b_layer}\n"
          "  | |■■■|■■■| | |■■■|■■■|■■■| | |■■■|■■■| | |■■■|■■■|■■■| |   |\n"
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
        import select
        import termios
        import tty
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
    from ..config import clr
    from .lister import MidiSetList

    # Flush input buffer before starting
    if sys.platform == 'win32':
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()

    draw_piano()

    while True:
        try:
            key = get_key_nonblocking()

            # Song selection mode
            if key == 'm':
                song_name = prompt_song_selection()
                if song_name:
                    play_song(song_name)
                    draw_piano()

            elif key in MidiSetList.note_k_bindings:
                _note_name, freq = MidiSetList.note_k_bindings[key]
                draw_piano(highlight_note=key.upper())
                MusicIns.p_note(freq)

        except KeyboardInterrupt:
            print(f"{Fore.LIGHTBLACK_EX}Exiting PK.{Style.RESET_ALL}")
            clr()
            break