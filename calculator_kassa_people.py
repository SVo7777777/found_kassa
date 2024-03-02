from tkinter import *
from tkinter import ttk, messagebox, filedialog
import math
import datetime
from tkcalendar import Calendar, DateEntry
import os
try:
    import tkinter as tk
    from tkinter import ttk
    from tkinter import scrolledtext

except ImportError:
    import Tkinter as tk
    import ttk
#создаём окно
root = Tk()
root.title("фазенда")
root.geometry("1200x535+2+2")#1300x460+200+2; 1500x600+5+5
root['bg'] = 'orange'
root.overrideredirect(0)
#root.attributes("-topmost", True)
root.resizable()
root.option_add("*tearOff", FALSE)
dirname, filename = os.path.split(os.path.realpath(__file__))
def rew_tabl():
    win = Tk()
    win.title("Paзрешение")
    win.geometry("300x70+20+120")
    l = Label(win, text="Введите код доступа: ")
    l.place(x=5, y=10)
    e = Entry(win)
    e.place(x=5, y=30)
    lv = Label(win)
    def vvod(event):
        if e.get() == 'fazenda':
            print('Welcome..!!!')
            os.startfile(dirname + '\\kalkulator.txt')
            win.destroy()
        else:
            lv.config(text='Неверный пароль!!!')
            lv.place(x=5, y=50)
            print('Код неверный..!!!')
    e.bind('<Return>', vvod)

def itog_day(data):
    global wind1
    wind1.destroy()
    wind = Tk()
    wind.title('итог за день')
    wind.geometry('400x200+500+300')
    print(data)
    l_per = Label(wind, text='Всего переводов за ' + data)
    l_per.place(x=10, y=20)
    l = Label(wind, text='Всего наличными за ' + data)
    l.place(x=10, y=50)
    l2 = Label(wind, text='Итого за ' + data)
    l2.place(x=80, y=100)
    per = []
    nal = []
    with open('kalkulator.txt', 'r') as f:
        all = f.read()
        sp_all = all.splitlines()
        for i in range(len(sp_all)):
            s = sp_all[i].split()
            da = data.split()
            #print(s)
            #print(da)
            #print(s[0][0:5])
            #print(da[0])
            if len(s) == 4:
                if s[0][0:5] == da[0] and s[3] == 'перевод':
                    per.append(int(s[2]))
            else:
                if s[0][0:5] == da[0]:
                    nal.append(int(s[2]))
    print(math.fsum(per))
    print(math.fsum(nal))
    l_per.config(text='Всего переводов за ' + data + ': ' + str(math.fsum(per)))
    l.config(text='Всего наличными за ' + data + ': ' + str(math.fsum(nal)))
    l2.config(text='Итого за ' + data + ': ' + str(math.fsum(nal) + math.fsum(per)))
def total_che():
    global wind1
    wind1 = Tk()
    wind1.title('итог за день')
    wind1.geometry('400x200+500+300')
    l3 = Label(wind1, text='Введите дату по образцу (число-месяц: 23-04):')
    l3.place(x=10, y=50)
    en = Entry(wind1)
    en.place(x=10, y=80)
    en.bind('<Return>', lambda em: (itog_day(en.get())))
def col():
    global wind1
    wind1 = Tk()
    wind1.title('количество строк')
    wind1.geometry('400x200+500+300')
    l3 = Label(wind1, text='Введите количество строк калькулятора')
    l3.place(x=10, y=50)
    en = Entry(wind1)
    en.place(x=10, y=80)
    en.bind('<Return>', lambda em: (tabl(int(en.get()))))
