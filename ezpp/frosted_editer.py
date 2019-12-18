#!/usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk, ImageFilter


class Application(tk.Frame):
    def __init__(self, master=None, filename=None):
        super().__init__(master)
        self.master = master
        self.filename = filename
        self.create_widgets()

    def create_widgets_images(self, root):
        self.image = Image.open(self.filename)
        self.imageTK = ImageTk.PhotoImage(self.image)
        self.imgLabel = ttk.Label(root, image=self.imageTK, text='origin')
        self.imgLabel.pack(side="left", fill='x')

        self.imgFrosted = ttk.Label(root, text='forested', compound='image')
        self.imgFrosted.pack(side="right", fill='x')

    def create_widgets_fileinfos(self, root):
        self.fileLabel = ttk.Label(root, text="file:xxx")
        self.fileLabel.pack(side="bottom", anchor='nw')

        self.fileOutputLabel = ttk.Label(root, text="file output :xxx")
        self.fileOutputLabel.pack(side="bottom", anchor='sw')

    def create_widgets_controls(self, root):
        self.blur = 10
        self.mode = 3
        self.sblur = ttk.Scale(root, orient='horizontal',
                               length=600, from_=1.0, to=100.0, command=self.update_blur)
        # pack(side='top', ipadx=10, ipady=10, anchor='center')
        self.lbBlur = ttk.Label(root, text='Blur:')
        self.lbMode = ttk.Label(root, text='Mode:')
        self.rbModeNone = ttk.Radiobutton(
            root, text='None', value=0, command=self.update_modeNone)
        self.mode = tk.StringVar()
        self.rbMode3 = ttk.Radiobutton(
            root, text='3', value=3, command=self.update_mode3)

        self.rbMode5 = ttk.Radiobutton(
            root, text='5', value=5, command=self.update_mode5)

        self.lbBlur.grid(row=0, column=0, ipadx=10, ipady=10)
        self.sblur.grid(row=0, column=1, columnspan=3, ipadx=10, ipady=10)
        self.lbMode.grid(row=1, column=0)
        self.rbModeNone.grid(row=1, column=1)
        self.rbMode3.grid(row=1, column=2)
        self.rbMode5.grid(row=1, column=3)

    def update_mode5(self):
        self.mode = 5
        self.frosted()

    def update_mode3(self):
        self.mode = 3
        self.frosted()

    def update_modeNone(self):
        self.mode = None
        self.frosted()

    def update_blur(self, value):
        self.blur = round(float(value))
        self.frosted()

    def create_widgets(self):

        self.fileinfos_frame = ttk.Frame()
        self.create_widgets_fileinfos(self.fileinfos_frame)
        self.fileinfos_frame.pack(side='top', fill='x')

        self.controls_frame = ttk.Frame()
        self.create_widgets_controls(self.controls_frame)
        self.controls_frame.pack(side='top', fill='x')

        self.images_frame = ttk.Frame()
        self.create_widgets_images(self.images_frame)
        self.images_frame.pack(side='bottom', fill='x')

    def frosted(self):
        print(f"frosted b:{self.blur} m:{self.mode}")
        self.imageFrosted = self.image.filter(
            ImageFilter.GaussianBlur(self.blur))
        if self.mode:
            self.imageFrosted = self.imageFrosted.filter(
                ImageFilter.ModeFilter(self.mode))
        self.imageTKFrosted = ImageTk.PhotoImage(self.imageFrosted)
        self.imgFrosted.config(image=self.imageTKFrosted)


def frosted_editer(filename):
    root = tk.Tk()
    ttk.Style().configure(
        "TButton",
        padding=16,
        relief="flat",
        background="#ccc"
    )
    ttk.Style().configure(
        "TFrame",
        padding=16,
        relief="flat",
        background="#99ff99"
    )
    ttk.Style().configure(
        "TLabel",
        padding=16,
        relief="flat",
        background="#eef"
    )
    app = Application(master=root, filename=filename)
    app.master.title(filename)
    app.master.geometry("1024x768")
    app.mainloop()
