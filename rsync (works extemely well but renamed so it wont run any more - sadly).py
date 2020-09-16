import sys
from pathlib import Path
sys.path.append(str(Path.absolute(Path(__file__).resolve().parent.parent) / 'jpSource'))
from jp_date import *
import os
from subprocess import call
from jp_file import slash, program_dir

running_in_vscode = True
if running_in_vscode:
    # source = "/home/john/Documents/PythonCode/"
    source = "/home/john/"
    # dest_root = "/Media/rsync/python_backups/"
    dest_root = "/Media/rsync/home_backups/"
    interval = ""
else:
    source = slash(sys.argv[1])
    dest_root = slash(sys.argv[2])
    if len(sys.argv) == 4:
        interval = sys.argv[3]
    else:
        interval = ""

def backup_folder_name():
    # return to_international_date(now()) + "_" + to_short_time(now(), format="24hr")
    # return to_international_date(now()) + "_" + str(hour(now())) + "_" + str(minute(now()))
    ttime = to_short_time(now(), format="24hr")
    ttime = ttime.replace(':', '-')
    return to_international_date(now()) + "_" + ttime

def get_last_backup():
    """ returns the last backup folder based on the modified time """
    dirs = [dI for dI in os.listdir(dest_root) if os.path.isdir(os.path.join(dest_root,dI))]
    result = ''
    if len(dirs) > 0:
        maxtime = 0.0
        for d in dirs:
            filetime = os.path.getmtime(dest_root + d)
            if filetime > maxtime:
                maxtime = filetime
                result = dest_root + d
    return result

last_backup = get_last_backup()
dest = slash(dest_root) + backup_folder_name()

# the rsync_excludes file is in the program's directory
exclude_str = "--exclude-from=" + program_dir() + "rsync_excludes"

# if first run, just do it
if len(last_backup) == 0:
    call(["rsync", "-a", exclude_str, source, dest])
else:
    if running_in_vscode:
        print('running in vscode')
        call(["rsync", "-a", exclude_str, "--delete", "--link-dest=" + last_backup, source, dest])
        call(["touch", "-m", dest]) # rsync doesn't always update the dest folder's modification time
    else:
        # it's not a first run and we're not running in vscode
        if interval == "--daily":
            if day(now()) != day(from_filetime(os.path.getmtime(last_backup))):
                call(["rsync", "-a", exclude_str, "--delete", "--link-dest=" + last_backup, source, dest])
                call(["touch", "-m", dest]) # rsync doesn't always update the dest folder's modification time
            else:
                pass
        else:
            call(["rsync", "-a", exclude_str, "--delete", "--link-dest=" + last_backup, source, dest])    
            call(["touch", "-m", dest]) # rsync doesn't always update the dest folder's modification time
