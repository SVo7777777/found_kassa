from tkinter import *
from tkinter import ttk, messagebox, filedialog
import math
import datetime
import re
import os

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
notebook.add(frame1, text="<ТАБЕЛЬ РАБОТНИКОВ>", compound=LEFT)
notebook.add(frame3, text="<пусто>", compound=LEFT)# image=python_logo,

#создаём холсты
#для поиска




#для табеля
canvas7 = Canvas(frame1, width=84, height=160, borderwidth=0, background="gray")
canvas7.pack(side="right", fill="both", expand=False)
ph = PhotoImage(file='fazenda1.png')
canvas7.create_image(500, 483, image=ph)
canvas8 = Canvas(frame1, width=300, height=140, borderwidth=0, background="green")
canvas8.pack(side="top", fill="both", expand=False)
ph2 = PhotoImage(file='fazenda2.png')
canvas8.create_image(600, 200, image=ph2)

vsb80 = Scrollbar(frame1, orient="vertical")
vsb80.pack(side="left", fill="y", expand=True)
canvas90 = Canvas(frame1, width=500, height=460, borderwidth=0, background="lightblue")#
canvas90.pack(side="left", fill="both", expand=True)
canvas9 = Canvas(frame1, width=150, height=460, borderwidth=0, background="lightblue")
canvas9.pack(side="left", fill="both", expand=True)
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
                    lst.append(sf[0])
                # without_last = count.pop(len(count)-1)
        except FileNotFoundError:
            print('внимание', f'создайте файл {file} ')
    except IndexError:
        messagebox.showinfo('внимание', 'табель пустой')


canvas90.configure(yscrollcommand=vsb80.set)
vsb80.configure(command=canvas90.yview)
#создаём фрэйм для виджетов на холсте, чтобы их прокручивать
scrolled_frame80 = Frame(canvas90, background=canvas90.cget('bg'))
canvas90.create_window((4, 4), window=scrolled_frame80, anchor="nw")
def on_configure80(event):
    """Set the scroll region to encompass the scrolled frame"""
    canvas90.configure(scrollregion=canvas90.bbox("all"))
scrolled_frame80.bind("<Configure>", on_configure80)
color = ['lightsalmon', 'springgreen', 'khaki', 'aquamarine', 'pink', 'gold', 'plum', 'skyblue', 'yellowgreen', 'burlywood', 'aqua']
#заполняем  вкладку для табеля
entry90 = {}
but90 = {}
for i in range(11):
    for j in range(2):
        if j == 0:
            but90[(i, j)] = Button(scrolled_frame80, width=1, bg='LightSteelBlue', fg='Black', justif="left",
                                  font=('Arial', 8, 'bold'), text='%s' % i)  # + '/' + '%s' % j)
            but90[i, j].grid(row=i, column=j)


        else:
            entry90[(i, j)] = Entry(scrolled_frame80, width=2, name='e' + str(i) + str(j), fg='blue', justif='center', bg=color[i],
                                   font=('Arial', 14,''))
            entry90[i, j].grid(row=i, column=j)


            if i == 0:
                entry90[i, j].insert(0, '%s' % (j - 1))
                entry90[i, j].config(font=('Arial', 14, 'bold'), bg='green', fg='white')
            if j == 1:
                entry90[i, j].config(width=15, justif='left')

entry0 = {}
menubut0 = {}
but0 = {}
sum_hour = []
names_entry = []
for i in range(11):
    for j in range(33):
        entry0[(i, j)] = Entry(scrolled_frame8, width=2, name='e' + str(i) + str(j), fg='blue', justif='center',
                               font=('Arial', 14, ''), bg=color[i])
        entry0[i, j].grid(row=i, column=j)

        names_entry.append(str(entry0[i, j]))
        if i == 0:
            entry0[i, j].insert(0, '%s' % (j + 1))
            entry0[i, j].config(font=('Arial', 14, 'bold'), bg='green', fg='white')
        if j == 31:
            entry0[i, j].config(width=6)
        if j == 31 and i != 0:
            entry0[i, j].config(fg='red')
        if i > 0 and j == 32:
            entry0[i, j].config(fg='white')
        if j == 32:
            entry0[i, j].config(width=10)
        if j == 32 and i != 0:
            entry0[i, j].config( bg='white')           
    sum_hour.append(0)
print(sum_hour)
#print(names_entry)
def svtabl(file1):
    if messagebox.askokcancel('сохранение ', 'Вы уверены, что хотите сохранить?'):
        with open('tabel2.txt', 'w') as f:
            f.truncate()
        for i in range(1, 10):
            el = entry90[i, 1].get()
            with open('tabel2.txt', 'a+') as f:
               f.write(el + ' ')
            for j in range(31):

               if entry0[i, j] == '':
                   break
               else:
                   el = entry0[i, j].get()
                   with open('tabel2.txt', 'a+') as f:
                       f.write(el + ' ')

            if entry0[i+1, 1].get() == '':
                break
            else:
                with open('tabel2.txt', 'a+') as f:
                    f.write('\n')
        messagebox.showinfo('сохранение', "табель успешно сохранён!")

        with open('tabel2.txt', 'r') as f, open(file1, 'w') as file:
            fi = f.read()
            file.truncate()
            file.write(fi)

