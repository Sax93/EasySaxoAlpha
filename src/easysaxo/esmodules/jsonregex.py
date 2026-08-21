"""JSON/Regex processing for EasySaxo"""

# `jsonregex.py` ONLY FOR JSON AND REGEX COMMANDS
# literally the most useless file ever

import json
import os

from colorama import Fore, Style

from ..esmodules.dirloct import DirLocation


class JsonData:
    @staticmethod
    def jsonrd(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath)
            if os.path.exists(full_path):
                with open(full_path, "r", encoding="utf-8") as f:
                    print(f"\n--- Formatted JSON ---\n{json.dumps(json.load(f), indent=4)}\n--- End of JSON ---")
            else: print(f"File {Fore.RED}{filepath}{Style.RESET_ALL} does not exist.")
        except (IsADirectoryError, FileNotFoundError, KeyboardInterrupt) as e:
            print(f"{Fore.RED}Error reading JSON: {e}{Style.RESET_ALL}")

import re


class RegexData:
    @staticmethod
    def match_pattern(pattern, text, ignore_case=False):
        try:
            flags = re.IGNORECASE if ignore_case else 0
            compiled = re.compile(pattern, flags)
            matches = compiled.findall(text)
            mode = "case-insensitive" if ignore_case else "case-sensitive"
            if matches:
                print(f"Found {Fore.GREEN}{len(matches)}{Style.RESET_ALL} matches of '{pattern}' ({mode}).")
            else:
                print(f"{Fore.YELLOW}No matches found for pattern '{pattern}' ({mode}).{Style.RESET_ALL}")
        except (TypeError, ValueError) as e:
            print(f"{Fore.RED}Regex matching error: {e}{Style.RESET_ALL}")

    @staticmethod
    def match_file(pattern, filepath, ignore_case=False):
        try:
            if os.path.exists(filepath):
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                RegexData.match_pattern(pattern, content, ignore_case=ignore_case)
            else:
                print(f"File {Fore.RED}{filepath}{Style.RESET_ALL} does not exist.")
        except (TypeError, ValueError, IsADirectoryError, KeyboardInterrupt) as e:
            print(f"{Fore.RED}Error reading file for regex: {e}{Style.RESET_ALL}")