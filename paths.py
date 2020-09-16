import os
import sys


"""
Prints the PATH environmental varible as a list of strings
Can be redirected to a txt file

USAGE:
    python paths
    python paths > paths.txt
"""

pathlist = os.environ.get('path').split(';')

print('  Paths')
print('-----------')
for p in pathlist:
    print(p)


print()
print()
print('   python\'s sys.path')
print('-----------')
for s in sys.path:
    print(s)
print()

# Note: changing Python's path requires
# 1. changing the PYTHON_HOME environmental variable
# 2. changing the PYTHONPATH environmental variable
# 3. (with administrator privileges) change the ftype for the file association

os.system("Pause")
