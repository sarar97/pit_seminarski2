from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Label, Button
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Polinom(Frame):

    def __init__(self):
        super().__init__()
        self.prikazi()

    def func(self, k5, k4, k3, k2, k1, k0, x):
        return k5 * x ** 5 + k4 * x ** 4 + k3 * x ** 3 + k2 * x ** 2 + k1 * x + k0

    def plot(self, k5, k4, k3, k2, k1, k0, i, u):
        if k5 == '' or k4 == '' or k3 == '' or k2 == '' or k1 == '' or k0 == '' or i == '' or u == '':
            messagebox.showwarning("OBAVEŠTENJE", "Niste uneli potrebne parametre")
        else:
            i, u = int(i), int(u)
            # x = np.linspace(i, u, 100)
            x = np.arange(i, u, 0.0001)
            k5, k4, k3, k2, k1, k0 = int(k5), int(k4), int(k3), int(k2), int(k1), int(k0)
            y = self.func(k5, k4, k3, k2, k1, k0, x)
            # y = k5 * x ** 5 + k4 * x ** 4 + k3 * x ** 3 + k2 * x ** 2 + k1 * x + k0

            fig = plt.figure(figsize=(4, 3))
            plot = fig.add_subplot(111)
            plt1 = FigureCanvasTkAgg(fig, self)
            plot.plot(x, y, color='r')
            plt1.get_tk_widget().grid(row=1, column=3, rowspan=10, padx=15)
            
    def prikazi(self):
        sK5 = StringVar()
        Label(self, text="Najveci koeficijent reda 5: ", font='Helvetica 10 bold').grid(row=1, column=1)
        Entry(self, textvariable=sK5, width=10).grid(row=1, column=2)

        sK4 = StringVar()
        sK4.set(0)
        Label(self, text="Najveci koeficijent reda 4: ", font='Helvetica 10 bold').grid(row=2, column=1)
        Entry(self, textvariable=sK4, width=10).grid(row=2, column=2)

        sK3 = StringVar()
        sK3.set(0)
        Label(self, text="Najveci koeficijent reda 3: ", font='Helvetica 10 bold').grid(row=3, column=1)
        Entry(self, textvariable=sK3, width=10).grid(row=3, column=2)

        sK2 = StringVar()
        sK2.set(1)
        Label(self, text="Najveci koeficijent reda 2: ", font='Helvetica 10 bold').grid(row=4, column=1)
        Entry(self, textvariable=sK2, width=10).grid(row=4, column=2)

        sK1 = StringVar()
        sK1.set(0)
        Label(self, text="Najveci koeficijent reda 1: ", font='Helvetica 10 bold').grid(row=5, column=1)
        Entry(self, textvariable=sK1, width=10).grid(row=5, column=2)

        sK0 = StringVar()
        sK0.set(0)
        Label(self, text="Slobodan član: ", font='Helvetica 10 bold').grid(row=6, column=1)
        Entry(self, textvariable=sK0, width=10).grid(row=6, column=2)

        sDonjiInteval = StringVar()
        sDonjiInteval.set(-10)
        Label(self, text="Donji interval: ", font='Helvetica 10 bold').grid(row=7, column=1)
        Entry(self, textvariable=sDonjiInteval, width=10).grid(row=7, column=2)

        sGornjiInterval = StringVar()
        sGornjiInterval.set(10)
        Label(self, text="Gornji interval: ", font='Helvetica 10 bold').grid(row=8, column=1)
        Entry(self, textvariable=sGornjiInterval, width=10).grid(row=8, column=2)

        plotBtn = Button(master=self, text="Plot",  # font='Helvetica 10 bold', bg='powderblue',
                         command=lambda: self.plot(sK5.get(), sK4.get(), sK3.get(), sK2.get(), sK1.get(), sK0.get(),
                                                   sDonjiInteval.get(), sGornjiInterval.get()))
        plotBtn.grid(row=10, column=2)

        rezBisekcije = StringVar()
        Label(self, text="Rezultat bisekcije: ", font='Helvetica 10 bold').grid(row=11, column=1)
        Label(self, text=rezBisekcije.get(), font='Helvetica 10 bold').grid(row=11, column=2)

        self.grid(row=1, column=1, columnspan=3)

# root = Tk()
# root.geometry('1200x800')
# tp = Polinom()
# # tss.setGeometry(300, 300)
# root.mainloop()
