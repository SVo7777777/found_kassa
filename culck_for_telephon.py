from tkinter import *
from tkinter import ttk, messagebox, filedialog
import math
import datetime
#from digital_keyboard import klava
#from buyers_sales import total_buyers
import os
import random
try:
    import tkinter as tk
    from tkinter import ttk
    from tkinter import scrolledtext

except ImportError:
    import Tkinter as tk
    import ttk
#создаём окно
root = Tk()
root.title("калькулятор")
root.geometry("580x250+2+2")#1300x460+200+2; 1500x600+5+5
root['bg'] = 'orange'
root.overrideredirect(0)
#root.attributes("-topmost", True)
root.resizable()
root.option_add("*tearOff", FALSE)
dirname, filename = os.path.split(os.path.realpath(__file__))

#создаём меню

#для калькулятора 
canvas9 = Canvas(root, width=100, height=260, borderwidth=0, background="DarkKhaki")
canvas9.pack(side="left", fill="both", expand=True)
canvas10 = Canvas(root, width=500, height=200, borderwidth=0, background="BurlyWood")
canvas10.pack(side="right", fill="both", expand=False)
sum_chek = Label(canvas10, text=' 0.0 р. ', fg='red', width=13, font=('Arial', 14, 'bold'))
sum_chek.place(x=2, y=60)
vv_sum = Entry(canvas10, width=10, justif='center', font=('Arial', 14, 'bold'))
vv_sum.place(x=122, y=93)
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
        for j in range(6):

                if j == 5 or j == 7:
                    but[(z, j)] = Button(scrolled_frame8, text='del', width=4, fg='blue',
                                          font=('Arial', 10, 'bold'))
                    but[z, j].grid(row=z, column=j)
                    #if j == 7:
                        #but[z, j].config(text='+', width=5)
                else:
                    entry[(z, j)] = Entry(scrolled_frame8, width=5, fg='blue',
                                              font=('Arial', 14, 'bold'))
                    entry[z, j].grid(row=z, column=j)
                    if j == 1 or j == 3:
                        entry[z, j].config(justif='center')
                    if j == 1 or j == 3:
                        entry[z, j].config(width=3)
                    if j == 0:
                        entry[z, j].config(width=4)
                    if j == 2:
                        entry[z, j].config(width=5)
                    if j == 0:
                        entry[z, j].config(justif='right')
                    if j == 1:
                        entry[z, j].insert(0, 'x')
                    if j == 3:
                        entry[z, j].insert(0, '=')
                    if j == 4:
                        entry[z, j].config(fg='orange', width=7)
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
            sum_chekf()
        else:
            entry[t, 4].delete('0', END)
            sum_sp.pop(t)
            print(sum_sp)
            print(math.fsum(sum_sp))
            entry[t, 4].insert(0, stoim)
            sum_sp.insert(t, stoim)
            chek_full = False
            #удалить сумму из списка
            print(sum_sp)
            sum_chekf()
        entry[t + 1, 0].focus(), focus(), vvod(t + 1)
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
    if sum_sp == []:
        messagebox.showinfo('внимание', 'действие выполнить нельзя!')
    else:
        ito = math.fsum(sum_sp)
        ito1 = ito
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

chek_itogo = Button(canvas10, text='сумма', fg='red', width=9, bd=1, command=sum_chekf, font=('Arial', 20, 'bold'))
chek_itogo.place(x=2, y=5)
chek_sdacha = Button(canvas10, text='сдача с сум:', fg='lightgreen', anchor='e', width=11, bd=1, command=sdacha_chekf, font=('Arial', 12, 'bold'))
chek_sdacha.place(x=2, y=90)

#сохраняем суммы в 'kalkulator.txt'
def save(s):
    now_chek = datetime.datetime.now()
    data = now_chek.strftime("%d-%m-%Y %H:%M")
    with open('kalkulator.txt', 'a+') as k:
        k.write('\n' + data + ': ' + s)

