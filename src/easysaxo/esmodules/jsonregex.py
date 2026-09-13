"""JSON/Regex processing for EasySaxo.

Includes:
- JsonData class
- RegexData class
"""

# `jsonregex.py` ONLY FOR JSON AND REGEX COMMANDS
# literally the most useless file ever

import json
import os

from colorama import Fore, Style

from ..config import easysaxo
from .dirloct import DirLocation


class JsonData:
    """Provides utility methods for loading, validating and pretty-printing JSON files."""
    @staticmethod
    def jsonrd(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath)
            if os.path.exists(full_path):
                with open(full_path, "r", encoding="utf-8") as f: print(f"\n--- Formatted JSON ---\n{json.dumps(json.load(f), indent=4)}\n--- End of JSON ---")
                return
            easysaxo.k_log("5")
            print(f"File {Fore.RED}{filepath}{Style.RESET_ALL} does not exist.")
        except (IsADirectoryError, FileNotFoundError, KeyboardInterrupt) as e:
            easysaxo.k_log("5" if isinstance(e, FileNotFoundError) else "f2" if isinstance(e, IsADirectoryError) else "11")
            print(f"{Fore.RED}Error reading JSON: {e}{Style.RESET_ALL}")

import re


class RegexData:
    """Provides pattern-matching utilities for inline strings and text files
    using regular expressions."""
    @staticmethod
    def match_pattern(pattern, text, ignore_case=False):
        try:
            flags = re.IGNORECASE if ignore_case else 0
            compiled = re.compile(pattern, flags)
            matches = compiled.findall(text)
            mode = "case-insensitive" if ignore_case else "case-sensitive"

            if not matches: 
                print(f"{Fore.YELLOW}No matches found for pattern '{pattern}' ({mode}).{Style.RESET_ALL}")
                return
            print(f"Found {Fore.GREEN}{len(matches)}{Style.RESET_ALL} matches of '{pattern}' ({mode}).")
        except (TypeError, ValueError) as e:
            easysaxo.k_log("6")
            print(f"{Fore.RED}Regex matching error: {e}{Style.RESET_ALL}")

    @staticmethod
    def match_file(pattern, filepath, ignore_case=False):
        try:
            full_path = DirLocation._resolve_path(filepath)
            
            if os.path.isdir(full_path):
                print(f"{Fore.RED}'{filepath}' is a directory, not a file.{Style.RESET_ALL}")
                return

            if os.path.exists(full_path):
                with open(full_path, "r", encoding="utf-8") as f: content = f.read()
                RegexData.match_pattern(pattern, content, ignore_case=ignore_case)
                return
            
            easysaxo.k_log("5")
            print(f"File {Fore.RED}{filepath}{Style.RESET_ALL} does not exist.")
        except (TypeError, ValueError, KeyboardInterrupt, PermissionError) as e: 
            easysaxo.k_log("4" if isinstance(e, PermissionError) else "6" if isinstance(e, ValueError or TypeError) else "11")
            print(f"{Fore.RED}Error reading file: {e}{Style.RESET_ALL}")