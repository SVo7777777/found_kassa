from tkinter import *
from tkinter import ttk, messagebox, filedialog
import math
import datetime
import re
import os

#создаём окно
root = Tk()
root.title("фазенда")
root.geometry("1500x600+5+5")#1300x460+200+2
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
            os.startfile(dirname + '\\tabl.txt')
            win.destroy()
        else:
            lv.config(text='Неверный пароль!!!')
            lv.place(x=5, y=50)
            print('Код неверный..!!!')
    e.bind('<Return>', vvod)

def total_che():
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
            os.startfile(dirname + '\\total_chek.txt')
            win.destroy()
        else:
            lv.config(text='Неверный пароль!!!')
            lv.place(x=5, y=50)
            print('Код неверный..!!!')

    e.bind('<Return>', vvod)
#создаём меню
main_menu = Menu(root, fg='blue', bg='orange', font=('Comic',40, 'bold'), bd=2)
main_menu.configure(fg='blue', bg='orange', font=('Comic',40, 'bold'), bd=2)
main_menu['fg'] = 'green'
file_menu = Menu()
file_menu.add_command(label="open_tabl", command=rew_tabl)
file_menu.add_command(label="open_total_check", command=total_che)
root.config(menu=main_menu)

main_menu.add_cascade(label="open", menu=file_menu)
#main_menu.add_cascade(label="правка", menu=file_menu2)
#main_menu.add_cascade(label="формат", menu=file_menu3)

# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
# создаем несколько фреймвов(вкладок)
frame1 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
frame1.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH, expand=True)
notebook.add(frame1, text="<ПОИСК РАСТЕНИЯ>", compound=LEFT)# image=python_logo,
notebook.add(frame3, text="<КАЛЬКУЛЯТОР>", compound=LEFT)

#создаём холсты
#для поиска
canvas_search = Canvas(frame1, width=1500, height=760, borderwidth=0, background="lightgreen")
canvas_search.place(x=2, y=190)
canvas_foto = Canvas(frame1, width=1500, height=185, borderwidth=0, background="lightblue")
canvas_foto.place(x=2, y=2)
ph2 = PhotoImage(file='fazenda2.png')
canvas_foto.create_image(600, 200, image=ph2)
canvas_foto2 = Canvas(frame1, width=400, height=695, borderwidth=0, background="lightblue")
canvas_foto2.place(x=1125, y=2)
ph = PhotoImage(file='fazenda1.png')
canvas_foto2.create_image(600, 483, image=ph)

#для кассового чека
canvas9 = Canvas(frame3, width=200, height=460, borderwidth=0, background="lightblue")
canvas9.pack(side="left", fill="both", expand=True)
canvas11 = Canvas(frame3, width=750, height=210, borderwidth=0, background="lightgreen")
#canvas11.place(x=0, y=0)
now_chek = datetime.datetime.now()
data_chek = Label(canvas11, text=now_chek.strftime("%d-%m-%Y %H:%M"), font=('Arial', 14, 'bold'))
data_chek.place(x=1, y=30)
num_chek = Label(canvas11, text='чек № 1', font=('Arial', 14, 'bold'))
num_chek.place(x=170, y=30)
num_chek2 = Label(canvas11, text='общая сумма по чеку № 1', font=('Arial', 14, 'bold'))
num_chek2.place(x=1, y=70)

canvas10 = Canvas(frame3, width=450, height=900, borderwidth=0, background="lightgreen")
canvas10.place(x=700, y=0)
sum_chek = Label(canvas10, text=' 0.0 р. ', fg= 'red', width=24, font=('Arial', 20, 'bold'))
sum_chek.place(x=15, y=200)
sd_chek = Label(canvas10, text='Сдача с оплаты: ', width=24, font=('Arial', 20, ''))
sd_chek.place(x=20, y=350)
vv_sum = Entry(canvas10, width=24, justif='center', font=('Arial', 20, 'bold'))
vv_sum.place(x=30, y=400)
#создаём полосу прокрутки для холста для frame8 and canvas9 для кассового чека
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
#frame3 and canvas9 для кассового чека создаём поля для ввода ввиде таблицы
with open('tabl.txt', 'r') as f:
    l = f.read()
    lst = []
    lst2 = []
    count = l.splitlines()
    print(len(count))
    num_lines = len(count)
    for i in range(1, len(count)):
        sf = count[i].split()
        lst.append(sf[1])
        lst2.append(sf[1] + ' ' + sf[2])
