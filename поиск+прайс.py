from tkinter import *
from tkinter import ttk, messagebox, filedialog
import math
import datetime
import re
import os
from idlelib.tooltip import Hovertip
#создаём окно
root = Tk()
root.title("фазенда")
root.geometry("700x380+5+5")#1300x460+200+2
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
            os.startfile(dirname + '\\tabel.txt')
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
            os.startfile(dirname + '\\tabel2.txt')
            win.destroy()
        else:
            lv.config(text='Неверный пароль!!!')
            lv.place(x=5, y=50)
            print('Код неверный..!!!')

    e.bind('<Return>', vvod)
#создаём меню

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
notebook.add(frame1, text="<ПОИСК РАССТЕНИЙ>", compound=LEFT)
notebook.add(frame3, text="<ПРАЙС>", compound=LEFT)# image=python_logo,

#создаём холсты для прайса
canvas5 = Canvas(frame3, width=184, height=100, borderwidth=0, background="gray")
canvas5.pack(side="top", fill="both", expand=False)
ph3 = PhotoImage(file='fazenda2.png')
canvas5.create_image(400, 200, image=ph3)
canvas6 = Canvas(frame3, width=184, height=250, borderwidth=0, background="lightgray")
canvas6.pack(side="top", fill="both", expand=False)

#для поиска
canvas7 = Canvas(frame1, width=184, height=160, borderwidth=0, background="gray")
canvas7.pack(side="right", fill="both", expand=False)
ph = PhotoImage(file='fazenda1.png')
canvas7.create_image(500, 483, image=ph)
canvas8 = Canvas(frame1, width=300, height=140, borderwidth=0, background="green")
canvas8.pack(side="top", fill="both", expand=False)
ph2 = PhotoImage(file='fazenda2.png')
canvas8.create_image(600, 200, image=ph2)
canvas9 = Canvas(frame1, width=200, height=460, borderwidth=0, background="lightblue")
canvas9.pack(side="left", fill="both", expand=True)


can00 = Canvas(canvas9, width=30)
#can00.pack(side="top", fill="x", expand=False)
can = Canvas(canvas9)

#создаём полосу прокрутки для холста для frame8 and canvas9 для табеля
vsb20 = Scrollbar(canvas9, orient="horizontal")
vsb20.pack(side="bottom", fill="x", expand=False)
can.configure(xscrollcommand=vsb20.set)
vsb20.configure(command=can.xview)
vsb8 = Scrollbar(canvas9, orient="vertical")
vsb8.pack(side="right", fill="y", expand=False)
can.configure(yscrollcommand=vsb8.set)
vsb8.configure(command=can.yview)

can.pack(side="left", fill="both", expand=True)

#создаём фрэйм для виджетов на холсте, чтобы их прокручивать
scrolled_frame8 = Frame(can, background=can.cget('bg'))
can.create_window((4, 4), window=scrolled_frame8, anchor="nw")
def on_configure8(event):
    """Set the scroll region to encompass the scrolled frame"""
    can.configure(scrollregion=can.bbox("all"))
scrolled_frame8.bind("<Configure>", on_configure8)
#frame3 and canvas9 для кассового чека создаём поля для ввода ввиде таблиц
#открываем файл для чтения количества строк
def count1(file):
    global count, num_lines, lst
    try:
        try:
            with open(file, 'r') as a:
                l = a.read()
                count = l.splitlines()  # count-список из строк файла
                num_lines = len(count)
                print('count--', count)
                lst = []
                print(len(count))
                for i in range(len(count)):
                    sf = count[i].split()
                    lst.append(sf[1])
                # without_last = count.pop(len(count)-1)
        except FileNotFoundError:
            print('внимание', f'создайте файл {file} ')
    except IndexError:
        messagebox.showinfo('внимание', 'что-то с файлом "tabl.txt"')

count1('tabl.txt')

