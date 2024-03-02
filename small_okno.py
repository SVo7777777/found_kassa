from tkinter import *
from tkinter import ttk, messagebox, filedialog
import math
import datetime
#from digital_keyboard import klava
from buyers_sales import total_buyers
import os
import random
try:
    import tkinter as tk
    from tkinter import ttk
    from tkinter import scrolledtext

except ImportError:
    import Tkinter as tk
    import ttk
win = Tk()
win.title("Paзрешение")
win.geometry("600x250+5+5")
dirname, filename = os.path.split(os.path.realpath(__file__))
l = Label(win, text="Введите код доступа: ")
l.place(x=5, y=10)
e = Entry(win)
e.place(x=5, y=50)
lv = Label(win)
buyers = False
def vvod(event):
    if e.get() == 'fazenda':
        if buyers:
            win.destroy()
            total_buyers()

        else:
            print('Welcome..!!!')
            os.startfile(dirname + '\\kalkulator.txt')
            win.destroy()
    else:
        lv.config(text='Неверный пароль!!!')
        lv.place(x=5, y=50)
        print('Код неверный..!!!')
e.bind('<Return>', vvod)
win.mainloop()