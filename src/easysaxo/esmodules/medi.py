"""Multimedia handler for EasySaxo."""

import os

from rich import print

from ..config import easysaxo
from ..esmodules.dirloct import DirLocation


class MediaData:
    """Multimedia handler/operator set (Audio and ASCII Render)."""
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
            print(f"Playing audio: [green]{filepath}[/green]")
        except (FileNotFoundError, PermissionError) as e: 
            easysaxo.k_log("5" if isinstance(e, FileNotFoundError) else "4")
            print(f"[red]Error playing audio file: {e}[/red]")

    @staticmethod
    def stopaudio():
        try:
            import pygame
            if MediaData.pygame_initialized and pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
                print("[green]Audio stopped.[/green]")
            else: print("[yellow]No audio is currently playing.[/yellow]")
        except (ImportError, OSError, KeyboardInterrupt) as e: 
            easysaxo.k_log("10" if not isinstance(e, KeyboardInterrupt) else "11")
            print(f"[red]Error stopping audio: {e}[/red]")
        
    @staticmethod
    def render_preset(name):
        from .builtinrender import Image as bt

        attr_name = f"{name.lower()}Logo"
        logo = getattr(bt, attr_name, None)

        if logo:
            print(logo)
            return True

        return False

    @staticmethod
    def render(filepath, colnum=80):
        try:
            from ascii_magic import AsciiArt
        except ImportError:
            print("[red]ASCII Art not available.[/red]")
            return

        resolved_path = DirLocation._resolve_path(filepath)

        VALID_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.gif')
        if not resolved_path.lower().endswith(VALID_EXTENSIONS):
            easysaxo.k_log("f1")
            print(f"[red]Error: Invalid image extension. Supported: {', '.join(VALID_EXTENSIONS)}[/red]")
            return

        if not os.path.isfile(resolved_path):
            easysaxo.k_log("5")
            print(f"[red]Error: Image file '{filepath}' not found.[/red]")
            return

        try:
            print("[magenta]Rendering your image...[/magenta]")
            cols = int(colnum) if str(colnum).isdigit() else 80
            ascii_r = AsciiArt.from_image(resolved_path)
            ascii_r.to_terminal(columns=cols)
        except (ValueError, FileNotFoundError, PermissionError, KeyboardInterrupt) as e:
            easysaxo.k_log("5" if isinstance(e, FileNotFoundError) else "4" if isinstance(e, PermissionError) else "6" if isinstance(e, ValueError) else "11")
            print(f"[red]Could not render: {e}[/red]")
    
    @staticmethod
    def txt2rt(text):
        try: 
            from art import text2art
        except ImportError:
            easysaxo.k_log("9")
            print("[red]Art not available.[/red]")
            return
        result = text2art(text)
        print(f"[cyan]{result}[/cyan]")

    @staticmethod
    def renderbanner(descript):
        from .builtinrender import TextToImage as tti
        attr_name = f"{descript.lower()}Text"
        logo = getattr(tti, attr_name, None)
        if logo: print(logo)
        else: print(f"[red]Preset text image '{descript}' not found[/red]")