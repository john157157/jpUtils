
"""
Corrected, the thread stops now.
"""

import sys
import os
import PIL
from PIL import Image
# import PIL.Image # python-imaging
from PIL import ImageStat # python-imaging
import Xlib.display # python-xlib

from time import sleep

import gtk
gtk.gdk.threads_init()

import threading

# uses the package python-xlib
# from http://snipplr.com/view/19188/mouseposition-on-linux-via-xlib/
# or: sudo apt-get install python-xlib
from Xlib import display


old_stdout = sys.stdout
sys.stdout = open(os.devnull, 'w')

mouseX = 0
mouseY = 0

def mousepos():
    """mousepos() --> (x, y) get the mouse coordinates on the screen (linux, Xlib)."""
    data = display.Display().screen().root.query_pointer()._data
    mouseX = data["root_x"]
    mouseY = data["root_y"]
    return data["root_x"], data["root_y"]


class MouseThread(threading.Thread):
    def __init__(self, parent, label, jplabel):
        threading.Thread.__init__(self)
        self.label = label
        self.jplabel = jplabel
        self.killed = False

    def run(self):
        try:
            while True:
                if self.stopped():
                    break
                text = "{0}".format(mousepos())
            
                self.label.set_text("x, y: " + text)
                x, y = mousepos()
                self.jplabel.set_text("rgb: " + get_pixel_colour(x,y))#   mousepos()[0], [1]))
                sleep(0.01)
        except (KeyboardInterrupt, SystemExit):
            sys.exit()

    def kill(self):
        self.killed = True

    def stopped(self):
        return self.killed

def get_pixel_colour(i_x, i_y):
	# import PIL.Image # python-imaging
	# import PIL.ImageStat # python-imaging
	# import Xlib.display # python-xlib
	o_x_root = Xlib.display.Display().screen().root
	o_x_image = o_x_root.get_image(i_x, i_y, 1, 1, Xlib.X.ZPixmap, 0xffffffff)
	o_pil_image_rgb = PIL.Image.frombytes("RGB", (1, 1), o_x_image.data, "raw", "BGRX")
	lf_colour = PIL.ImageStat.Stat(o_pil_image_rgb).mean
	return str(tuple(map(int, lf_colour)))
 
print get_pixel_colour(0, 0)


class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Mouse coordinates 0.1")
        self.set_size_request(250, 60)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", self.quit)

        label = gtk.Label()
        jplabel = gtk.Label()
        self.mouseThread = MouseThread(self, label, jplabel)
        self.mouseThread.start()

        fixed = gtk.Fixed()
        fixed.put(label, 10, 10)
        
        # jplabel.set_text('hello world')
        jplabel.set_text(str(get_pixel_colour(mouseX, mouseY)))
        jptemp = gtk.Fixed()
        fixed.put(jplabel, 10, 40)

        self.add(fixed)
        self.show_all()

    def quit(self, widget):
        self.mouseThread.kill()
        gtk.main_quit()


if __name__ == '__main__':
    app = PyApp()
    gtk.main()