chek_full = False
#очищаем калькулятор
def chek_up():
    global zapisej2, tabl_full, sum_sp, vvod_search2, pust_chek,vvod_not, ito, entry_focus
    if pust_chek == True:
        messagebox.showinfo('внимание', 'действие выполнить нельзя!')
    else:
        answer = messagebox.askyesno(
            title="Вопрос",
            message=f"Сохранить сумму? {chek_itogo['text']}")
        if answer:
            result2 = messagebox.askyesno('внимание', 'это перевод?', detail="Hello World!")
            c = chek_itogo['text'].split('.')
            if result2:
                s = int(c[0])
                save(str(s) + ' перевод')
            else:
                s = int(c[0])
                save(str(s))
    for i in range(col):
        if entry[i, 0].get() != '':
            entry[i, 0].delete('0', END)
            entry[i, 2].delete('0', END)
            entry[i, 4].delete('0', END)
    sum_sp = []
    entry_focus = []
    print('список сумм пуст - ', sum_sp)
    entry[0, 0].focus()
    focus()
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

def rew_sum():
    wind2 = Tk()
    wind2.title('итоги')
    wind2.geometry('400x200+20+40')
    now_chek = datetime.datetime.now()
    data1 = now_chek.strftime("%d-%m")
    def itog_day(data):
        try:
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
        except IndexError:
            messagebox.showerror('IndexError', ' удалите пустую строку в "kalkulator.txt"')
    def itog_y():
        l_per.config(text='Всего переводов ')
        l.config(text='Всего наличными ')
        l2.config(text='Итого за ')
        per = []
        nal = []
        with open('kalkulator.txt', 'r') as f:
            all = f.read()
            sp_all = all.splitlines()
            s_kakogo = sp_all[0].split()[0]
            po_kakoe = sp_all[-1].split()[0]
            for i in range(len(sp_all)):
                s = sp_all[i].split()
                if len(s) == 4:
                    if s[3] == 'перевод':
                        per.append(int(s[2]))
                else:
                        nal.append(int(s[2]))
        #print(math.fsum(per))
        #print(math.fsum(nal))
        l_per.config(text='Всего переводов c ' + s_kakogo + ' по' + po_kakoe + ': ' + str(math.fsum(per)))
        l.config(text='Всего наличными c ' + s_kakogo + ' по' + po_kakoe + ': ' + str(math.fsum(nal)))
        l2.config(text='Итого c ' + s_kakogo + ' по' + po_kakoe + ': ' + str(math.fsum(nal) + math.fsum(per)))

    def itog_mon(m):
        month = {'01': 'ЯНВАРЬ',
                 '02': 'ФЕВРАЛЬ',
                 '03': 'МАРТ',
                 '04': 'АПРЕЛЬ',
                 '05': 'МАЙ',
                 '06': 'ИЮНЬ',
                 '07': 'ИЮЛЬ',
                 '08': 'АВГУСТ',
                 '09': 'СЕНТЯБРЬ',
                 '10': 'ОКТЯБРЬ',
                 '11': 'НОЯБРЬ',
                 '12': 'ДЕКАБРЬ'}
        data = month.get(m)
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
                if len(s) == 4:
                    if s[0][3:5] == m and s[3] == 'перевод':
                        per.append(int(s[2]))
                else:
                    if s[0][3:5] == m:
                        nal.append(int(s[2]))
        l_per.config(text='Всего переводов за ' + data + ': ' + str(math.fsum(per)))
        l.config(text='Всего наличными за ' + data + ': ' + str(math.fsum(nal)))
        l2.config(text='Итого за ' + data + ': ' + str(math.fsum(nal) + math.fsum(per)))

    def itog_m():
        wind2 = Tk()
        wind2.title('итог за месяц')
        wind2.geometry('300x50+100+150')
        l = Label(wind2, text='Введите номер месяца по образцу (месяц: 04):')
        l.place(x=10, y=0)
        e = Entry(wind2)
        e.place(x=10, y=17)
        e.focus()

        def dest():
            wind2.destroy()

        e.bind('<Return>', lambda en: (itog_mon(e.get()), dest()))

    l_per = Label(wind2, font=("Arial", 10))
    l_per.place(x=10, y=20)
    l = Label(wind2, font=("Arial", 10))
    l.place(x=10, y=50)
    l2 = Label(wind2,font=("Arial", 10))
    l2.place(x=80, y=100)
    i_cheki = Button(wind2, text='итог за сегодня', width=13, command=lambda: itog_day(data1), bd=1,
                     font=('Arial', 12, ''))
    i_cheki.place(x=10, y=160)
    i_mon = Button(wind2, text='итог за месяц', width=12, command=lambda: itog_m(), bd=1,
                     font=('Arial', 12, ''))
    i_mon.place(x=145, y=160)
    i_all = Button(wind2, text='общий итог', width=12, command=lambda: itog_y(), bd=1,
                   font=('Arial', 12, ''))
    i_all.place(x=270, y=160)

