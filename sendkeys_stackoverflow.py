# import sys
# from pathlib import Path
# sys.path.append(str(Path.absolute(Path(__file__).resolve().parent.parent) / "jpSource"))

import pyautogui as auto
# import jp_xlib

# these are necessary due to Linux's keyboard shortcuts bizarre behaviour
auto.keyUp('alt')
auto.keyUp('ctrl')
auto.keyUp('shift')

auto.press('end')
auto.write(' site:stackoverflow.com') # overflow.com')
auto.press('enter')






