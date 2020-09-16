"""
Util converts unix style linefeeds in text file(s) to DOS format
USAGE:
    python linefeeds myfile.txt
    python linefeeds *.txt
    python linefeeds *.*
"""

import sys
import glob

num_args = len(sys.argv)
if num_args != 2:
    print("USAGE: linefeeds file_spec (wildcards ok)")
    print("WARNING: file_spec should not include binaries")
else:
    globspec = sys.argv[1]
    files = glob.glob(globspec)
    for filename in files:
        fileContents = open(filename,"r").read()
        f = open(filename,"w", newline="\r\n")
        f.write(fileContents)
        f.close()