#print(lst2)
with open('cheki.txt', 'r') as fi:
    li = fi.read()
    lin = li.splitlines()
    col_chek = len(lin)
    print(col_chek)
num_chek2.config(text='общая сумма по чеку № ' + str(col_chek))
num_chek.config(text='чек № ' + str(col_chek))
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
        else:
            #messagebox.showinfo('внимание', 'удалите строку')
            #с = entry[t, 4].get()
            entry[t, 4].delete('0', END)
            sum_sp.pop(t)
            print(sum_sp)
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
    ch = num_chek['text']
    ch2 = ch.split()
    c = ch2[2]
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


def total_chek():
    sum = []
    win = Tk()
    win.title("Paзрешение")
    win.geometry("300x70+500+200")
    l = Label(win, text="Введите код доступа: ")
    l.place(x=5, y=10)
    e = Entry(win)
    e.place(x=5, y=30)
    lv = Label(win)

    def vvod(event):
        if e.get() == 'fazenda':
            with open('total_chek.txt', 'r') as f:
                file = f.read()
                sp = file.splitlines()
                for i in range(len(sp)):
                    s = sp[i].split()
                    sum.append(float((s[1])))
            print(math.fsum(sum))
            # but0[0, 4].config(text=str(math.fsum(sum)))
            #ch_total.config(text=str(math.fsum(sum)))  # общая сумма по всем чекам на кнопке
            win.destroy()
            win2 = Tk()
            win2.geometry('100x40+500+200')
            lab = Label(win2, text=str(math.fsum(sum)))
            lab.place(x=20, y=10)
        else:
            lv.config(text='Неверный пароль!!!')
            lv.place(x=5, y=50)
            print('Код неверный..!!!')

    e.bind('<Return>', vvod)
    #внизу накладной находится

def total_kalkuiator():
    sum = []
    win = Tk()
    win.title("Paзрешение")
    win.geometry("300x70+500+200")
    l = Label(win, text="Введите код доступа: ")
    l.place(x=5, y=10)
    e = Entry(win)
    e.place(x=5, y=30)
    lv = Label(win)

    def vvod(event):
        if e.get() == 'fazenda':
            with open('kalkulator.txt', 'r') as f:
                file = f.read()
                sp = file.splitlines()
                print(sp)
                print(len(sp))
                for i in range(len(sp)):
                    s = sp[i].split()
                    sum.append(int((s[0])))
            print(math.fsum(sum))
            win.destroy()
            win2 = Tk()
            win2.geometry('100x40+500+200')
            lab = Label(win2, text=str(math.fsum(sum)))
            lab.place(x=20, y=10)
        else:
            lv.config(text='Неверный пароль!!!')
            lv.place(x=5, y=50)
            print('Код неверный..!!!')

    e.bind('<Return>', vvod)
#сохраняем суммы в 'kalkulator.txt'
def save(s):
    with open('kalkulator.txt', 'a+') as k:
        k.write('\n' + str(s))

chek_full = False
#очищаем калькулятор
def chek_up():
    global zapisej2, tabl_full, sum_sp, vvod_search2, pust_chek,vvod_not, ito
    for i in range(40):
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
    s = int(ito)
    save(s)
    if zapisej2 != 0:
        print('всего записей: ', zapisej2+1)
    print('сумма = ', int(ito))
    zapisej2 = 0
    ito = 0
    #print(type(ito))


