import threading
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


def _exec(cmd):
    threading.Thread(target=lambda: os.system(cmd)).start()


def setup_win(image_path):
    win = Gtk.Window()

    win.set_type_hint(Gdk.WindowTypeHint.UTILITY)
    win.set_decorated(False)
    win.set_accept_focus(False)
    win.fullscreen()
    win.set_keep_below(True)

    image = Gtk.Image()
    image.set_from_file(image_path)
    win.add(image)

    win.add_events(Gdk.EventMask.SCROLL_MASK)
    win.connect("event", handle)

    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    xid = win.get_window().get_xid()
    return xid


events_pool = []

cmd_up = 'echo mouse scroll up'
cmd_down = 'echo mouse scroll down'
cmd_right = 'echo mouse right button clicked'


def handle(self, event):
    """
    """
    if event.type == Gdk.EventType.SCROLL:
        d = event.get_scroll_direction().direction
        if d == Gdk.ScrollDirection.UP:
            events_pool.append('up')
        elif d == Gdk.ScrollDirection.DOWN:
            events_pool.append('down')
    elif event.type == Gdk.EventType.BUTTON_PRESS:
        b = event.get_button().button
        if b == 1:
            events_pool.append('left')
        if b == 3:
            events_pool.append('right')
    else:
        pass

    if len(events_pool) >= 2:
        if events_pool[0] == events_pool[1] == 'right':
            _exec(cmd_right)
        elif events_pool[0] == events_pool[1] == 'up':
            _exec(cmd_up)
        elif 'up' in events_pool[:2] and 'down' in events_pool[:2]:
            _exec(cmd_down)
        for _ in range(len(events_pool)):
            events_pool.pop()


def loop():
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()


if '__main__' == __name__:
    import sys
    setup_win(sys.argv[1])
    loop()
