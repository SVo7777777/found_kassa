from tkinter import *
import time
from datetime import datetime
import locale
root = Tk()
root.title("Часы")
root.geometry('900x400+20+20')
root['bg'] = 'maroon4'

def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

def data():
    locale.setlocale(locale.LC_ALL, "")
    now = datetime.now()
    data = now.strftime("%d %B %Y (%A)")
    print(data)
    st = data.split()
    print(st)
    if st[1][-1] == 'ь' or st[1][-1] == 'й':
        month = st[1][0:-1].lower() + 'я'
    else:
        month = st[1].lower() + 'я'
    print(month)
    st[1] = month
    print(st)
    data1 = ' '.join(st)
    print(data1)
    now_chek = datetime.now()
    print(now_chek.strftime("%d-%m-%Y"))
    datetime_label.config(text=data1)

time_label = Label(root, bg='maroon4', fg='white', font=("Arial", 158, 'bold'))
time_label.pack()
datetime_label = Label(root, bg='maroon4', fg='white', font=("Arial", 48, 'bold'))
datetime_label.pack()
update_data = Button(root, bg='maroon4', text='обновить дату', fg='white', command=data, font=("Arial", 18, 'bold'))
update_data.pack()
update_time()
data()
root.mainloop()