counts = count
#print(counts)
def price(vid):
    global canvas6
    names = ["№№", "name", "tara", "place", "col", "price"]
    columns = count[0].split()
    counts2 = counts.pop(0)
    new_sp_tovara = []
    print(len(counts))
    def get_name(element):
        return element[1]
    if vid == ' ':
        for i in range(len(counts)):
            co = counts[i].split()
            new_sp_tovara.append(co)
        new_sp_tovara.sort(key=get_name)
        for i in range(len(counts)):
            new_sp_tovara[i][0] = str(i + 1)

    elif vid == 'кашпо':
        for i in range(len(counts)):
            co = counts[i].split()
            if co[2] == 'ка23' or co[2] == 'ка26' or co[2] == 'ка19':
                new_sp_tovara.append(co)
        new_sp_tovara.sort(key=get_name)
        for i in range(len(new_sp_tovara)):
            new_sp_tovara[i][0] = str(i + 1)

        #print(co)
        #print(new_sp_tovara)




    print(columns)# определяем столбцы
    #print(new_sp_tovara)
    tree = ttk.Treeview(canvas6, columns=names, height=18, show="headings")
    # определяем заголовки
    tree.heading("№№", text=columns[0], anchor=N)
    tree.heading("name", text=columns[1], anchor=N)
    tree.heading("tara", text=columns[2], anchor=N)
    tree.heading("place", text=columns[3], anchor=N)
    tree.heading("col", text=columns[4], anchor=N)
    tree.heading("price", text=columns[5], anchor=N)
    style = ttk.Style()
    style.configure(".", font=('Helvetica', 10, 'bold'), bg='lightgreen', foreground="orange")
    style.configure("Treeview", font=('Helvetica', 16), rowheight=26, foreground='green', anchor=N )
    style.configure("Treeview.Heading", font=('Helvetica', 20, 'bold'), foreground='red')
    # добавляем вертикальную прокрутку
    xscrollbar = ttk.Scrollbar(canvas6, orient='horizontal', command=tree.xview)
    tree.configure(xscroll=xscrollbar.set)
    xscrollbar.pack(side="bottom", fill="x", expand=True)
    yscrollbar = ttk.Scrollbar(canvas6, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=yscrollbar.set)
    yscrollbar.pack(side="right", fill="y", expand=True)
    tree.pack(side="left", fill="both", expand=True)
    tree.column("#1", stretch=NO, width=60, anchor=N)
    tree.column("#2", stretch=NO, width=250)
    tree.column("#3", stretch=NO, width=100, anchor=N)
    tree.column("#4", stretch=NO, width=100, anchor=N)
    tree.column("#5", stretch=NO, width=80, anchor=N)
    tree.column("#6", stretch=NO, width=100, anchor=N)
    # добавляем данные
    for plant in new_sp_tovara:
        tree.insert("", END, values=plant)
def price_show():
    global canvas6
    canvas6.pack()
def price_del():
    global canvas6
    canvas6.pack_forget()
#price('кашпо')
bt_price = Button(canvas5, text='овощ. рассада ', command=price('рассада'), bg ='lightblue', fg='blue', bd=0, font=('Arial', 16, 'bold'))
bt_price.place(x=300, y=10)
bt_price = Button(canvas5, text='овощ. рассада ', command=price('кашпо'), bg ='lightblue', fg='blue', bd=0, font=('Arial', 16, 'bold'))
bt_price.place(x=300, y=50)
bt_price = Button(canvas5, text='показать прайс', command=price_show, bg ='lightblue', fg='blue', bd=0, font=('Arial', 16, 'bold'))
bt_price.place(x=10, y=10)
bt_price_del = Button(canvas5, text='скрыть прайс', command=price_del, bg ='lightblue', fg='blue', bd=0, font=('Arial', 16, 'bold'))
bt_price_del.place(x=10, y=50)
#заполняем первую вкладку для поиска
entry0 = {}
menubut0 = {}
but0 = {}
for i in range(28):
    for j in range(8):
        if j == 0:
            but0[(i, j)] = Button(scrolled_frame8, width=6, bg='LightSteelBlue', fg='Black', justif="left",
                                 font=('Arial', 8, 'bold'), text='%s' % i)
            but0[i, j].grid(row=i, column=j)
            #myTip = Hovertip(but0[i, 0], 'подсказка')
        else:
            entry0[(i, j)] = Entry(scrolled_frame8, width=7, fg='blue',
                                  font=('Arial', 12, ''))
            entry0[i, j].grid(row=i, column=j)
            # self.entry[i,j].insert(0, plant[i][j])
            if i == 0:
                entry0[i, j].config(justif="center", bg="yellow", font=('Arial', 12, 'bold'), fg="green")
            if j == 0 or j == 5 or j == 4:
                entry0[i, j].config(justif='center')
            if j == 5:
                entry0[i, j].config(width=14)
            if j == 1:
                entry0[i, j].config(width=23)
            if j == 0:
                entry0[i, j].config(width=7)
            if j == 2 or j == 4 or j == 3:
                entry0[i, j].config(width=9, justif='center')
            if j == 6 or j == 7 or j == 8 or j == 9 or j == 10:
                entry0[i, j].config(width=7)
            if j == 6:
                entry0[i, j].config(width=14)

entry0[0, 1].insert(0, 'наименование')
entry0[0, 2].insert(0, 'тара')
entry0[0, 4].insert(0, 'place')
entry0[0, 5].insert(0, 'кол.на нач2024')
entry0[0, 3].insert(0, 'цена')
entry0[0, 6].insert(0, 'кол.на кон2024')
but0[0, 0].config(text='№№')