up_chek = Button(canvas10, text='очистить', width=14, command=chek_up, bd=0, font=('Arial', 30, ''))
up_chek.place(x=60, y=10)
#для кнопки удалить
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

#new_string(0, 0)
but = {}
entry = {}
combo_box = {}
ito = 0
zapisej2 = 0
for z in range(40):
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
#ввод чисел для клькулятора
def un_bind(t):
    global zapisej2
    entry[t, 0].unbind('<Return>')
    zapisej2 = t
    print('запись: ', zapisej2+1, '-ая')
    but[t, 5].config(command=lambda: del_str(t))
    entry[t, 2].bind("<Return>", lambda e: (chek_stoimost(t)))
    #entry[t, 2].bind("<Return>", lambda e: (chek_stoimost(t), entry[t+1, 0].focus(), vvod(t+1)))


entry[0, 0].bind("<Return>", lambda ev: (entry[0, 2].focus(), un_bind(0)))
def vvod(t):
    entry[t, 0].bind("<Return>", lambda ev: (entry[t, 2].focus(), un_bind(t)))


#открываем файл для чтения количества строк
with open('tabl.txt', 'r') as a:
    l = a.read()
    count = l.splitlines()#count-список из строк файла
    without_last = count.pop(len(count)-1)

menubut = {}
# для поиска на первой вкладке
def menubat0(i, j):
    menubut[(i + 1, 4)] = Menubutton(canvas_search, bg="orange", width=2, text='v', activebackground='blue',
                                     justify='center')
    options = Menu(menubut[i + 1, 4])
    menubut[i + 1, 4].config(menu=options)
    if i != 0:
        a = entry0[i + 1, 2].get()
        #print('в строке ', i + 1, a)
        #a = entry[i + 1, 2].get()
        c = entry0[i + 1, 6].get()
        t = entry0[i + 1, 3].get()
        p = entry0[i + 1, 4].get()
        col = entry0[i + 1, 5].get()
        prod = entry0[i + 1, 7].get()

        #print('в строке ', i + 1, a)
        #n = entry[i, 2].get()
        options.add_command(label='изменить название : ' + a, command=lambda: change_name(a, i, 2))
        options.add_command(label='изменить тару :' + t, command=lambda: change_name(t, i, 3))
        options.add_command(label='изменить расположение :' + p,command=lambda: change_name(p, i, 4))
        options.add_command(label='изменить количество :' + col, command=lambda: change_name(col, i, 5))
        options.add_command(label='изменить цену :' + c, command=lambda: change_name(c, i, 6))
        options.add_command(label='изменить "продано" :' + prod, command=lambda: change_name(prod, i, 7))

    menubut[i + 1, 4].grid(row=i + 1, columns=2)
#for i in range(1, num_lines):
    #menubat0(i, 1)
def change_n1(i,j,old):
    # global
    print('строка : ' + count[i])
    print('старое: ' + old)
    s = count[i].split()
    print(s)
    new = entry0[i + 1, j].get()
    print('заменяем на новое: ' + new)
    with open('tabl.txt', 'r') as file1, open('tabl1.txt', 'w') as file:
        lines = file1.readlines()
        print("мы тут")
        print(lines)
        for l in range(num_lines):
            #print('здесь')
            #stroca = stroca.strip()
            if count[i]+'\n' == lines[l]:
                s2_new = re.sub(old, new, lines[l])
                #file.write(s2_new)
                print('новая строка : '+ s2_new)
                file.write(s2_new)
                messagebox.showinfo('внимание', 'запись изменена')
            else:
                file.write(lines[l])
    menubat0(i, 1)


