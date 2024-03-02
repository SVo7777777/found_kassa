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
    wind.geometry('970x610+150+50')
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
    cal = Calendar(wind, font="Arial 14", selectmode='day', locale='ru_RU',
                   mindate=mindate, maxdate=maxdate, disabledforeground='blue', background="blue",
                   foreground="white",
                   selectbackground="blue",
                   normalbackground="PeachPuff",
                   weekendbackground="Purple",
                   weekendforeground="white",
                   cursor="hand1", year=currentYear, month=currentMonth, day=currentDay)
    # cal.pack(fill="both", expand=True)
    # cal.grid((row=0, column=0)
    cal.place(x=585, y=10)
    # текущая дата всегда выделена
    today_date = datetime.date(year=currentYear, month=currentMonth, day=currentDay)
    cal.calevent_create(today_date, 'Hello World', 'today_date')
    cal.tag_config('today_date', background='blue', foreground='white')
    '''text = tk.Text(wind, width=76, height=9, bg="PeachPuff", font=('Arial', 14, 'bold'),
                   fg='Maroon', wrap=tk.WORD)'''
    text = scrolledtext.ScrolledText(wind, width=75, height=9, bg="PeachPuff", font=('Arial', 14, 'bold'),
                                     fg='Maroon', wrap=tk.WORD)
    text.place(x=10, y=380)
    ##Label(wind, text='Количество покупателей:',  bg='Goldenrod', bd=0, fg='white',
          #font=('Arial', 18, 'bold')).place(x=10, y=280)

    text2 = tk.Text(wind, width=47, height=10, bg="PeachPuff", font=('Arial', 16, 'bold'),
                    fg='Maroon', wrap=tk.WORD)
    text2.place(x=10, y=50)
    text2.focus()
    i_cheki = Button(wind, text='внести', width=13,  bd=1, bg='Purple', fg='white',
                     font=('Arial', 12, 'bold'))
    i_cheki.place(x=10, y=10)
    look = Button(wind, text='проссмотреть', width=13, bd=1, bg='Purple', fg='white',
                  font=('Arial', 12, 'bold'))
    look.place(x=290, y=10)
    found = Entry(wind, width=15, bd=1, fg='Purple', bg='white',
                   font=('Arial', 15, 'bold'))
    found.place(x=600, y=260)
    found_ = Button(wind, text='поиск по словам', width=15, bd=1, bg='Purple', fg='white',
                   font=('Arial', 12, 'bold'))
    found_.place(x=780, y=260)

    sbros = Button(wind, text='сброс', width=13, bd=1, bg='Purple', fg='white',
                   font=('Arial', 12, 'bold'))
    sbros.place(x=150, y=10)
    kn = Button(wind, text='по дате', width=13, bd=1, bg='Purple', fg='white',
                font=('Arial', 12, 'bold'))
    kn.place(x=430, y=10)
    kn00 = Button(wind, text='add', width=9, bd=1, bg='Purple', fg='white',
                 font=('Arial', 12, 'bold'))
    kn00.place(x=860, y=310)
    kn0 = Button(wind, text='save', width=9, bd=1, bg='Purple', fg='white',
                 font=('Arial', 12, 'bold'))
    kn0.place(x=860, y=345)
    kn1 = Button(wind, text='вывод', width=9, bd=1, bg='Purple', fg='white',
                    font=('Arial', 12, 'bold'))
    kn1.place(x=860, y=380)
    kn2 = Button(wind, text='сброс', width=9, bd=1, bg='Purple', fg='white',
                 font=('Arial', 12, 'bold'))
    kn2.place(x=860, y=420)
    kn3 = Button(wind, text='look', width=9, bd=1, bg='Purple', fg='white',
                 font=('Arial', 12, 'bold'))
    kn3.place(x=860, y=460)
    kn4 = Button(wind, text='', width=9, bd=1, bg='Purple', fg='white',
                 font=('Arial', 12, 'bold'))
    kn4.place(x=860, y=500)
    kn5 = Button(wind, text='', width=9, bd=1, bg='Purple', fg='white',
                 font=('Arial', 12, 'bold'))
    kn5.place(x=860, y=540)
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
                    text2.delete('1.0', END)
                    text2.insert('1.0', sp_all[i])
                    break
        if ne_sobirali:
            text2.delete('1.0', END)
            text2.insert('1.0', 'нет записей в этот день')

    def look_col(t):
        text2.delete('1.0', END)
        if t == 1:
            with open('dnevnik.txt', 'r') as f:
                fi = f.read()
                text2.insert('1.0', fi)
        elif t == 0:
            with open('dnevnik3.txt', 'r') as f:
                fi = f.read()
                text2.insert('1.0', fi)
        else:
            with open('dnevnik2.txt', 'r') as f:
                fi = f.read()
                text.insert('1.0', fi)

    look.config(command=lambda: look_col(1))

    def sbrosit(t):
        if t == 1:
            text2.delete('1.0', END)
        else:
            text.delete('1.0', END)

    sbros.config(command=lambda: sbrosit(1))
    kn2.config(command=lambda: sbrosit(2))
    def vivod(data):
        # global not_sale
        text2.focus()
        text2.insert('1.0', data + ': ')
        ent[0, 0].delete('0', END)
        ent[0, 0].insert('0', data[0:10])

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
                    f.write(s + '\n')
                    messagebox.showinfo('внимание!!!',
                                        'запись внесена!!!')

        i_cheki.config(command=lambda: save_col(data))

    def update_text(event):
        #text.delete('1.0', END)
        text2.delete('1.0', END)

        cal.config(selectbackground="red")
        data = str(cal.selection_get())
        print('выбранная дата : ', data)
        new_data_format = data[8:10] + '-' + data[5:7] + '-' + data[0:4]
        print(new_data_format)

        vivod(new_data_format)
        kn.config(command=lambda: look_date(new_data_format))

    cal.bind("<<CalendarSelected>>", update_text)

