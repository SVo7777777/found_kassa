from tkinter import *
from tkinter import ttk, messagebox, filedialog
import math
def klava():
    root =Tk()
    root.title("цифровая клавиатура")
    root.geometry("340x465+840+52")#1300x460+200+2; 1500x600+5+5
    root['bg'] = 'orange'
    root.overrideredirect(0)
    root.attributes("-topmost", True)
    root.resizable()
    root.option_add("*tearOff", FALSE)
    def discount(n):
        try:
            widget = root.focus_get()
            print(widget, "has focus")
            print(n)
            #widget.insert('0', n)
            name = widget.nametowidget(widget)
            print(widget.nametowidget(widget))#имя виджета
            root.nametowidget(name).insert(END, n)
            '''print(names_entry.index(str(widget.nametowidget(widget))))#индекс в списке имен
            print(names_entry[names_entry.index(str(widget.nametowidget(widget)))+1])#следующий в списке имён
            n = names_entry[names_entry.index(str(widget.nametowidget(widget)))+1]'''
        except ValueError:
            print('это не  энтри')
    e1 = Entry(root, width=5 )
    e1.place(x=1, y=10)
    e2 = Entry(root, width=5 )
    e2.place(x=40, y=10)
    e3 = Entry(root, width=5 )
    e3.place(x=80, y=10)
    num_1 = Button(root, text='1', width=4, height=2, fg='white',bg='blue',command=lambda: discount(1), bd=2, font=('Arial', 25, 'bold'))
    num_1.place(x=5, y=40)
    num_2 = Button(root, text='2', width=4, height=2, fg='white',bg='blue', command=lambda: discount(2), bd=2, font=('Arial', 25, 'bold'))
    num_2.place(x=95, y=40)
    num_3 = Button(root, text='3', width=4, height=2, fg='white',bg='blue', command=lambda: discount(3), bd=2, font=('Arial', 25, 'bold'))
    num_3.place(x=185, y=40)
    num_4 = Button(root, text='4', width=4, height=2, fg='white',bg='blue',command=lambda: discount(4), bd=2, font=('Arial', 25, 'bold'))
    num_4.place(x=5, y=145)
    num_5 = Button(root, text='5', width=4, height=2, fg='white',bg='blue', command=lambda: discount(5), bd=2, font=('Arial', 25, 'bold'))
    num_5.place(x=95, y=145)
    num_6 = Button(root, text='6', width=4, height=2, fg='white',bg='blue', command=lambda: discount(6), bd=2, font=('Arial', 25, 'bold'))
    num_6.place(x=185, y=145)
    num_7 = Button(root, text='7', width=4, height=2, fg='white',bg='blue',command=lambda: discount(7), bd=2, font=('Arial', 25, 'bold'))
    num_7.place(x=5, y=250)
    num_8 = Button(root, text='8', width=4, height=2, fg='white',bg='blue', command=lambda: discount(8), bd=2, font=('Arial', 25, 'bold'))
    num_8.place(x=95, y=250)
    num_9 = Button(root, text='9', width=4, height=2, fg='white',bg='blue', command=lambda: discount(9), bd=2, font=('Arial', 25, 'bold'))
    num_9.place(x=185, y=250)
    num_0 = Button(root, text='0', width=15, height=1, fg='white',bg='blue',command=lambda: discount(0), bd=2, font=('Arial', 26, 'bold'))
    num_0.place(x=5, y=355)
    num_b = Button(root, text='bs', width=2, height=4, fg='white',bg='blue', command=lambda: dele(), bd=2, font=('Arial', 26, 'bold'))
    num_b.place(x=275, y=40)
    num_e = Button(root, text='en', width=2, height=3, fg='white',bg='blue', command=lambda: entr(15), bd=2, font=('Arial', 26, 'bold'))
    num_e.place(x=275, y=201)
    root.mainloop()
#klava()