def change_n(name, tara, i,j,old):
    #global
    with open('tabl.txt', 'r') as f:
        st = f.readlines()
        str = name + ' ' + tara
        print(str)
        for line in st:
            sovpad = re.search(str, line)
            if sovpad:
                print('строка : ' + line)
                li = line
                s = line.split()
                print(s)
    print('старое: '+ old)
    print(s)
    print('строка : ' + li)
    print(li[6])
    new = entry0[i+1, j].get()
    print('заменяем на новое: '+ new)
    with open('tabl.txt', 'r') as file1, open('tabl.txt', 'r') as file:
        f_old = file1.read()
        #print(f_old)
        lines = file.readlines()
        #print(lines)
        for l in lines:
            #print(li)
            if li == l:
                print(li + '\n')
                #s2_new = re.sub(old, new, l)
                # file.write(s2_new)
                old_l = l.split()
                old_l[j-1] = new
                s2_new = ' '.join(old_l)
                print('старая строка : ' + l)
                print('новая строка : ' + s2_new)
                new_f = f_old.replace(l, s2_new + '\n')
                with open('tabl.txt', 'w') as f:
                    f.write(new_f)
                    #print(new_f)
                    messagebox.showinfo('внимание', 'запись изменена')

    menubat0(i, 1)
    #change_n(num_line, column, old)

def change_name(a, num_line, column):
    if messagebox.askokcancel('внесение', 'хотите изменить : %s' % a):
        old = entry0[num_line+1, column].get()
        name = entry0[num_line + 1, 2].get()
        tara = entry0[num_line + 1, 3].get()
        print('staroe',old)
        print(name)
        entry0[num_line+1, column].focus()
        entry0[num_line+1, column].delete('0', END)
        entry0[num_line+1, column].bind('<Return>', lambda et: change_n(name, tara, num_line, column, old))
#ввод строки в таблицу на первой вкладке, на поиске
#but[num_lines+1, 0].config(command=lambda: tabl(num_lines))
def inf():
    messagebox.showinfo('внимание', "строка внесена")
    vvod_search.unbind('<KeyRelease>')
    if vvod_search.get() == "":
        vvod_search.insert(0, "очистите таблицу")
    else:
        vvod_search.delete("0", END)
        vvod_search.insert(0, "обновите")

def vnos(num_lines):
    try:
        i = num_lines+1
        with open('tabl.txt', 'r') as f:
            l = f.read()
            sp = l.splitlines()
            print(sp)
            #new_sp = sp.pop(len(sp)-1)
            #print(new_sp[-1])
            last_l = sp[-1].split()
            print(int(last_l[0])+1)
            n = int(last_l[0])+1
        entry0[i, 1].insert(0, str(n))
        inputt(i, 1)
        entry0[i, 2].focus()
        #entry0[i, 1].bind("<Return>", lambda e: (inputt(i, 1), entry0[i, 2].focus()))
        entry0[i, 2].bind("<Return>", lambda e: (inputt(i, 2), entry0[i, 3].focus()))
        entry0[i, 3].bind("<Return>", lambda e: (inputt(i, 3), entry0[i, 4].focus()))
        entry0[i, 4].bind("<Return>", lambda e: (inputt(i, 4), entry0[i, 5].focus()))
        entry0[i, 5].bind("<Return>", lambda e: (inputt(i, 5), entry0[i, 6].focus()))
        entry0[i, 6].bind("<Return>", lambda e: (inputt(i, 6), entry0[i, 7].focus()))
        entry0[i, 7].bind("<Return>", lambda e: (inputt(i, 7), inf()))
        but0[num_lines+2, 0].config(command=lambda: tabl(num_lines+1))
    except IndexError:
        messagebox.showwarning('внимание', 'удалите из файла пустую строку в конце')
# курсор в файле должен быть в начале строки без пробела
def tabl(num_lines):
    if entry0[num_lines+1, 1].get() == '':
        if messagebox.askokcancel('внесение', 'хотите внести запись'):
            vnos(num_lines)
    else:
        messagebox.showwarning('внимание', 'обновите таблицу, \nчтобы внести запись')
