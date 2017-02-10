#!/usr/bin/env python3

import tkinter
from taskadder.TaskAdder import TaskAdder

def main():
    root = tkinter.Tk()
    app = TaskAdder(root)
    root.eval('tk::PlaceWindow %s center' \
            % root.winfo_pathname(root.winfo_id()))
    root.attributes('-alpha', 0.9)
    app.mainloop()