def discount(p):
    try:
        s = chek_itogo['text']
        #print(s)
        sp = s.split(".")
        #print(sp)
        su = int(sp[0])
        new_sum = su - su * 0.01 * p
        chek_itogo['text'] = str(new_sum)
    except ValueError:
        messagebox.showwarning('ValueError', 'Дейслвие выполнить невозможно!!!')

def klava():
    global keyboard
    keyboard = Toplevel(root)
    keyboard.title("цифровая клавиатура")
    keyboard.geometry("248x95+330+155")#1300x460+200+2; 1500x600+5+5
    #keyboard['bg'] = 'orange'
    keyboard.overrideredirect(0)
    keyboard.attributes("-topmost", True)
    keyboard.resizable()
    keyboard.option_add("*tearOff", FALSE)
    def discount(n):
        #print(entry_focus[-1])
        if n == 11:
            entry_focus[-1].focus()
            entry_focus[-1].delete(entry_focus[-1].index(END) - 1)#удаляем последний символ из энтри
        elif n == 22:#кнопка ввода en
            entry_focus[-1].focus()
            for key in entry:
                if entry[key] == entry_focus[-1]:
                    #print('entry[key] = ', entry[key])
                    #print('entry_focus[-1] = ', entry_focus[-1])
                    #print(key)
                    if key[1] == 0:
                        entry[key[0], 2].focus()
                        focus()
                        un_bind(key[0])
                        break
                    elif key[1] == 2:
                        chek_stoimost(key[0])
                        focus()
                        break
        else:
            entry_focus[-1].insert(END, n)
            entry_focus[-1].focus()
    num_1 = Button(keyboard, text='1', width=2, height=1, fg='white',bg='blue',command=lambda: discount(1), bd=2, font=('Arial', 15, 'bold'))
    num_1.place(x=1, y=1)
    num_2 = Button(keyboard, text='2', width=2, height=1, fg='white',bg='blue', command=lambda: discount(2), bd=2, font=('Arial', 15, 'bold'))
    num_2.place(x=36, y=1)
    num_3 = Button(keyboard, text='3', width=2, height=1, fg='white',bg='blue', command=lambda: discount(3), bd=2, font=('Arial', 15, 'bold'))
    num_3.place(x=71, y=1)
    num_4 = Button(keyboard, text='4', width=2, height=1, fg='white',bg='blue',command=lambda: discount(4), bd=2, font=('Arial', 15, 'bold'))
    num_4.place(x=106, y=1)
    num_5 = Button(keyboard, text='5', width=2, height=1, fg='white',bg='blue', command=lambda: discount(5), bd=2, font=('Arial', 15, 'bold'))
    num_5.place(x=141, y=1)
    num_6 = Button(keyboard, text='6', width=2, height=1, fg='white',bg='blue', command=lambda: discount(6), bd=2, font=('Arial', 15, 'bold'))
    num_6.place(x=1, y=45)
    num_7 = Button(keyboard, text='7', width=2, height=1, fg='white',bg='blue',command=lambda: discount(7), bd=2, font=('Arial', 15, 'bold'))
    num_7.place(x=36, y=45)
    num_8 = Button(keyboard, text='8', width=2, height=1, fg='white',bg='blue', command=lambda: discount(8), bd=2, font=('Arial', 15, 'bold'))
    num_8.place(x=71, y=45)
    num_9 = Button(keyboard, text='9', width=2, height=1, fg='white',bg='blue', command=lambda: discount(9), bd=2, font=('Arial', 15, 'bold'))
    num_9.place(x=106, y=45)
    num_0 = Button(keyboard, text='0', width=2, height=1, fg='white',bg='blue',command=lambda: discount(0), bd=2, font=('Arial', 15, 'bold'))
    num_0.place(x=141, y=45)
    num_b = Button(keyboard, text='bs', width=5, height=1, fg='white',bg='blue', command=lambda: discount(11), bd=2, font=('Arial', 16, 'bold'))
    num_b.place(x=176, y=1)
    num_e = Button(keyboard, text='en', width=5, height=1, fg='white',bg='blue', command=lambda: discount(22), bd=2, font=('Arial', 16, 'bold'))
    num_e.place(x=176, y=45)
    root.mainloop()
