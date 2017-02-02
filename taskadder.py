#!/usr/bin/env python3

import configparser
import tkinter as tk
from tkinter import ttk
from kanboard import Kanboard


class Kan():

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.url = config['auth']['url']
        self.token = config['auth']['token']
        self.project_id = config['auth']['project']
        self.kb = self.auth()

    def auth(self):
        return Kanboard(self.url, 'jsonrpc', self.token)

    def create_task(self, text):
        self.kb.create_task(project_id=self.project_id, title=text)

class TaskAdderWindow(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_input_box()

    def create_input_box(self):

        ttk.Style().configure('TEntry', padding=10)
        self.input = ttk.Entry(width=50)
        self.input.pack()
        self.input.focus_set()

        self.contents = tk.StringVar()
        self.contents.set('')
        self.input['textvariable'] = self.contents

        self.input.bind('<Key-Return>', self.make_task)

    def make_task(self, event):
        k = Kan()
        k.create_task(self.contents.get())
        self.contents.set('')
        root.destroy()


if __name__=='__main__':
    root = tk.Tk()
    app = TaskAdderWindow(master=root)
    app.mainloop()
    k = Kan()