def summer(en):
    global sum_hour
    try:
        e = en.get()
        print('введенное: ', e)
        print(sum_hour)
        ind = int(str(en)[43:44])#имя виджета:.!notebook.!frame.!canvas3.!frame.e225
        print('индекс: ',ind)
        sum_hour[ind] = sum_hour[ind] + int(e)
        print(sum_hour)
        entry0[ind, 31].delete('0', END)
        entry0[ind, 31].insert(0, f'{sum_hour[ind]}')
        entry0[ind, 32].delete('0', END)
        entry0[ind, 32].insert(0, f'{sum_hour[ind] * 200}')
        print(str(en)[43:44])
    except ValueError:
        print('это не число')
def focus1(t):
    try:
        widget = root.focus_get()
        print(widget, "has focus")
        print(t)
        print(widget.nametowidget(widget))#имя виджета
        print(names_entry.index(str(widget.nametowidget(widget))))#индекс в списке имен
        print(names_entry[names_entry.index(str(widget.nametowidget(widget)))+1])#следующий в списке имён
        n = names_entry[names_entry.index(str(widget.nametowidget(widget)))+1]
        widget.bind('<Return>', lambda e: (scrolled_frame8.nametowidget(n).focus(), focus1(t), summer(widget)))#переход фокуса в следующий энтри
    except ValueError:
        print('это не  энтри')
root.bind_all("<Button-1>", lambda e: focus1(t))
t = 0
entry90[0, 1].delete('0', END)
entry90[0, 1].insert(0, 'ФИО сотрудника')
entry90[0, 1].config(width=15, justif='center')
entry0[0, 31].delete('0', END)
entry0[0, 31].insert(0, 'всего')
entry0[0, 31].config(width=6)
entry0[0, 32].delete('0', END)
entry0[0, 32].insert(0, 'з/п')
but90[0, 0].config(text='№№')
def change_color():
    for i in range(1, 11):
        entry0[i, 32].config(fg='red', font=('Arial', 16, 'bold'))

tabl_full = False
def poisk(m, file):
    global zapisej, tabl_full, sum_hour
    try:
        t = 0
        count1(file)
        save_tablb.config(command=lambda: (svtabl(file)))
        if tabl_full == False:
            with open(file, 'r') as f:
                for i in range(num_lines):
                    s = f.readline()
                    if m != '':
                        name_sovp = re.search(m, s)
                        name_sovp1 = re.search(m.title(), s)
                        if name_sovp or name_sovp1:
                            sp1 = s.split()
                            #print(sp1)
                            t = t + 1
                            hour = []
                            if t <= 16:
                                entry90[t, 1].insert(0, sp1[0])
                                for j2 in range( 1, len(sp1)):
                                    #entry0[t + 1, j2 + 1].delete('0', END)
                                    # entry[i3 + 1, j2 + 1].insert(0, sp1[j2])
                                    entry0[t, j2-1].insert(0, sp1[j2])
                                    if sp1[j2] != '-':
                                        hour.append(int(sp1[j2]))
                                    #menubat0(t-1, 1, sp1)
                                    t1 = t
                                #entry0[t, 1].insert(0, sp1[0])
                                entry0[t, 31].delete('0', END)
                                entry0[t, 31].insert(0, math.fsum(hour))
                                sum_hour[t] = math.fsum(hour)
                                entry0[t, 32].delete('0', END)
                                entry0[t, 32].insert(0, f'{sum_hour[t] * 200}')

                            else:
                                for j2 in range(1, len(sp1)):
                                    entry0[t + 1, j2 + 1].grid(row=t + 1, column=j2 + 1)
                                    # entry[i3 + 1, j2 + 1].insert(0, sp1[j2])
                                    entry0[t, j2 -11].insert(0, sp1[j2])
                                    #menubat0(t-1, 1, sp1)
                                    t1 = t
                                #entry0[t, 1].insert(0, sp1[0])
                                entry0[t, 31].delete('0', END)
                                entry0[t, 31].insert(0, math.fsum(hour))

                                sum_hour[t] = math.fsum(hour)
                                entry0[t, 32].delete('0', END)
                                entry0[t, 32].insert(0, f'{sum_hour[t] * 200}')
                    else:
                        sp1 = s.split()
                        #print(sp1)
                        t = t + 1
                        hour = []
                        for j2 in range(1, len(sp1)):
                            # entry0[t + 1, j2 + 1].delete('0', END)
                            # entry[i3 + 1, j2 + 1].insert(0, sp1[j2])
                            entry0[t, j2 - 1].insert(0, sp1[j2])
                            if sp1[j2] != '-':
                                hour.append(int(sp1[j2]))
                            #menubat0(t - 1, 1, sp1)
                            t1 = t
                        entry90[t, 1].insert(0, sp1[0])
                        entry0[t, 31].delete('0', END)
                        entry0[t, 31].insert(0, math.fsum(hour))
                        sum_hour[t] = math.fsum(hour)
                        entry0[t, 32].delete('0', END)
                        entry0[t, 32].insert(0, f'{sum_hour[t] * 200}')
                zapisej = t
                print(t)
                #print(t1)
                tabl_full = True
                if t == 0:
                    messagebox.showinfo('внимание', 'данного товара нет в наличии')
                    tabl_full = False
                #print(menubuts)
                print(sum_hour)
        else:
            messagebox.showinfo('внимание','обновите таблицу')
    except FileNotFoundError:
        messagebox.showinfo('внимание', f'создайте файл: {file}')


