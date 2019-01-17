#!/usr/bin/env python3

"""
Python GUI Programming with Tkinter
by Alan D. Moore
Packt Publishing, May 2018 (ISBN: 9781788835886)

Introduction to Tkinter > Creating a Tkinter Hello World

https://learning.oreilly.com/library/view/python-gui-programming/9781788835886/f699d30a-6fe2-409c-8502-d33cbdfed4b8.xhtml
"""


import tkinter as tk
from tkinter import ttk


class HelloView(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # label
        name_label = ttk.Label(self, text="Name:")
        name_label.grid(row=0, column=0, sticky=tk.W)

        # edit box
        self.name = tk.StringVar()
        name_entry = ttk.Entry(self, textvariable=self.name)
        name_entry.grid(row=0, column=1, sticky=(tk.W + tk.E))

        # button
        chg_button = ttk.Button(self, text="Change", command=self.on_change)
        chg_button.grid(row=0, column=2, sticky=tk.E)

        # label
        self.hello_string = tk.StringVar()
        self.hello_string.set("Hello World")
        hello_label = ttk.Label(self, textvariable=self.hello_string, font=("TkDefaultFont", 64), wraplength=600)
        hello_label.grid(row=1, column=0, columnspan=3)

        self.columnconfigure(1, weight=1)

    def on_change(self):
        if self.name.get().strip():
            self.hello_string.set("Hello " + self.name.get())
        else:
            self.hello_string.set("Hello World")


class MyApplication(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Hello Tkinter")
        self.geometry("800x600")
        self.resizable(width=False, height=False)

        HelloView(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()