def inputt(i, j):
    global zapisej
    #print('here')
    s = entry0[i, j].get()
    if j == 7:
        s1 = s

        k = 2
        n = 0
        while entry0[k, 1].get() != '':
            n = n + 1
            k = k + 1
            print(n)
            print(k)

        zapisej = n
        print('zapisej=', zapisej)

    elif j == 1:
        s1 = ' \n' + s + ' '
    else:
        s1 = s + ' '
    try:
        file = open("tabl.txt", "a")#, encoding='utf-8')
        try:
            file.write(s1)
            #print(s1)
        finally:
            file.close()

    except FileNotFoundError:
        print("Невозможно открыть файл")



# показ, где находится растение

#заполняем первую вкладку для поиска
entry0 = {}
menubut0 = {}
but0 = {}
for i in range(18):
    for j in range(9):
        if i == 0 or j == 0:
            but0[(i, j)] = Button(canvas_search, width=10, bg='LightSteelBlue', fg='Black', justif="left",
                                 font=('Arial', 10, 'bold'), text='%s' % i + '/' + '%s' % j)
            but0[i, j].grid(row=i, column=j)

            if j == 5 or j == 4:
                but0[i, j].config(width=20)
            if j == 2:
                but0[i, j].config(width=34)

            if j == 3 or j == 6:
                but0[i, j].config(width=6 + 4 + 3)
            if j == 7 or j == 8 or j == 9 or j == 10 or j == 11:
                but0[i, j].config(width=6 + 4)
        else:
            entry0[(i, j)] = Entry(canvas_search, width=7, fg='blue',
                                  font=('Arial', 16, ''))
            entry0[i, j].grid(row=i, column=j)
            # self.entry[i,j].insert(0, plant[i][j])
            if i == 1:
                entry0[i, j].config(justif="center", bg="yellow", font=('Arial', 16, 'bold'), fg="green")
            if j == 1 or j == 4 or j == 5:
                entry0[i, j].config(justif='center')
            if j == 5 or j == 4:
                entry0[i, j].config(width=14)
            if j == 2:
                entry0[i, j].config(width=23)
            if j == 1:
                entry0[i, j].config(width=7)
            if j == 3 or j == 6:
                entry0[i, j].config(width=9, justif='center')
            if j == 7 or j == 8 or j == 9 or j == 10 or j == 11:
                entry0[i, j].config(width=7)

entry0[1, 1].insert(0, '№')
entry0[1, 2].insert(0, 'наименование')
entry0[1, 3].insert(0, 'тара')
entry0[1, 4].insert(0, 'расположение')
entry0[1, 5].insert(0, 'количество')
entry0[1, 6].insert(0, 'цена')
entry0[1, 7].insert(0, 'продано')

but0[0, 2].config(text='всего наименований товара: ' + str(len(count)-2))
but0[2, 0].config(command=lambda: tabl(1))#886 строка
but0[0, 4].config(command=total_chek, text='total_sum')
def rew_kalkulator():
    os.startfile('kalkulator.txt')
but0[0, 1].config(command=rew_kalkulator)
but0[0, 3].config(command=total_kalkuiator, text='kalk')

tabl_full = False
def poisk(m):
    global zapisej, tabl_full
    try:
        #m = vvod_search.get()
        t = 0
        listbox.place_forget()
        listbox_values.set('')
        if tabl_full == False:
            with open('tabl.txt', 'r') as f:
                for i in range(num_lines):
                    s = f.readline()
                    name_sovp = re.search(m, s)
                    name_sovp1 = re.search(m.title(), s)
                    if name_sovp or name_sovp1:
                        sp1 = s.split()
                        #print(sp1)
                        t = t + 1
                        if t <= 16:
                            for j2 in range(1, len(sp1)):
                                #entry0[t + 1, j2 + 1].delete('0', END)
                                # entry[i3 + 1, j2 + 1].insert(0, sp1[j2])
                                entry0[t+1, j2 + 1].insert(0, sp1[j2])
                                menubat0(t, 1)
                                t1 = t
                            entry0[t+1, 1].insert(0, t)
                        else:
                            for j2 in range(1, len(sp1)):
                                entry0[t + 1, j2 + 1].grid(row=t + 1, column=j2 + 1)
                                # entry[i3 + 1, j2 + 1].insert(0, sp1[j2])
                                entry0[t + 1, j2 + 1].insert(0, sp1[j2])
                                menubat0(t, 1)
                                t1 = t
                            entry0[t + 1, 1].insert(0, t)
                zapisej = t
                print(t)
                #print(t1)
                tabl_full = True
                if t == 0:
                    messagebox.showinfo('внимание', 'данного товара нет в наличии')
                    tabl_full = False
                #print(menubuts)
        else:
            messagebox.showinfo('внимание','обновите таблицу')
    except KeyError:
        messagebox.showwarning('внимание', 'превышение строк списка')
        for i in range(2, 18):
            for j in range(1, 8):
                entry0[i, j].delete('0', END)
        delbut()
