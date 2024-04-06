from tkinter import *
from tkinter import ttk, messagebox, filedialog
import math
import datetime
from tkcalendar import Calendar, DateEntry
import re
import random
try:
    import tkinter as tk
    from tkinter import ttk
    from tkinter import scrolledtext

except ImportError:
    import Tkinter as tk
    import ttk
def total_buyers():
    wind = Tk()
    wind.title('КАЛЕНДАРЬ СОБЫТИЙ В 2023 ГОДУ')
    wind.geometry('970x310+150+50')
    wind['bg'] = 'DarkViolet'  # 'Goldenrod'
    # wind.attributes("-topmost", True)
    import datetime
    today = datetime.date.today()
    currentDay = today.day
    currentMonth = today.month
    currentYear = today.year
    mindate = datetime.date(year=2018, month=1, day=21)
    maxdate = today + datetime.timedelta(weeks=500)
    print(mindate, maxdate)
    cal = Calendar(wind, font="Arial 7", selectmode='day', locale='ru_RU',
                   mindate=mindate, maxdate=maxdate, disabledforeground='blue', background="blue",
                   foreground="white",
                   selectbackground="blue",
                   normalbackground="PeachPuff",
                   weekendbackground="Purple",
                   weekendforeground="white",
                   cursor="hand1", year=currentYear, month=currentMonth, day=currentDay)
    # cal.pack(fill="both", expand=True)
    # cal.grid((row=0, column=0)
    cal.place(x=520, y=10)
    # текущая дата всегда выделена
    today_date = datetime.date(year=currentYear, month=currentMonth, day=currentDay)
    cal.calevent_create(today_date, 'Hello World', 'today_date')
    cal.tag_config('today_date', background='blue', foreground='white')
    text = tk.Text(wind, width=30, height=11, bg="PaleGreen", font=('Arial', 16, 'bold'),
                   fg='Maroon', wrap=tk.WORD)
    #text.place(x=10, y=10)
    ##Label(wind, text='Количество покупателей:',  bg='Goldenrod', bd=0, fg='white',
          #font=('Arial', 18, 'bold')).place(x=10, y=280)

    text2 = tk.Text(wind, width=25, height=8, bg="PeachPuff", font=('Arial', 10, 'bold'),
                    fg='Maroon', wrap=tk.WORD)
    text2.place(x=10, y=5)
    text2.focus()
    i_cheki = Button(wind, text='внести', width=12,  bd=1, bg='Purple', fg='white',
                     font=('Arial', 8, 'bold'))
    i_cheki.place(x=10, y=410)
    look = Button(wind, text='проссмотреть', width=10, bd=1, bg='Purple', fg='white',
                  font=('Arial', 8, 'bold'))
    look.place(x=590, y=340)
    found = Entry(wind, width=12, bd=1, fg='Purple', bg='white',
                   font=('Arial', 10, 'bold'))
    found.place(x=5, y=350)
    found_ = Button(wind, text='поиск по словам', width=12, bd=1, bg='Purple', fg='white',
                   font=('Arial', 8, 'bold'))
    found_.place(x=270, y=340)

    sbros = Button(wind, text='сброс', width=12, bd=1, bg='Purple', fg='white',
                   font=('Arial', 8, 'bold'))
    sbros.place(x=270, y=410)
    kn = Button(wind, text='по дате', width=10, bd=1, bg='Purple', fg='white',
                font=('Arial', 8, 'bold'))
    kn.place(x=590, y=410)
    def found_words():
        data = found.get()
        text2.delete('1.0', END)
        with open('dnevnik.txt', 'r') as f:
            all = f.read()
            sp_all = all.splitlines()
            for i in range(len(sp_all)):
                s = re.search(data, sp_all[i])
                if s:
                    text2.insert(END, sp_all[i] + "\n")

    found_.config(command=found_words)
    def look_date(data):
        ne_sobirali = True
        with open('dnevnik.txt', 'r') as f:
            all = f.read()
            sp_all = all.splitlines()
            for i in range(len(sp_all)):
                s = re.search(data, sp_all[i])
                if s:
                    ne_sobirali = False
                    #text2.delete('1.0', END)
                    text2.insert(END, sp_all[i][12:] +' ')
                    #break
        if ne_sobirali:
            text2.delete('1.0', END)
            text2.insert('1.0', 'нет записей в этот день')

    def look_col():
        text2.delete('1.0', END)
        with open('dnevnik.txt', 'r') as f:
            fi = f.read()
            text2.insert('1.0', fi)

    look.config(command=look_col)

    def sbrosit():
        text2.delete('1.0', END)

    sbros.config(command=sbrosit)

    def vivod(data):
        # global not_sale
        text2.focus()
        text2.insert('1.0', data + ': ')

        def save_col(d):
            # text2.delete('1.0', END)
            s = text2.get('1.0', END)
            print('длина строки: ', len(s))
            print(text2.get('1.0', END))
            if len(s) <= 12:
                messagebox.showwarning('предупреждение!!!',
                                       'действие выполнить невозможно!!!\nсделайте запись!!!')
            else:
                with open('dnevnik.txt', 'a+') as f:
                    f.write(s)
                    messagebox.showinfo('внимание!!!',
                                        'запись внесена!!!')

        i_cheki.config(command=lambda: save_col(data))

    def update_text(event):
        text.delete('1.0', END)
        text2.delete('1.0', END)

        cal.config(selectbackground="red")
        data = str(cal.selection_get())
        print('выбранная дата : ', data)
        new_data_format = data[8:10] + '-' + data[5:7] + '-' + data[0:4]
        print(new_data_format)

        vivod(new_data_format)
        kn.config(command=lambda: look_date(new_data_format))

    cal.bind("<<CalendarSelected>>", update_text)
    wind.mainloop()
# создаём меню
total_buyers()