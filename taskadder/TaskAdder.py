import os
import tkinter
import tkinter.font
import tkinter.ttk as ttk
from taskadder.kan import Kan

class TaskAdder(tkinter.Frame):
    def __init__(self, parent):
        icon = tkinter.Image('photo', file='icon.png')
        tkinter.Frame.__init__(self,parent)
        self.parent = parent
        self.parent.wm_title("Task Adder")
        self.customFont = tkinter.font.Font(size=24)
        self.parent.call('wm', 'iconphoto', self.parent._w, icon)
        self.initialize()

    def initialize(self):
        self.grid()

        self.taskText = tkinter.StringVar()

        ttk.Style().configure('TEntry', padding=10)
        self.entry = ttk.Entry(
                self,
                width=50,
                textvariable=self.taskText,
                font=self.customFont)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.focus_set()

        self.entry.bind('<Return>', self.onPressReturn)
        self.entry.bind('<Escape>', self.onPressEscape)

    def onPressReturn(self, event):
        Kan().create_task(self.taskText.get())
        self.parent.destroy()

    def onPressEscape(self, event):
        self.parent.destroy()




