import tkinter as tk
from tkinter import ttk

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

        self.input.bind('<Key-Return>', self.print_contents)

    def print_contents(self, event):
        print(self.contents.get())
        self.contents.set('')
        root.destroy()


if __name__=='__main__':
    root = tk.Tk()
    app = TaskAdderWindow(master=root)
    app.mainloop()



