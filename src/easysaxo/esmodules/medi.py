#`medi.py` ONLY FOR MULTIMEDIA FILE HANDLING COMMAND DEFINING

import os

from colorama import Fore, Style

from ..esmodules.dirloct import DirLocation

try: # we are trying to import asciiart here to avoid double check in main file
    from ascii_magic import AsciiArt
    ASCII_AVAILABLE = True
except ImportError: ASCII_AVAILABLE = False

class MediaData:
    pygame_initialized = False

    @staticmethod
    def init_pygame():
        import pygame
        if not MediaData.pygame_initialized:
            os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
            pygame.mixer.init()
            MediaData.pygame_initialized = True
        return pygame

    @staticmethod
    def playaudio(filepath):
        try:
            pygame = MediaData.init_pygame()
            pygame.mixer.music.load(DirLocation._resolve_path(filepath))
            pygame.mixer.music.play()
            print(f"Playing audio: {Fore.GREEN}{filepath}{Style.RESET_ALL}")
        except (FileNotFoundError, PermissionError) as e: print(f"{Fore.RED}Error playing audio file: {e}{Style.RESET_ALL}")

    @staticmethod
    def stopaudio():
        try:
            import pygame
            if MediaData.pygame_initialized and pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
                print(f"{Fore.GREEN}Audio stopped.{Style.RESET_ALL}")
            else: print(f"{Fore.YELLOW}No audio is currently playing.{Style.RESET_ALL}")
        except ImportError as e: print(f"{Fore.RED}Error stopping audio: {e}{Style.RESET_ALL}")
        
    # render area
    @staticmethod
    def render_preset(name):
        import random
        from .builtinrender import Image as bt
        from .lister import ColorList

        attr_name = f"{name.lower()}Logo"
        logo = getattr(bt, attr_name, None)
        
        if logo:
            rancolor = random.choice(ColorList.colors)
            ranfore = getattr(Fore, rancolor)
            print(f"{ranfore}{logo}{Style.RESET_ALL}")
            return True
            
        return False # fallback to file rendering

    @staticmethod
    def render(filepath, colnum=80):
        if not ASCII_AVAILABLE:
            print(f"{Fore.RED}ASCII Art not available.{Style.RESET_ALL}")
            return
            # on top of it all, we check if asciiart is available
            # to avoid errors with the command

        resolved_path = DirLocation._resolve_path(filepath)

        VALID_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.gif')
        if not resolved_path.lower().endswith(VALID_EXTENSIONS):
            print(f"{Fore.RED}Error: Invalid image extension. Supported: {', '.join(VALID_EXTENSIONS)}{Style.RESET_ALL}")
            return

        if not os.path.isfile(resolved_path):
            print(f"{Fore.RED}Error: Image file '{filepath}' not found.{Style.RESET_ALL}")
            return

        try:
            print(f"{Fore.LIGHTMAGENTA_EX}Rendering your image...{Style.RESET_ALL}")
            cols = int(colnum) if str(colnum).isdigit() else 80
            ascii_r = AsciiArt.from_image(resolved_path)
            ascii_r.to_terminal(columns=cols)
        except (ValueError, FileNotFoundError, PermissionError) as e:
            print(f"{Fore.RED}Could not render: {e}{Style.RESET_ALL}")
    
    @staticmethod
    def txt2rt(text):
        try: 
            from art import text2art
        except ImportError:
            print(f"{Fore.RED}Art not available.{Style.RESET_ALL}")
            return
        result = text2art(text)
        print(f"{Fore.CYAN}{result}{Style.RESET_ALL}")
        
    @staticmethod
    def renderbanner(descript):
        import random

        from .builtinrender import TextToImage as tti
        from .lister import ColorList
        
        rancolor = random.choice(ColorList.colors)
        ranfore = getattr(Fore, rancolor)
        attr_name = f"{descript.lower()}Text"
        logo = getattr(tti, attr_name, None)
        if logo:
            print(f"{ranfore}{logo}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Preset text image '{descript}' not found")
        
        
# holy useless code