menubuts = {}
def menubats(i, j):
    global menubuts, optionss
    menubuts[(i, 6)] = Menubutton(scrolled_frame8, bg="orange", width=2, text='v', activebackground='blue',
                                      justify='center')#activeforeground='blue',
    optionss = Menu(menubuts[i, 6])
    menubuts[i, 6].config(menu=optionss)
    if i != 0:
        a = entry0[i, 1].get()  # название
        tara = entry0[i, 2].get()  # тара
        p = entry0[i, 3].get()  # расположение
        col = entry0[i, 4].get()  # количество
        c = entry0[i, 5].get()  # цена
        #print('в строке ', i + 1, a)
        optionss.add_command(label='показать, где ' + a, command=lambda: show(a, p, i, col, tara, c))
        optionss.add_command(label='добавить в накладную ' + '"' + a + '"', command=lambda: (nakl(a, c, tara, p)))
        #optionss.add_command(label='добавить в товарный чек' + '"' + a + '"')
    menubuts[i, 6].grid(row=i, columns=3)

#кнопки меню для изменения данных в прайсе
menubut = {}
def menubat0(i, j):
    menubut[(i, 4)] = Menubutton(scrolled_frame8, bg="orange", width=2, text='v', activebackground='blue',
                                     justify='center')
    options = Menu(menubut[i, 4])
    menubut[i, 4].config(menu=options)
    if i != 0:
        a = entry0[i, 1].get()
        #print('в строке ', i + 1, a)
        #a = entry[i + 1, 2].get()
        c = entry0[i, 5].get()
        t = entry0[i, 2].get()
        p = entry0[i, 3].get()
        col = entry0[i, 4].get()
        #print('в строке ', i + 1, a)
        #n = entry[i, 2].get()
        options.add_command(label='изменить название : ' + a, command=lambda: change_name(a, i, 1, a, t))
        options.add_command(label='изменить тару :' + t, command=lambda: change_name(t, i, 2, a, t))
        options.add_command(label='изменить цену :' + p, command=lambda: change_name(p, i, 3, a, t))
        options.add_command(label='изменить place :' + col,command=lambda: change_name(col, i, 4, a, t))
        options.add_command(label='изменить количество :' + c, command=lambda: change_name(c, i, 5, a, t))
    menubut[i, 4].grid(row=i, columns=5)
def change_n(i,j,old, name, tara):
    #global
    print('старое: ' + old)
    st = name + ' ' + tara
    new = entry0[i, j].get()
    print('заменяем на новое: ' + new)
    with open('tabl.txt', 'r') as file1, open('tabl.txt', 'r') as file:
        f_old = file1.read()
        #print(f_old)
        lines = file.readlines()
        print(lines)
        for l in lines:
            name_sovp = re.search(st, l)
            name_sovp1 = re.search(st.title(), l)
            if name_sovp or name_sovp1:
                s2_new = re.sub(old, new, l)
                # file.write(s2_new)
                print('старая строка : ' + l)
                print('новая строка : ' + s2_new)
                new_f = f_old.replace(l, s2_new)
                with open('tabl.txt', 'w') as f:
                    f.write(new_f)
                    #print(new_f)
                    messagebox.showinfo('внимание', 'запись изменена')
    menubat0(i, 1)
    #change_n(num_line, column, old)
def change_name(men, num_line, column, name, tara):
    if messagebox.askokcancel('внесение', 'хотите изменить : %s' % men):
        old = entry0[num_line, column].get()
        entry0[num_line, column].focus()
        entry0[num_line, column].delete('0', END)
        entry0[num_line, column].bind('<Return>', lambda et: change_n(num_line, column, old, name, tara))
        #print(n)
#ввод строки в таблицу на первой вкладке, на главном прайс-листе
but0[1, 0].config(command=lambda: tabl(1))
def inf():
    messagebox.showinfo('внимание', "строка внесена")
def vnos(num_lines):
    i = num_lines
    with open('tabl.txt', 'r') as f:
        l = f.read()
        sp = l.splitlines()
        print(sp)
        print(sp[-1])
        last_l = sp[-1].split()
        print(int(last_l[0])+1)
        n = int(last_l[0])+1
    try:
        file = open("tabl.txt", "a")#, encoding='utf-8')
        try:
            file.write('\n' + str(n) + ' ')
        finally:
            file.close()
    except FileNotFoundError:
        print("Невозможно открыть файл")
    entry0[i, 1].focus()
    entry0[i, 1].bind("<Return>", lambda e: (inputt(i, 1), entry0[i, 2].focus()))
    entry0[i, 2].bind("<Return>", lambda e: (inputt(i, 2), entry0[i, 3].focus()))
    entry0[i, 3].bind("<Return>", lambda e: (inputt(i, 3), entry0[i, 4].focus()))
    entry0[i, 4].bind("<Return>", lambda e: (inputt(i, 4), entry0[i, 5].focus()))
    entry0[i, 5].bind("<Return>", lambda e: (inputt(i, 5), entry0[i, 6].focus()))
    entry0[i, 6].bind("<Return>", lambda e: (inputt(i, 6), entry0[i, 7].focus()))
    entry0[i, 7].bind("<Return>", lambda e: (inputt(i, 7), inf()))
    but0[num_lines+1, 0].config(command=lambda: tabl(num_lines+1))
