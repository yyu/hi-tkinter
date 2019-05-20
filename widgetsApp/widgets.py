#!/usr/bin/env python3


import tkinter as tk
from tkinter import ttk


class HelloView(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        row = 0

        # radio button
        self.radio_var = tk.StringVar()
        self.radio_var.set('radio1')
        self.radio1 = ttk.Radiobutton(self, text="radio 1", variable=self.radio_var, value="radio1")
        self.radio2 = ttk.Radiobutton(self, text="radio 2", variable=self.radio_var, value="radio2")
        self.radio1.grid(row=row, column=1, sticky=tk.W)
        self.radio2.grid(row=row, column=2, sticky=tk.W)

        row += 1

        # spinbox
        self.spinbox_var = tk.IntVar()
        self.spinbox_var.set(3)
        self.spinbox1 = ttk.Spinbox(self, textvariable=self.spinbox_var, from_=1, to=10)
        self.spinbox1.grid(row=row, column=1, sticky=tk.W)

        row += 1

        # drop down list
        self.dropdown_options = ['spring', 'summer', 'autumn', 'winter']
        self.dropdown_var = tk.StringVar()
        self.dropdown1 = ttk.OptionMenu(self, self.dropdown_var, 'winter', *self.dropdown_options)
        self.dropdown1.grid(row=row, column=1, sticky=tk.W)

        row += 1

        # label
        label1 = ttk.Label(self, text="label1:")
        label1.grid(row=row, column=0, sticky=tk.W)

        # entry
        self.entry1_string = tk.StringVar()
        self.entry1_string.set("entry-1")
        entry1 = ttk.Entry(self, textvariable=self.entry1_string)
        entry1.grid(row=row, column=1, sticky=(tk.W + tk.E))

        row += 1

        # label
        label2 = ttk.Label(self, text="label2:")
        label2.grid(row=row, column=0, sticky=tk.W)

        # entry
        self.entry2_string = tk.StringVar()
        self.entry2_string.set("entry-2")
        entry2 = ttk.Entry(self, textvariable=self.entry2_string)
        entry2.grid(row=row, column=1, sticky=(tk.W + tk.E))

        row += 1

        # label
        self.label2_string = tk.StringVar()
        self.label2_string.set("Hello World")
        label2 = ttk.Label(self, textvariable=self.label2_string, font=("TkDefaultFont", 22), wraplength=500)
        label2.grid(row=row, column=0, columnspan=3)

        row += 1

        # button
        button1 = ttk.Button(self, text="button1", command=self.on_button1)
        button1.grid(row=row, column=2, sticky=tk.E)

        row += 1

        # button
        button2 = ttk.Button(self, text="button2", command=self.on_button2)
        button2.grid(row=row, column=2, sticky=tk.E)

        row += 1

        ##################################################

        self.columnconfigure(1, weight=1)


    def on_button1(self):
        if self.entry1_string.get().strip():
            self.label2_string.set("Hello " + self.entry1_string.get() + "; " +
                    self.radio_var.get() + "; " +
                    str(self.spinbox_var.get()) + "; " +
                    self.dropdown_var.get()
            )
        else:
            self.label2_string.set("Hello World")

    def on_button2(self):
        from tkinter.filedialog import askopenfilename # see lib/python3.7/tkinter/filedialog.py
        filename = askopenfilename()
        print('"%s"' % filename)
        if filename:
            self.entry1_string.set(filename)


class MyApplication(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Hello Tkinter")
        #self.geometry("800x600")
        self.resizable(width=False, height=False)

        HelloView(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = MyApplication()
    #img = tk.PhotoImage(file="robot.gif")
    #app.tk.call('wm', 'iconphoto', app._w, img)
    app.mainloop()
