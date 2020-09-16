import sys
from pathlib import Path
sys.path.append(str(Path.absolute(Path(__file__).resolve().parent.parent) / 'jpSource'))
from jp_date import *
import os
from subprocess import call
from jp_file import slash, program_dir
import jp_windows
import jp_stdout
from zipfile import ZipFile


# caller is responsible for getting the source and dest right ie lower_case and ending in '*'
# if "Visual Studio Code" in jp_windows.active_window_name():
    # source = "c:\\docs\\damon john\\*"
# else:
    # source = '' # sys.argv[1]


source = os.getcwd()

def get_all_py_files(source): 
  
    # initializing empty file paths list 
    file_paths = [] 
  
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(source): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            if filename.endswith(".py"):
                filepath = os.path.join(root, filename) 
                file_paths.append(filepath) 
  
    # returning all file paths 
    return file_paths         
  

# for root, dirs, files in os.walk(source):
#     for file in files:
#         if file.endswith(".py"):
#             # print(os.path.join(root, file))
#             p = os.path.join(root, file)
#             print(p)
#             print(Path(p).parent)
#             print(Path(p).parts[-2])
#             # part = os.path.dirname(os.path.abspath(file))
#             # print(part.parent)
#             # print(Path(file).parent)


file_paths = get_all_py_files(source)
# print(file_paths)
for file in file_paths:
    print(file)

print()
print(source)
zip_filename = Path(source).parts[-1] + '.zip'

if os.path.exists(zip_filename):
    os.remove(zip_filename)

with ZipFile(zip_filename,'w') as zip: 
        # writing each file one by one 
        for file in file_paths: 
            zip.write(file) 
  











# if first run, just do it
# if len(last_backup) == 0:
#     call(["rsync", "-a", exclude_str, source, dest])
# else:
#     if running_in_vscode:
#         print('running in vscode')
#         call(["rsync", "-a", exclude_str, "--delete", "--link-dest=" + last_backup, source, dest])
#         call(["touch", "-m", dest]) # rsync doesn't always update the dest folder's modification time
#     else:
#         # it's not a first run and we're not running in vscode
#         if interval == "--daily":
#             if day(now()) != day(from_filetime(os.path.getmtime(last_backup))):
#                 call(["rsync", "-a", exclude_str, "--delete", "--link-dest=" + last_backup, source, dest])
#                 call(["touch", "-m", dest]) # rsync doesn't always update the dest folder's modification time
#             else:
#                 pass
#         else:
#             call(["rsync", "-a", exclude_str, "--delete", "--link-dest=" + last_backup, source, dest])    
#             call(["touch", "-m", dest]) # rsync doesn't always update the dest folder's modification time




# this is useful if I decide to include the time in the backup folder name
# def backup_folder_name():
#     # return to_international_date(now()) + "_" + to_short_time(now(), format="24hr")
#     # return to_international_date(now()) + "_" + str(hour(now())) + "_" + str(minute(now()))
#     ttime = to_short_time(now(), format="24hr")
#     ttime = ttime.replace(':', '-')
#     return to_international_date(now()) + "_" + ttime

# I don't think I need this
# def get_last_backup():
#     """ returns the last backup folder based on the modified time """
#     dirs = [dI for dI in os.listdir(dest_root) if os.path.isdir(os.path.join(dest_root,dI))]
#     result = ''
#     if len(dirs) > 0:
#         maxtime = 0.0
#         for d in dirs:
#             filetime = os.path.getmtime(dest_root + d)
#             if filetime > maxtime:
#                 maxtime = filetime
#                 result = dest_root + d
#     return result



# and I don't think I need all this stuff
# if "Visual Studio Code" in jp_windows.active_window_name()
    # running_in_vscode = True
# else:
    # running_in_vscode = False

# directory strategy:
#   user passes in the source dir eg:
#       1. c:\docs
#       2. c:\docs\pythoncode
#       3. c:\users\john
#   code uses an ifelse construct to build the dest
# if running_in_vscode:
    # source = "c:\\docs\\pythoncode\\"
    # source = "c:\\docs\\"
    # source = "c:\\users\\john\\"

    # python_dest = "e:\\backups_python\\" + to_international_date(now())
    # docs_dest = "e:\\backups_docs\\" + to_international_date(now())
    # users_john_dest = "e:\\backups_users_john\\" + to_international_date(now())
    # interval = ""
# else:
    # source = slash(sys.argv[1])
    # dest_root = slash(sys.argv[2])
    # if len(sys.argv) == 4:
        # interval = sys.argv[3]
    # else:
        # interval = ""


