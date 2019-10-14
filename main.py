"""
"""
import os.path
import time
import sys

import glob, random
from ewmh import EWMH

from helper.gtk import setup_win, loop
import helper.gtk as helper

ewmh = EWMH()
disp = ewmh.display

lst = glob.glob('./cropped/*.png')
lst.sort()

def setup_win(workspace_id, image_path):
    xid = helper.setup_win(image_path)
    name = os.path.split(image_path)[1].replace(' ', '')

    win_x = disp.create_resource_object("window", xid)
    ewmh.setWmDesktop(win_x, workspace_id)
    win_x.set_wm_class('notile', 'notile')


ci = ewmh.getCurrentDesktop()
wins = []
for i in range(ewmh.getNumberOfDesktops()):
    if i == ci:
        continue
    setup_win(i, lst[i])
setup_win(ci, lst[ci])

disp.flush()

helper.loop()
