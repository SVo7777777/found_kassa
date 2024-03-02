# Importing tkinter module
# and all functions
from tkinter import *
from tkinter.ttk import *

# creating master window
master = Tk()


# This method is used to get
# the name of the widget
# which currently has the focus
# by clicking Mouse Button-1

def pri():
    print('hello')
def focus(event):
    widget = master.focus_get()
    print(widget, "has focus")
    print(widget.nametowidget(widget))#имя виджета
    print(sp.index(str(widget.nametowidget(widget))))#индекс в списке имен
    print(sp[sp.index(str(widget.nametowidget(widget)))+1])#следующий в списке имён
    n = sp[sp.index(str(widget.nametowidget(widget)))+1]
    widget.bind('<Return>', lambda e: (master.nametowidget(n).focus(), pri()))#переход фокуса в следующий энтри


slo = {}
sp = []
# Entry widget
e1 = Entry(master, name='e1')
sp.append(str(e1))
slo[str(e1)] = 'e1'

e1.pack(expand=1, fill=BOTH)
e12 = Entry(master, name='e12')
sp.append(str(e12))
slo[str(e12)] = 'e12'
e12.pack(expand=1, fill=BOTH)
e13 = Entry(master, name='e13')
sp.append(str(e13))
slo[str(e13)] = 'e13'
e13.pack(expand=1, fill=BOTH)
e14 = Entry(master, name='e14')
sp.append(str(e14))
slo[str(e14)] = 'e14'
e14.pack(expand=1, fill=BOTH)
#print(slo)
print(sp)
# Button Widget
e2 = Button(master, text="Button")
e2.pack(pady=5)

# Radiobutton widget
e3 = Radiobutton(master, text="Hello")
e3.pack(pady=5)
Label(master, text="Label1").pack()
label2 = Label(master, name="name", text="Label2")

label2.pack()
# Here function focus() is binded with Mouse Button-1
# so every time you click mouse, it will call the
# focus method, defined above
master.bind_all("<Button-1>", lambda e: focus(e))
print(master.children.values())
print(master.winfo_children())
print(master.nametowidget('.name'))
print(str(e2))
Button(master, text="Delete label2", command=lambda: master.nametowidget(".name").destroy()).pack()

# infinite loop
mainloop()