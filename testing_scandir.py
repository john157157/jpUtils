import sys
from pathlib import Path
sys.path.append(str(Path.absolute(Path(__file__).resolve().parent.parent) / 'jpSource'))
from time import time
from jp_scandir import jp_scandir
from pprint import pprint
from jp_file import *

starttime = time()
print()

def find_in_file(path, needle):
    """ returns lists of (line_num, path) tuples """
    result = []
    contents = slurp_text_file(path)
    if needle in contents:
        content_lines = contents.split('\n')
        print('---------------')
        print(path)
        for i, l in enumerate(content_lines):
            if needle in l:
                result.append((i, path))
                print(f'{i} {l}')
    return result

fullpaths are dict keys, each holding a list of tuples of file details
dict key: myfile1.py: value: dict with path as a key
                        value: (size?, inode?, idate,)
                      ]
     key: myfile2.py: [
                        value: (size?, inode?, idate)
                        value: (size?, inode?, idate)
                      ]  



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

 

folder = '/home/john/Documents/PythonCode'
mask = '.py -pyc -pyd -whl -pyz'
needle = 'django'

filelist = jp_scandir(folder, mask, recursive=True, want_sorted=False, want_full_path=True)
hits = []
for i, f in enumerate(filelist):
    hits.extend(find_in_file(f, needle))
    # print(f'{i+1}: {f}')

# for h in hits:
    # print(f'{h[0]} {h[1]}')



print(f'elapsed time: {time()-starttime}')