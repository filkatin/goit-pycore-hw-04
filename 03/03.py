# python -m venv .venv
# .\.venv\Scripts\activate
# pip list
# pip install colorama
# pip freeze > 03_requirements.txt
# deactivate
# python 03.py ./

import sys
import os
import pathlib
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_directory_structure(path, indent=''):
    try:
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_dir():
                    print(f"{indent}{Fore.BLUE}{entry.name}/")
                    print_directory_structure(entry.path, indent + '    ')
                elif entry.is_file():
                    print(f"{indent}{Fore.GREEN}{entry.name}")
    except PermissionError:
        print(f"{indent}{Fore.RED}Permission denied: {path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_directory>")
        sys.exit(1)
    #path = pathlib.Path(__file__).parent
    path = Path(sys.argv[1])

    if not path.exists():
        print(f"{Fore.RED}Error: The path '{path}' does not exist.")
        sys.exit(1)
    
    if not path.is_dir():
        print(f"{Fore.RED}Error: The path '{path}' is not a directory.")
        sys.exit(1)
    
    print(f"{Fore.CYAN}Directory structure of '{path}':")
    print_directory_structure(path)

if __name__ == "__main__":
    main()