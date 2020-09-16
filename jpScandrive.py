#!/usr/bin/python3

import sys
from pathlib import Path
sys.path.append(str(Path.absolute(Path(__file__).resolve().parent.parent) / 'jpSource'))
from time import time
from jp_scandir import jp_scandir
from jp_file import slash
# from colorama import init
# from colorama import Fore, Back, Style
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[34m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLACK = '\33[30m'

starttime = time()

help_str = """USAGE: jpScandrive options path google-style-search
eg jpScandrive -R "/Media/DVDs/" "Godfather"

note: path is case sensitive
"""

path = '/Media/Music/'
search_str = "Music"
recursive = True

if len(sys.argv) == 4:
    if sys.argv[1] == "-R":
        recursive = True
    path = slash(sys.argv[2])
    search_str = sys.argv[3]
elif len(sys.argv) == 2:
    print()
    print(help_str)
    exit()



filelist = jp_scandir(path, search_str, recursive=True, want_sorted=True, want_full_path=True)
# print(Fore.BLUE)
for i, f in enumerate(filelist):
    head, tail = os.path.split(f)

    print(bcolors.BLACK + f'{i}:' + bcolors.OKBLUE + head + os.sep + bcolors.BLACK + tail)

print(bcolors.BLACK)
print(f'{len(filelist)} files in {time()-starttime:2.2} seconds')