def total_buyers():
    wind = Tk()
    wind.title('всего покупателей за день')
    wind.geometry('850x300+300+300')
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
                   normalbackground="lightgreen",
                   weekendbackground="darkgreen",
                   weekendforeground="white",
                   cursor="hand1", year=currentYear, month=currentMonth, day=currentDay)
    # cal.pack(fill="both", expand=True)
    # cal.grid((row=0, column=0)
    #cal.place(x=400, y=10)
    #текущая дата всегда выделена
    today_date = datetime.date(year=currentYear, month=currentMonth, day=currentDay)
    cal.calevent_create(today_date, 'Hello World', 'today_date')
    cal.tag_config('today_date', background='blue', foreground='white')
    text = tk.Text(wind, width=30, height=10.4, bg="pink", font=('Arial', 16, 'bold'),
                   fg='green', wrap=tk.WORD)
    text.place(x=10, y=10)
    #text.insert('1.0', str(today) + ' : ')
    text.focus()
    day = {}
    hour = ['06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
    k = 0
    data = []
    with open('kalkulator.txt', 'r') as f:
        all = f.read()
        sp_all = all.splitlines()
        for i in range(len(sp_all)):
            s = sp_all[i].split()
            data.append(s[0])
            print(s)
        print(data)
        d = []
        v = 0
        d.append(data[0])
        for c in data:
            if c != d[v]:
                d.append(c)
                v = v + 1

        print('список дат: ', d)
    with open('kalkulator.txt', 'r') as f:
        all = f.read()
        sp_all = all.splitlines()
        day[d[k]] = []
        for i in range(len(sp_all)):
            s = sp_all[i].split()
            print(s)
            print(s[0])
            print('номер элемента списка дат: ', k)
            print(d[k])
            if s[0] == d[k]:
                day[d[k]].append(s[1])


            else:
                k = k + 1
                print('номер элемента списка дат: ', k)
                day[d[k]] = []
                print(d[k])
                day[d[k]].append(s[1])
                print(d[k])

        print(day)
        print(len(day))
        #m = []
        #print(m)
        p = 0
        for n in d:
            print('date ', n)
            print('hours in this date ', day[n])
            print(len(day[n]))
            a = len(day[n])
            print('длина ключа словаря', a)
            print(len(hour))
            for hou in range(len(hour)-1):
                print(hour[hou])
                for l in range(a):
                    ho = day[n][l]
                    print('hours ', ho[0:2])
                    if hour[hou] == ho[0:2]:
                        p = p + 1
                        print(p)
                print(hour[hou], ' in date ', n, ' num ', p)
                text.insert(END, '\n' + n + ' : ' + hour[hou] + '-' + hour[hou + 1] + ' - ' + str(p) + ' чел.' )
                p = 0

    def update_text(event):
        text.delete('1.0', '2.0')
        cal.config(selectbackground="red")
        data = str(cal.selection_get())
        print('выбранная дата : ', data)
        data_num = data.replace('-', '')
        print(data_num)
        text.insert('1.0', data + ' : ')
        text.focus()
        if data_num in d:
            vvod(data)
        else:
            text.insert('2.0', ' за этот день нет фото')

     #text.bind('<Return>', print_sel)
    cal.bind("<<CalendarSelected>>", update_text)
    ''' m.append([])
            print(m)
            df = day[n]
            for j in range(a):
                dv = df[j][0:2]
                print(df[j][0:2])
                m[p].append(dv)
            print(m)
            p = p + 1
        ho = 0
        for h in range(len(d)):
            for o in range(len(hour)):
                if m[h][o] == hour[o]:
                    ho = ho + 1
            print(ho)
            ho = 0'''


#создаём меню
main_menu = Menu(root, fg='blue', bg='orange', font=('Comic',40, 'bold'), bd=2)
main_menu.configure(fg='blue', bg='orange', font=('Comic',40, 'bold'), bd=2)
main_menu['fg'] = 'green'
file_menu = Menu()
file_menu.add_command(label="open_calculator", command=rew_tabl)
file_menu.add_command(label="itog_day", command=total_che)
file_menu.add_command(label="col", command=col)
file_menu.add_command(label="total_buyers", command=total_buyers)

root.config(menu=main_menu)
main_menu.add_cascade(label="open", menu=file_menu)

#для кассового чека
canvas9 = Canvas(root, width=200, height=460, borderwidth=0, background="lightblue")
canvas9.pack(side="left", fill="both", expand=True)
canvas10 = Canvas(root, width=450, height=900, borderwidth=0, background="lightgreen")
canvas10.place(x=700, y=0)
sum_chek = Label(canvas10, text=' 0.0 р. ', fg= 'red', width=24, font=('Arial', 20, 'bold'))
sum_chek.place(x=15, y=200)
sd_chek = Label(canvas10, text='Сдача с оплаты: ', width=24, font=('Arial', 20, ''))
sd_chek.place(x=20, y=350)
vv_sum = Entry(canvas10, width=24, justif='center', font=('Arial', 20, 'bold'))
vv_sum.place(x=30, y=400)
#создаём полосу прокрутки для холста для frame3 and canvas9 для кассового чека
vsb8 = Scrollbar(canvas9, orient="vertical")
vsb8.pack(side="right", fill="y")
canvas9.configure(yscrollcommand=vsb8.set)
vsb8.configure(command=canvas9.yview)
#создаём фрэйм для виджетов на холсте, чтобы их прокручивать
scrolled_frame8 = Frame(canvas9, background=canvas9.cget('bg'))
canvas9.create_window((4, 4), window=scrolled_frame8, anchor="nw")
def on_configure8(event):
    """Set the scroll region to encompass the scrolled frame"""
    canvas9.configure(scrollregion=canvas9.bbox("all"))
scrolled_frame8.bind("<Configure>", on_configure8)
#создаём таблицу для калькулятора
but = {}
entry = {}
combo_box = {}
ito = 0
zapisej2 = 0
def tabl(col):
    for z in range(col):
        for j in range(7):

                if j == 5 or j == 7:
                    but[(z, j)] = Button(scrolled_frame8, text='удалить', width=8, fg='blue',
                                          font=('Arial', 19, 'bold'))
                    but[z, j].grid(row=z, column=j)
                    #if j == 7:
                        #but[z, j].config(text='+', width=5)
                else:
                    entry[(z, j)] = Entry(scrolled_frame8, width=5, fg='blue',
                                              font=('Arial', 30, 'bold'))
                    entry[z, j].grid(row=z, column=j)
                    if j == 1 or j == 3:
                        entry[z, j].config(justif='center')
                    if j == 1 or j == 3:
                        entry[z, j].config(width=3)
                    if j == 0:
                        entry[z, j].config(justif='right')
                    if j == 1:
                        entry[z, j].insert(0, 'x')
                    if j == 3:
                        entry[z, j].insert(0, '=')
                    if j == 4:
                        entry[z, j].config(fg='orange')
col = 20
tabl(col)

sum_sp = []
def chek_stoimost(t):# стоимость по строке
    global chek_full, name_tara
    try:

        price = entry[t, 0].get()
        colich = entry[t, 2].get()
        print(price)
        print(colich)
        stoim = int(price)*int(colich)
        if entry[t, 4].get() == '':
            entry[t, 4].insert(0, stoim)
            chek_full = False
            sum_sp.append(stoim)
            print(sum_sp)
            print(math.fsum(sum_sp))
        else:
            #messagebox.showinfo('внимание', 'удалите строку')
            #с = entry[t, 4].get()
            entry[t, 4].delete('0', END)
            sum_sp.pop(t)
            print(sum_sp)
            print(math.fsum(sum_sp))
            entry[t, 4].insert(0, stoim)
            sum_sp.insert(t, stoim)
            chek_full = False
            #удалить сумму из списка
            print(sum_sp)
        #if t > 0:

        entry[t + 1, 0].focus(), vvod(t + 1)
    except ValueError:
        if entry[t, 0].get() == '':
            messagebox.showinfo('внимание', 'введите число')
            entry[t, 0].focus()
            vvod(t)
pust_chek = True

vvod_not = False# выбор растния в поиске возможен
def sum_chekf():
    global sum_sp, pust_chek, ito, vvod_not
    t = 0
    vvod_not = True# выбор растния в поиске невозможен
    pust_chek = False
    #ch = num_chek['text']
    #ch2 = ch.split()
    #c = ch2[2]
    if sum_sp == []:
        messagebox.showinfo('внимание', 'действие выполнить нельзя!')
    else:
        ito = math.fsum(sum_sp)
        ito1 = ito
        if ito > 10000 and ito <= 50000:
            messagebox.showinfo('внимание', f'ваша сумма {int(ito)} р. \nвам полагается скидка 5 %!')
            ito = ito - ito * 0.05
            sum_chek.config(text=str(ito1) + 'p.')
            chek_itogo.config(text=str(ito) + 'p.')

        elif ito > 50000 and ito <= 100000:
            messagebox.showinfo('внимание', f'ваша сумма {int(ito)} р. \nвам полагается скидка 10 %!')
            ito = ito - ito * 0.1
            sum_chek.config(text=str(ito1) + 'p.')
            chek_itogo.config(text=str(ito) + 'p.')

        elif ito > 100000 and ito <= 500000:
            messagebox.showinfo('внимание', f'ваша сумма {int(ito)} р. \nвам полагается скидка 15 %!')
            ito = ito - ito * 0.15
            sum_chek.config(text=str(ito1) + 'p.')
            chek_itogo.config(text=str(ito) + 'p.')

        elif ito > 500000:
            messagebox.showinfo('внимание', f'ваша сумма {int(ito)} р. \nвам полагается скидка 30 %!')
            ito = ito - ito * 0.3
            sum_chek.config(text=str(ito1) + 'p.')
            chek_itogo.config(text=str(ito) + 'p.')

        else:
            sum_chek.config(text=str(ito1) + 'p.')
            chek_itogo.config(text=str(ito) + 'p.')

def sdacha_chekf():
    try:
        s = chek_itogo['text']
        print(s[0:-4])
        s2 = vv_sum.get()
        it = int(s2) - int(s[0:-4])
        chek_sdacha.config(text=str(it))
    except ValueError:
        messagebox.showinfo('внимание', 'действие выполнить нельзя')



chek_itogo = Button(canvas10, text='сумма', fg='red', width=14, bd=0, command=sum_chekf, font=('Arial', 37, 'bold'))
chek_itogo.place(x=10, y=100)
chek_sdacha = Button(canvas10, text='сдача', fg='lightgreen', width=14, bd=0, command=sdacha_chekf, font=('Arial', 37, 'bold'))
chek_sdacha.place(x=10, y=250)

#сохраняем суммы в 'kalkulator.txt'
def save(s):
    now_chek = datetime.datetime.now()
    data = now_chek.strftime("%d-%m-%Y %H:%M")
    with open('kalkulator.txt', 'a+') as k:
        k.write('\n' + data + ': ' + s)

chek_full = False
#очищаем калькулятор
def chek_up():
    global zapisej2, tabl_full, sum_sp, vvod_search2, pust_chek,vvod_not, ito
    if pust_chek == True:
        messagebox.showinfo('внимание', 'действие выполнить нельзя!')
    else:
        answer = messagebox.askyesno(
            title="Вопрос",
            message=f"Сохранить сумму? {int(ito)}")
        if answer:
            result2 = messagebox.askyesno('внимание', 'это перевод?', detail="Hello World!")
            if result2:
                s = int(ito)
                save(str(s) + ' перевод')
            else:
                s = int(ito)
                save(str(s))
    for i in range(col):
        if entry[i, 0].get() != '':
            entry[i, 0].delete('0', END)
            entry[i, 2].delete('0', END)
            entry[i, 4].delete('0', END)
    sum_sp = []
    print('список сумм пуст - ', sum_sp)
    entry[0, 0].focus()
    vvod(0)
    pust_chek = True
    vvod_not = False  # выбор растния в поиске возможен
    chek_itogo.config(text='сумма')
    sum_chek.config(text='0.0 p.')
    chek_sdacha.config(text='сдача')
    vv_sum.delete("0", END)

    if zapisej2 != 0:
        print('всего записей: ', zapisej2+1)
    print('сумма = ', int(ito))
    zapisej2 = 0
    ito = 0
    #print(type(ito))

def rew_sum():
    wind2 = Tk()
    wind2.title('итог за день')
    wind2.geometry('400x200+500+300')
    now_chek = datetime.datetime.now()
    data1 = now_chek.strftime("%d-%m")
    data2 = now_chek.strftime("%d-%m-%Y %H:%M")
    def itog_day(data):
        l_per.config(text='Всего переводов за ' + data)
        l.config(text='Всего наличными за ' + data)
        l2.config(text='Итого за ' + data)
        per = []
        nal = []
        with open('kalkulator.txt', 'r') as f:
            all = f.read()
            sp_all = all.splitlines()
            for i in range(len(sp_all)):
                s = sp_all[i].split()
                da = data.split()
                print(s)
                print(da)
                print(s[0][0:5])
                print(da[0])
                if len(s) == 4:
                    if s[0][0:5] == da[0] and s[3] == 'перевод':
                        per.append(int(s[2]))
                else:
                    if s[0][0:5] == da[0]:
                        nal.append(int(s[2]))
        print(math.fsum(per))
        print(math.fsum(nal))
        l_per.config(text='Всего переводов за ' + data + ': ' + str(math.fsum(per)))
        l.config(text='Всего наличными за ' + data + ': ' + str(math.fsum(nal)))
        l2.config(text='Итого за ' + data + ': ' + str(math.fsum(nal) + math.fsum(per)))



    def clear():
        l_per.config(text='')
        l.config(text='')
        l2.config(text='')
        l.place_forget()
        l2.place_forget()
        l_per.place_forget()
        l3.place_forget()
        e.place_forget()

    l_per = Label(wind2, font=("Arial", 16))
    l_per.place(x=10, y=20)
    l = Label(wind2, font=("Arial", 16))
    l.place(x=10, y=50)
    l2 = Label(wind2,font=("Arial", 16))
    l2.place(x=80, y=100)
    l3 = Label(wind2)
    #l3.place(x=10, y=50)
    e = Entry(wind2)
    #e.place(x=10, y=80)

    i_cheki = Button(wind2, text='итог за сегодня', width=14, command=lambda: itog_day(data1), bd=1,
                     font=('Arial', 12, ''))
    i_cheki.place(x=140, y=160)

#id_cheki = Button(wind2, text='итог за день', width=14, command=itog_d, bd=1, font=('Arial', 12, ''))
#id_cheki.place(x=200, y=130)
up_chek = Button(canvas10, text='очистить', width=14, command=chek_up, bd=0, font=('Arial', 30, ''))
up_chek.place(x=60, y=10)
save_sum = Button(canvas10, text='rew', fg='gray', width=4, command=rew_sum, bd=0, font=('Arial', 15, ''))
save_sum.place(x=400, y=400)
#для кнопок удалить
def del_str(z):
    global zapisej2, vvod_not
    vvod_not = False  # выбор растения в поиске возможен

    try:
        print('удаляем ' + str(z) + ' строку')
        print('удаляем ' + str(sum_sp[z]))

        entry[z, 0].delete('0', END)
        entry[z, 2].delete('0', END)
        entry[z, 4].delete('0', END)
        entry[z, 6].delete('0', END)
        sum_sp.pop(z)
        print(sum_sp)
        print(math.fsum(sum_sp))
        print(zapisej2)
        d = zapisej2
        for n in range(zapisej2+1):
            print('проверяем строку ' + str(n))
            if entry[n, 0].get() == '':
                print('строка ' + str(n) + ' пустая')
                if entry[n+1, 0].get() != '':
                    print('строка ' + str(n + 1) + ' непустая')
                    m0 = entry[n + 1, 0].get()
                    print(m0)
                    m2 = entry[n + 1, 2].get()
                    m4 = entry[n + 1, 4].get()
                    entry[n, 0].insert(END, m0)
                    entry[n, 2].insert(END, m2)
                    entry[n, 4].insert(END, m4)
                    entry[n + 1, 0].delete('0', END)
                    entry[n + 1, 2].delete('0', END)
                    entry[n + 1, 4].delete('0', END)
                else:
                    entry[d, 0].focus()
                    entry[d+1, 0].unbind('<Return>')
                    vvod(d)
                    d = d-1
    except IndexError:
        messagebox.showinfo('внимание', 'не удаляется, \nжми "ок" и удалится')
        entry[z, 0].delete('0', END)
        entry[z, 2].delete('0', END)
        entry[z, 4].delete('0', END)
        entry[z, 0].focus()
        vvod(z)

#ввод чисел для клькулятора
def un_bind(t):
    global zapisej2
    entry[t, 0].unbind('<Return>')
    zapisej2 = t
    print('запись: ', zapisej2+1, '-ая')
    but[t, 5].config(command=lambda: del_str(t))
    entry[t, 2].bind("<Return>", lambda e: (chek_stoimost(t)))
    #entry[t, 2].bind("<Return>", lambda e: (chek_stoimost(t), entry[t+1, 0].focus(), vvod(t+1)))

entry[0, 0].focus()
entry[0, 0].bind("<Return>", lambda ev: (entry[0, 2].focus(), un_bind(0)))
def vvod(t):
    entry[t, 0].bind("<Return>", lambda ev: (entry[t, 2].focus(), un_bind(t)))

root.mainloop()