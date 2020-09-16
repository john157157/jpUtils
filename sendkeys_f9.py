import sys
sys.path.insert(1, "/home/john/Documents/PythonCode/jpSource")
from jp_xlib import *
import pyautogui as auto
import time

# print(active_window_name())
RunInBrowser = False

print('hello vscode')
auto.keyUp('alt')
auto.keyUp('ctrl')
auto.keyUp('shift')
if 'PyCharm' in active_window_name():
    auto.hotkey('ctrl', 's')
    time.sleep(.1)
    if RunInBrowser:
        import sys
        sys.path.insert(1, "/home/john/Documents/PythonCode/jpSource")
        from jp_xlib import *
        x, y = auto.position()
        activate_window('Chrome')
        time.sleep(.25)
        auto.click(87, 19)
        auto.press('f5')
        auto.moveTo(x, y)
    else:
        auto.hotkey('ctrl', 'f2', interval=.05)
        auto.hotkey('ctrl', 'shift', 'f9')
       #  auto.getAllTitles()

if 'Studio' in active_window_name():
    auto.hotkey('ctrl', 's')
    time.sleep(.1)
    if RunInBrowser:
        import sys
        sys.path.insert(1, "/home/john/Documents/PythonCode/jpSource")
        from jp_xlib import *
        x, y = auto.position()
        activate_window('Chrome')
        time.sleep(.25)
        auto.click(87, 19)
        auto.press('f5')
        auto.moveTo(x, y)
    else:
        auto.hotkey('ctrl','alt', 'n')
        # auto.hotkey('ctrl', 'f5')
        # auto.getAllTitles()



