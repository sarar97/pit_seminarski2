import tkinter
from slika import Slika
from polinom import Polinom

top = tkinter.Tk()
top.title('Programiranje u integrisanim tehnologijama - kolokvijum 2')
top.geometry('1200x800')

tp = Polinom()
tp.grid(row=1, column=1)
tss = Slika('cat.png')
tss.grid(row=2, column=1)

top.mainloop()
