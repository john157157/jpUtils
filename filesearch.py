import sys
sys.path.insert(1, "c:\\docs\\pythoncode\\jpSource")
from jp_scandir import *
import os


print()
print()
print()
print('************************** results **********************************')
# print(f'len(sys.argv) = {len(sys.argv)}')

if len(sys.argv) == 1:
    # print('USAGE: scandir "needle needle2 -antineedle..." [--recursive] ')
    print('USAGE: dirscan [-r] "needle needle2 -antineedle..."')
    print('(-r if you want recursive)')
    os._exit(0)

if sys.argv[1].find('-r') != -1:
    recursive = True
else:
    recursive = False






search_str = sys.argv[len(sys.argv) - 1]

files = scandir_filtered(os.getcwd(), search=search_str, recursive=recursive)
print()
for f in files:
    print(f)

print(f'{len(files)} files found')
'''
    :param path
    :param search
    :param recursive: (default=False)
    :param want_sorted: (default=True)
    :param want_full_path: (default=False EXCEPT when recursive=True, then full_path is automatic)
'''
