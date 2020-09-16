import sys
from pathlib import Path
sys.path.append(str(Path.absolute(Path(__file__).resolve().parent.parent) / 'jpSource'))

from jp_speech import *
from time import sleep

# while 1:
    # say("It's time to run some water")
    # minutes = 30
    # sleep(60*minutes)

i = 0
while 1:
    if i % 30 == 0:
        print("it's time to run some water")
        say("it's time to run some water")
        i = 0
    sleep(60)
    i += 1
    print(i)