# создаём меню
    lab = {}
    ent = {}
    names_entry = []
    def fix():
        for j in range(8):

            lab[(0, j)] = Button(wind, width=12, bg='white', fg='darkred', justif="left",
                                 font=('Arial', 10, 'bold'), text='%')#+ '/' + '%s' % j)
            lab[0, j].place(x=105*j+15, y=320)
            ent[(0, j)] = Entry(wind, width=11, bg='white', name='e'+str(0)+str(j), fg='Black', justif="center",
                                font=('Arial', 13, 'bold'))  # + '/' + '%s' % j)
            ent[0, j].place(x=105 * j + 15, y=345)
            names_entry.append(str(ent[0, j]))
            if j == 0:
                lab[0, j].config(text='дата', justif="left")
            if j == 1:
                lab[0, j].config(text='название')
            if j == 2:
                lab[0, j].config(text='посев')
            if j == 3:
                lab[0, j].config(text='пикировка')
            if j == 4:
                lab[0, j].config(text='черенкование')
            if j == 5:
                lab[0, j].config(text='высадка')
            if j == 6:
                lab[0, j].config(text='стрижка')
            if j == 7:
                lab[0, j].config(text='чистка')

    fix()
    def save():
        for j in range(8):
            el = ent[0, j].get()
            with open('dnevnik2.txt', 'a+') as f, open('dnevnik3.txt', 'a+') as fi:
                if el == '-':
                    if j == 7:
                        f.write('         ' + el + '          ')
                    else:
                        f.write('         ' + el + '          |')
                elif el == '+':
                    if j == 7:
                        f.write('         ' + el + '         ')
                    else:
                        f.write('         ' + el + '         |')
                elif len(el) == 5:
                    f.write(el + '          |')#10 пробелов
                elif len(el) == 6:
                    f.write(el + '        |')#8 пробелов
                elif len(el) == 7:
                    f.write(el + '      |') #6 пробелов
                elif len(el) == 8:
                    f.write(el + '    |')#4 пробелов
                elif len(el) == 9:
                    f.write(el + '  |')#2 пробелов
                else:
                    f.write(el + '|')
                fi.write(el + '|')
        with open('dnevnik2.txt', 'a+') as f:
                f.write('\n')
        messagebox.showinfo('сохранение', "строка успешно сохранена!")
    def add():
        sp = []
        name = ent[0, 1].get()
        sp.append(name + ': ')
        for j in range(2, 8):
            el = ent[0, j].get()
            if el == '+':
                el = lab[0, j]['text']
                sp.append(el + ',')
            elif el != '-' and el != ' ' and el != '':
                el1 = lab[0, j]['text']
                el2 = ent[0, j].get()
                sp.append(el1 + '-' + el2 + ',')
        print(sp)
        line = ' '.join(sp)
        line = line[:-1]
        print(line)
        text2.insert(END, line + '; ')

    kn00.config(command=add)
    kn0.config(command=save)
    kn1.config(command=lambda: look_col(2))
    kn3.config(command=lambda: look_col(0))
    def focus1(t):
        try:
            widget = wind.focus_get()
            print(widget, "has focus")
            #print(t)
            #print(widget.nametowidget(widget))  # имя виджета
            #print(names_entry.index(str(widget.nametowidget(widget))))  # индекс в списке имен
            i = names_entry.index(str(widget.nametowidget(widget)))
            if i == 7:
                n = '.e00'
                print(n)  # следующий в списке имён
            else:
                print(names_entry[names_entry.index(str(widget.nametowidget(widget))) + 1])  # следующий в списке имён
                n = names_entry[names_entry.index(str(widget.nametowidget(widget))) + 1]
            widget.bind('<Return>', lambda e: (wind.nametowidget(n).focus(), focus1(t)))  # переход фокуса в следующий энтри
        except ValueError:
            print('это не  энтри')

    wind.bind_all("<Button-1>", lambda e: focus1(t))
    t = 0
    wind.mainloop()
total_buyers()