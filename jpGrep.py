#!/usr/bin/python3

import sys
from pathlib import Path
sys.path.append(str(Path.absolute(Path(__file__).resolve().parent.parent) / 'jpSource'))
from time import time
from jp_scandir import jp_scandir
from pprint import pprint
from jp_file import *
from collections import namedtuple
from os import lstat


starttime = time()

Rec = namedtuple('Rec' , 'fullpath hits')
inodes = set()
needle_bearing_files = {}

# this won't work as-is
# in a gui, it doesn't matter that an inode can have multiple links and only one needs to be changed
# every file containing the search text needs to (optionally) do the find/replace
def find_in_file(path, needle):
    """ returns lists of (line_num, path) tuples """
    # inode has already been checked so we know we need to gather data
    result = Rec(fullpath=path, hits=[])
    contents = slurp_text_file(path)
    if needle in contents:
        content_lines = contents.split('\n')
        for i, l in enumerate(content_lines):
            if needle in l:
                result.hits.append((i))
    return result






# # this is slighter faster but the previous routine is more flexible
# def find_in_file(path, needle):
#     """ returns lists of (line_num, path) tuples """
#     result = []
#     content_lines = read_text_file(path)
#     # if needle in contents:
#     # content_lines = contents.split('\n')
#     print('---------------')
#     print(path)
#     for i, l in enumerate(content_lines):
#         if needle in l:
#             result.append((i, path))
#             print(f'{i} {l}')
#     return result

 
if __name__ == "__main__":
    print('start')
    folder = '/home/john/Documents/PythonCode'
    mask = '.py -pyc -pyd -whl -pyz -pyw'
    if len(sys.argv) == 2:
        needle = sys.argv[1]
    else:
        needle = 'expand='
    # 
    print(f'looking for {needle} in {folder}')
    filelist = jp_scandir(folder, mask, recursive=True, want_sorted=False, want_full_path=True)
    # hits = []
    for i, f in enumerate(filelist):
        inode = lstat(f).st_ino
        if not inode in inodes:
            inodes.add(inode)
            # find_in_file(f, needle, inode)
            fif = find_in_file(f, needle)
            if len(fif.hits) != 0:
                needle_bearing_files[inode] = find_in_file(f, needle)

        # hits.extend(find_in_file(f, needle))
    pprint(needle_bearing_files)
    print(f'{len(needle_bearing_files)} files in {time()-starttime} seconds')



# inodes = {}
# rec = Rec('temp', [])
# rec.hits.append(1)
# inodes[333] = rec
# rec = Rec('wonder', [])
# rec.hits.append(9)
# inodes[444] = rec
# inodes[123456] = Rec('fullpath1', [1,2,3])
# 
# for k,v in inodes.items():
    # print(k,v.hits)


# pprint(inodes)