l_search = Label(canvas8, text='Выберите месяц:', bg ='lightblue', fg='blue', font=('Arial', 10, 'bold'))
l_search.place(x=1, y=10)#y=150


def uptabl():
    global zapisej, tabl_full, lst, lst2
    tabl_full = False
    rewtablb['text'] = 'расход'
    vvod_search2.delete('0', END)
    listbox2.place_forget()
    vvod_search2.bind('<KeyRelease>', check_input2)
    for i in range(1, 11):
        entry0[i, 32].config(fg='white', font=('Arial', 16, 'bold'))
    with open('tabel.txt', 'r') as f:
        l = f.read()
        lst = []
        lst2 = []
        count = l.splitlines()
        for i in range(len(count)):
            sf = count[i].split()
            lst.append(sf[0])
            #lst2.append(sf[0] + ' ' + sf[2])
    try:
        #vvod_search.bind('<KeyRelease>', check_input)
        for i in range(1, zapisej+2):
            entry90[i, 1].delete('0', END)
            for j in range(32):
                entry0[i, j].delete('0', END)
    except NameError:
        messagebox.showinfo('внимание', 'действие выполнить нельзя!')



def rashod():
    global count
    try:
        su = 0
        for i in range(1, len(count)+1):
            s1 = entry0[i, 32].get()
            print(s1)
            sp = s1.split('.')
            print(sp)
            su = su + int(sp[0])
            print(su)
            rewtablb.config(text=su)
    except NameError:
        messagebox.showwarning('предупреждение', 'действие выполнить нельзя!')


save_tablb = Button(canvas8, width=16, text='сохранить табель ', bg='lightblue',fg='blue', bd=0 ,font=('Arial', 10, 'bold'))
save_tablb.place(x=430, y=80)
uptablb = Button(canvas8, width=16, text='очистить табель', bg='lightblue', command=lambda: uptabl(), fg='blue', bd=0 ,font=('Arial', 10, 'bold'))
uptablb.place(x=1, y=80)
rewtablb = Button(canvas8, width=10, text='расход',bg='lightblue', command=lambda: rashod(), fg='blue', bd=0 ,font=('Arial', 10, 'bold'))
rewtablb.place(x=860, y=50)
b_zp = Button(canvas8, width=6, bg='lightblue', fg='blue', justif="left", bd=0,
              command=change_color, font=('Arial', 10, 'bold'), text='з/п')#+ '/' + '%s' % j)
b_zp.place(x=630, y=10)
lst3 = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
                'Ноябрь', 'Декабрь']
slo = {'Январь': 'tabel_jan.txt',
       'Февраль': 'tabel_feb.txt',
       'Март': 'tabel_mar.txt',
       'Апрель': 'tabel_apr.txt',
       'Май': 'tabel_may.txt',
       'Июнь': 'tabel_jun.txt',
       'Июль': 'tabel_jul.txt',
       'Август': 'tabel_aug.txt',
       'Сентябрь': 'tabel_sep.txt',
       'Октябрь': 'tabel_oct.txt',
       'Ноябрь': 'tabel_nov.txt',
       'Декабрь': 'tabel_des.txt'

}

def check_input2(_event=None):
    value = vvod_search2.get().lower()
    #listbox.place_forget()
    vvod_search2.focus()
    if value == '':
        listbox2_values.set('')
        listbox2.place_forget()

    else:
        data = []
        for item in lst3:
            if value.lower() in item.lower():
                data.append(item)
                listbox2.place(x=320, y=60)
                vvod_search2.focus()
                listbox2_values.set(data)
entry_text2 = StringVar()
vvod_search2 = Entry(canvas8,  width=10, fg='black', font=('Arial', 10, 'bold'), textvariable=entry_text2)
vvod_search2.place(x=330, y=1)
vvod_search2.bind('<KeyRelease>', check_input2)
#vvod_search.bind('<Return>', poisk)
def on_change_selection2(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        entry_text2.set(data)
        for key in slo:
            if key == data:
                print(slo[key])
                poisk('', slo[key])
        check_input2()
        listbox2.delete(0, 2)
        listbox2.place_forget()
        vvod_search2.unbind('<KeyRelease>')

listbox2_values = Variable()
listbox2 = Listbox(canvas8, listvariable=listbox2_values, width=20, fg='black', font=('Arial', 10, 'bold'))
listbox2.bind('<<ListboxSelect>>', on_change_selection2)
listbox2_values.set(lst3)
root.mainloop()