l_search = Label(canvas_foto, text='Введите название растения:', bg ='lightblue', fg='blue', font=('Arial', 20, 'bold'))
l_search.place(x=1, y=1)#y=150

def uptabl():
    global zapisej, tabl_full, lst, lst2
    tabl_full = False
    vvod_search.delete('0', END)
    listbox.place_forget()
    vvod_search.bind('<KeyRelease>', check_input)
    with open('tabl.txt', 'r') as f:
        l = f.read()
        lst = []
        lst2 = []
        count = l.splitlines()
        for i in range(1, len(count) - 1):
            sf = count[i].split()
            lst.append(sf[1])
            lst2.append(sf[1] + ' ' + sf[2])
    try:
        #vvod_search.bind('<KeyRelease>', check_input)
        for i in range(2, zapisej+2):
            for j in range(1, 8):
                entry0[i, j].delete('0', END)
    except NameError:
        messagebox.showinfo('внимание', 'действие выполнить нельзя!')


def delbut():
    for w in canvas_search.winfo_children():
        if w.winfo_class() == "Menubutton":
            w.destroy()


uptablb = Button(canvas_foto, width=18, text='очистить таблицу',bg='lightblue', command=lambda :(uptabl(),delbut()),fg='blue', bd=0 ,font=('Arial', 16, 'bold'))
uptablb.place(x=800, y=150)
rewtablb = Button(canvas_foto, width=4, text='tabl',bg='lightblue', command=lambda :rew_tabl(),fg='blue', bd=0 ,font=('Arial', 16, 'bold'))
#rewtablb.place(x=1050, y=150)
but0[0, 0].config(command=lambda :rew_tabl())# открывает файл с таблицей
def check_input(_event=None):
    value = vvod_search.get().lower()
    #listbox.place_forget()
    vvod_search.focus()
    if value == '':
        listbox_values.set('')
        listbox.place_forget()

    else:
        data = []
        for item in lst:
            if value.lower() in item.lower():
                data.append(item)
                listbox.place(x=400,y=30)
                vvod_search.focus()
                listbox_values.set(data)

entry_text = StringVar()
vvod_search = Entry(canvas_foto,  width=20, fg='black', font=('Arial', 20, 'bold'), textvariable=entry_text)
vvod_search.place(x=400, y=1)#y=150
#vvod_search = Entry(root, textvariable=entry_text)
vvod_search.bind('<KeyRelease>', check_input)
#vvod_search.place(x=5, y=5)
vvod_search.focus()
#vvod_search.bind('<Return>', poisk)
def on_change_selection(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        entry_text.set(data)
        poisk(data)
        check_input()
        listbox.delete(0, 2)
        listbox.place_forget()
        vvod_search.unbind('<KeyRelease>')
        #check_input()
listbox_values = Variable()
listbox = Listbox(canvas_foto, listvariable=listbox_values, width=20, fg='black', font=('Arial', 14, 'bold'))
listbox.bind('<<ListboxSelect>>', on_change_selection)
listbox_values.set(lst)

root.mainloop()