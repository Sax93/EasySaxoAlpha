#=================================================
# JSON and Regex Processing
#=================================================

# `jsonregex.py` ONLY FOR JSON AND REGEX COMMANDS
# literally the most useless file ever

from ..esmodules.dirloct import DirLocation
import os
from colorama import Fore, Style

import json
class JsonData:
    @staticmethod
    def jsonrd(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath)
            if os.path.exists(full_path):
                with open(full_path, "r", encoding="utf-8") as f:
                    print(f"\n--- Formatted JSON ---\n{json.dumps(json.load(f), indent=4)}\n--- End of JSON ---")
            else: print(f"File {Fore.RED}{filepath}{Style.RESET_ALL} does not exist.")
        except Exception as e: print(f"{Fore.RED}Error reading JSON: {e}{Style.RESET_ALL}")
        
import re
class RegexData:
    @staticmethod
    def match_pattern(pattern, text):
        try:
            matches = re.findall(pattern, text)
            if matches: 
                print(f"Found {Fore.GREEN}{len(matches)}{Style.RESET_ALL} matches of '{pattern}'.")
            else: 
                print(f"{Fore.YELLOW}No matches found for pattern '{pattern}'.{Style.RESET_ALL}")
        except Exception as e: 
            print(f"{Fore.RED}Regex matching error: {e}{Style.RESET_ALL}")

    @staticmethod
    def match_file(pattern, filepath):
        try:
            if os.path.exists(filepath):
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                RegexData.match_pattern(pattern, content)
            else:
                print(f"File {Fore.RED}{filepath}{Style.RESET_ALL} does not exist.")
        except Exception as e:
            print(f"{Fore.RED}Error reading file for regex: {e}{Style.RESET_ALL}")