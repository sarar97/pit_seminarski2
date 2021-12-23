import math
from tkinter.ttk import Label, Button
from tkinter import *
from PIL import Image, ImageTk


class Slika(Frame):

    def __init__(self, nazivSlike):
        super().__init__()
        try:
            self.naziv = nazivSlike
            self.imgObj = Image.open(nazivSlike)

        except IOError:
            print("Unable to load image ", nazivSlike)
            sys.exit(1)
        self.prikazi()

    def logTransform(self, c, f):
        g = c * math.log(float(1 + f), 10)
        return g

    def logTransformImage(self, image, var):
        var = int(var)
        c = var / math.log(var + 1, 10)
        for i in range(0, image.size[0] - 1):
            for j in range(0, image.size[1] - 1):
                f = image.getpixel((i, j))
                redPixel = round(self.logTransform(c, f[0]))
                greenPixel = round(self.logTransform(c, f[1]))
                bluePixel = round(self.logTransform(c, f[2]))
                image.putpixel((i, j), (redPixel, greenPixel, bluePixel))

        return image

    def prikaziLogSliku(self, arg):
        slika = Image.open(self.naziv)
        transformisanaSlika = self.logTransformImage(slika, arg)
        logImg = ImageTk.PhotoImage(transformisanaSlika)
        labelLogSlika = Label(self, image=logImg)
        labelLogSlika.image = logImg
        labelLogSlika.grid(row=5, column=2)

    def prikazi(self):
        slika = ImageTk.PhotoImage(self.imgObj)
        label = Label(self, image=slika)
        label.image = slika
        label.grid(row=5, column=1)
        varLogVrednost = StringVar()
        Label(self, text="Unesite vrednost logaritamske funkcije: ", font='Helvetica 10 bold').grid(row=1, column=1)
        Spinbox(self, from_=1, to=255, textvariable=varLogVrednost).grid(row=2, column=1)
        btn = Button(self, text="Log transformacija", command=lambda: self.prikaziLogSliku(varLogVrednost.get()),
                     font='Helvetica 10 bold', bg='powderblue')
        btn.grid(row=3, column=1, pady=5)
        self.grid(row=1, column=1, columnspan=2)

# root = Tk()
# root.geometry('1200x800')
# tp = Slika('cat.png')
# # tss.setGeometry(300, 300)
# root.mainloop()