# курсор в файле должен быть в начале строки без пробела
def tabl(num_lines):
    if messagebox.askokcancel('внесение', 'хотите внести запись'):
        vnos(num_lines)
def inputt(i, j):
    #print('here')
    s = entry0[i, j].get()
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

#поиск по названию
tabl_full = False
def poisk(m, file):
    global zapisej, tabl_full, myTip
    t = 0
    listbox2.place_forget()
    listbox2_values.set('')
    if tabl_full == False:
        with open(file, 'r') as f:
            for i in range(num_lines):
                s = f.readline()
                name_sovp = re.search(m, s)
                name_sovp1 = re.search(m.title(), s)
                if name_sovp or name_sovp1:
                    sp1 = s.split()
                    t = t + 1
                    if t <= 28:
                        for j2 in range(1, len(sp1)):
                            entry0[t, j2].insert(0, sp1[j2])
                            #menubats(t, 1)
                            menubat0(t, 1)
            zapisej = t
            print(t)
            tabl_full = True
            if t == 0:
                messagebox.showinfo('внимание', 'данного товара нет в наличии')
                tabl_full = False
    else:
        messagebox.showinfo('внимание', 'очистите таблицу')
        for i in range(2, 18):
            for j in range(1, 8):
                entry0[i, j].delete('0', END)
       # delbut()
    for i in range(1, 28):
        for j in range(2, 8):#всплывающая_подсказка
            myTip = Hovertip(entry0[i, j], entry0[i, 1].get() + ' ' + entry0[0, j].get() + ': ' + entry0[i, j].get())
def uptabl():
    global zapisej, tabl_full, lst, lst2
    tabl_full = False
    vvod_search2.delete('0', END)
    listbox2.place_forget()
    vvod_search2.bind('<KeyRelease>', check_input2)
    delbutn()
    listbox2.bind('<<ListboxSelect>>', on_change_selection2)
    try:
        #vvod_search.bind('<KeyRelease>', check_input)
        for i in range(1, zapisej+2):
            for j in range(1, 8):
                entry0[i, j].delete('0', END)
    except NameError:
        messagebox.showinfo('внимание', 'действие выполнить нельзя!')

def delbutn():
    for w in scrolled_frame8.winfo_children():
        if w.winfo_class() == "Menubutton":
             w.destroy()
l_search = Label(canvas8, text='Введите название расстения:', bg ='lightblue', fg='blue', font=('Arial', 16, 'bold'))
l_search.place(x=5, y=10)#y=150
uptablb = Button(canvas8, width=16, text='очистить таблицу', bg='lightblue', command=lambda: uptabl(), fg='blue', bd=0 ,font=('Arial', 16, 'bold'))
uptablb.place(x=5, y=100)
def check_input2(_event=None):
    value = vvod_search2.get().lower()
    #listbox.place_forget()
    vvod_search2.focus()
    if value == '':
        listbox2_values.set('')
        listbox2.place_forget()
    else:
        data = []
        for item in lst:
            if value.lower() in item.lower():
                data.append(item)
                listbox2.place(x=320, y=40)
                vvod_search2.focus()
                listbox2_values.set(data)
entry_text2 = StringVar()
vvod_search2 = Entry(canvas8,  width=15, fg='black', font=('Arial', 16, 'bold'), textvariable=entry_text2)
vvod_search2.place(x=320, y=10)
vvod_search2.bind('<KeyRelease>', check_input2)
#vvod_search.bind('<Return>', poisk)
def on_change_selection2(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        entry_text2.set(data)
        poisk(data, 'tabl.txt')
        check_input2()
        listbox2.delete(0, 2)
        listbox2.place_forget()
        vvod_search2.unbind('<KeyRelease>')
listbox2_values = Variable()
listbox2 = Listbox(canvas8, listvariable=listbox2_values, width=20, fg='black', font=('Arial', 14, 'bold'))
listbox2.bind('<<ListboxSelect>>', on_change_selection2)
listbox2_values.set(lst)
root.mainloop()