entry_focus = []
def focus():
  widg = root.focus_get()
  if widg.winfo_class() == "Entry":
    entry_focus.append(widg)

root.bind_all("<Button-1>", lambda e: focus())
up_chek = Button(canvas10, text='очистить', width=8, command=chek_up, bd=1, font=('Arial', 12, 'bold'))
up_chek.place(x=165, y=60)
klava = Button(canvas10, text='dig-keyb', height=2, width=8, command=klava, bd=1, font=('Arial', 13, 'bold'))
klava.place(x=165, y=5)
save_sum = Button(canvas10, text='rew', fg='gray', width=4, command=rew_sum, bd=0, font=('Arial', 12, ''))
save_sum.place(x=2, y=123)
save_sum = Button(canvas10, text='5 %', width=4, command=lambda: discount(5), bd=0, font=('Arial', 12, ''))
save_sum.place(x=50, y=123)
save_sum = Button(canvas10, text='10 %', width=4, command=lambda: discount(10), bd=0, font=('Arial', 12, ''))
save_sum.place(x=95, y=123)
save_sum = Button(canvas10, text='15 %', width=4, command=lambda: discount(15), bd=0, font=('Arial', 12, ''))
save_sum.place(x=140, y=123)
save_sum = Button(canvas10, text='20 %', width=4, command=lambda: discount(20), bd=0, font=('Arial', 12, ''))
save_sum.place(x=185, y=123)
save_sum = Button(canvas10, text='25 %', width=4, command=lambda: discount(25), bd=0, font=('Arial', 12, ''))
save_sum.place(x=2, y=153)
save_sum = Button(canvas10, text='30 %', width=4, command=lambda: discount(30), bd=0, font=('Arial', 12, ''))
save_sum.place(x=50, y=153)
save_sum = Button(canvas10, text='35 %', width=4, command=lambda: discount(35), bd=0, font=('Arial', 12, ''))
save_sum.place(x=95, y=153)
save_sum = Button(canvas10, text='40 %', width=4, command=lambda: discount(40), bd=0, font=('Arial', 12, ''))
save_sum.place(x=140, y=153)
save_sum = Button(canvas10, text='col', width=4, command=col, bd=0, font=('Arial', 12, ''))
save_sum.place(x=185, y=153)

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
        sum_chekf()
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
                    focus()
                    entry[d+1, 0].unbind('<Return>')
                    vvod(d)
                    d = d-1
    except IndexError:
        messagebox.showinfo('внимание', 'не удаляется, \nжми "ок" и удалится')
        entry[z, 0].delete('0', END)
        entry[z, 2].delete('0', END)
        entry[z, 4].delete('0', END)
        entry[z, 0].focus()
        focus()
        vvod(z)

#ввод чисел для клькулятора
def un_bind(t):
    global zapisej2
    entry[t, 0].unbind('<Return>')
    zapisej2 = t
    #print('запись: ', zapisej2+1, '-ая')
    but[t, 5].config(command=lambda: del_str(t))
    entry[t, 2].bind("<Return>", lambda e: (chek_stoimost(t)))

entry[0, 0].focus()
entry[0, 0].bind("<Return>", lambda ev: (entry[0, 2].focus(), focus(), un_bind(0)))
def vvod(t):
    entry[t, 0].bind("<Return>", lambda ev: (entry[t, 2].focus(), focus(), un_bind(t)))
root.mainloop()
