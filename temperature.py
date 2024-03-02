from tkinter import *
from tkinter import ttk, messagebox, filedialog
import math
import re
import datetime
from tkcalendar import Calendar, DateEntry
#from digital_keyboard import klava
import os
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
    wind.title('температура на улице и в теплицах')
    wind.geometry('770x380+30+20')
    wind['bg'] = 'Goldenrod'#'Goldenrod'
    #wind.attributes("-topmost", True)
    import datetime
    today = datetime.date.today()
    currentDay = today.day
    currentMonth = today.month
    currentYear = today.year
    mindate = datetime.date(year=2018, month=1, day=21)
    maxdate = today + datetime.timedelta(weeks=500)
    print(mindate, maxdate)
    cal = Calendar(wind, font="Arial 8", selectmode='day', locale='ru_RU',
                   mindate=mindate, maxdate=maxdate, disabledforeground='blue', background="blue",
                   foreground="white",
                   selectbackground="blue",
                   normalbackground="Khaki",
                   weekendbackground="SaddleBrown",
                   weekendforeground="white",
                   cursor="hand1", year=currentYear, month=currentMonth, day=currentDay)
    # cal.pack(fill="both", expand=True)
    # cal.grid((row=0, column=0)
    cal.place(x=480, y=40)
    #текущая дата всегда выделена
    today_date = datetime.date(year=currentYear, month=currentMonth, day=currentDay)
    cal.calevent_create(today_date, 'Hello World', 'today_date')
    cal.tag_config('today_date', background='blue', foreground='white')
    text = tk.Text(wind, width=21, height=11, bg="Khaki", font=('Arial', 10, 'bold'),
                   fg='Maroon', wrap=tk.WORD)
    #text.place(x=10, y=10)
    Label(wind, text='в ночь с какого | time | ул | т1|тр |',  bg='Goldenrod', bd=0, fg='white',
                     font=('Arial', 8, 'bold')).place(x=32, y=17)

    text2 = tk.Text(wind, width=33, height=8, bg="PaleGoldenrod", font=('Arial', 7, 'bold'),
                   fg='Maroon', wrap=tk.WORD)
    text2.place(x=1, y=50)
    text2.focus()
    i_cheki = Button(wind, text='внести', width=8,  bd=1, bg='SaddleBrown', fg='white',
                     font=('Arial', 6, 'bold'))
    i_cheki.place(x=10, y=300)
    look = Button(wind, text='проссмотреть', width=8, bd=1, bg='SaddleBrown', fg='white',
                     font=('Arial', 6, 'bold'))
    look.place(x=10, y=360)
    diagr = Button(wind, text='диаграмма', width=8, bd=1, bg='SaddleBrown', fg='white',
                  font=('Arial', 6, 'bold'))
    diagr.place(x=180, y=300)

    sbros = Button(wind, text='сброс', width=4, height=3, bd=1, bg='SaddleBrown', fg='white',
                   font=('Arial', 6, 'bold'))
    sbros.place(x=350, y=300)
    kn = Button(wind, text='по дате', width=8, bd=1, bg='SaddleBrown', fg='white',
                   font=('Arial', 6, 'bold'))
    kn.place(x=180, y=360)
    en_ul = Entry(wind, text='поиск', width=4, bd=1, bg='white', justif='right',
                   font=('Arial', 8, 'bold'))
    en_ul.place(x=10, y=423)
    kn_ul = Button(wind, text='по улице', width=6, bd=1, bg='SaddleBrown', fg='white',
                   font=('Arial', 6, 'bold'))
    kn_ul.place(x=80, y=413)
    max_ul = Button(wind, text='низкая', width=4, bd=1, bg='SaddleBrown', fg='white',
                   font=('Arial', 6, 'bold'))
    max_ul.place(x=220, y=413)
    vis_ul = Button(wind, text='высокая', width=4, bd=1, bg='SaddleBrown', fg='white',
                   font=('Arial', 6, 'bold'))
    vis_ul.place(x=340, y=413) 
    kn_hour_21 = Button(wind, text='21-22', width=2, bd=1, bg='blue', fg='white',
                font=('Arial', 6, 'bold'))
    kn_hour_21.place(x=480, y=413)
    kn_hour_22 = Button(wind, text='22-23', width=2, bd=1, bg='blue', fg='white',
                font=('Arial', 6, 'bold'))
    kn_hour_22.place(x=480, y=360)
    kn_hour_23 = Button(wind, text='23-24', width=2, bd=1, bg='blue', fg='white',
                font=('Arial', 6, 'bold'))
    kn_hour_23.place(x=570, y=413)

    kn_hour_24 = Button(wind, text='24-01', width=2, bd=1, bg='blue', fg='white',
                        font=('Arial', 6, 'bold'))
    kn_hour_24.place(x=570, y=360)
    kn_hour_01 = Button(wind, text='01-02', width=2, bd=1, bg='blue', fg='white',
                        font=('Arial', 6, 'bold'))
    kn_hour_01.place(x=660, y=413)
    kn_hour_02 = Button(wind, text='02-03', width=2, bd=1, bg='blue', fg='white',
                        font=('Arial', 6, 'bold'))
    kn_hour_02.place(x=660, y=360)
    kn_hour_04 = Button(wind, text='04-05', width=2, bd=1, bg='blue', fg='white',
                        font=('Arial', 6, 'bold'))
    kn_hour_04.place(x=750, y=360)
    kn_hour_03 = Button(wind, text='03-04', width=2, bd=1, bg='blue', fg='white',
                        font=('Arial', 6, 'bold'))
    kn_hour_03.place(x=750, y=413)
    kn_hour_05 = Button(wind, text='05-06', width=2, bd=1, bg='blue', fg='white',
                        font=('Arial', 6, 'bold'))
    kn_hour_05.place(x=840, y=413)
    kn_hour_06 = Button(wind, text='06-07', width=2, bd=1, bg='blue', fg='white',
                        font=('Arial', 6, 'bold'))
    kn_hour_06.place(x=840, y=360)
    
    l_per = Label(wind, font=("Arial", 16, 'bold'), text='Всего переводов за ', bg='Goldenrod', bd=0, fg='white')
    #l_per.place(x=370, y=320)
    l = Label(wind, font=("Arial", 16, 'bold'), text='Всего наличными за ', bg='Goldenrod', bd=0, fg='white')
    #l.place(x=370, y=350)
    l2 = Label(wind, font=("Arial", 25, 'bold'), text='Итого за ', bg='Goldenrod', bd=0, fg='white',)
    #l2.place(x=400, y=400)
    def look_date(data):
        ne_sobirali = True
        text2.delete('1.0', END)
        with open('temperature.txt', 'r') as f:
            all = f.read()
            sp_all = all.splitlines()
            for i in range(len(sp_all)):
                s = re.search(data, sp_all[i])
                if s:
                    ne_sobirali = False
                    
                    text2.insert(END, '\n' + sp_all[i])
                    
        if ne_sobirali:
            text2.delete('1.0', END)
            text2.insert('1.0', 'нет записей в этот день')
    def otdali():
        ne_sobirali = True
        text2.delete('1.0', END)
        t = en_ul.get()
        with open('temperature.txt', 'r') as f:
            all = f.read()
            sp_all = all.splitlines()
            for i in range(len(sp_all)):
                #s = re.search(t, sp_all[i])
                #if s:
                if t ==sp_all[i].split()[5]:
                    ne_sobirali = False
                    
                    text2.insert(END, '\n' + sp_all[i])
                    
        if ne_sobirali:
            text2.delete('1.0', END)
            text2.insert('1.0', 'не было такой  температуры')
    kn_ul.config(command=otdali)
    def itog_day2(data):
        l_per.place_forget()
        l.place_forget()
        l2.place_forget()
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
        l_per.config(font=("Arial", 16, 'bold'), text='Всего переводов за ' + data + ': ' + str(math.fsum(per)))
        l_per.place(x=370, y=320)
        l.config(font=("Arial", 16, 'bold'), text='Всего наличными за ' + data + ': ' + str(math.fsum(nal)))
        l.place(x=370, y=350)
        l2.config(font=("Arial", 20, 'bold'), text='Итого за ' + data + ': ' + str(math.fsum(nal) + math.fsum(per)))
        l2.place(x=400, y=400)

    def diagra(file_look, z, nai):
        global nadpisi, total, total_del
        root = Tk()
        root.geometry('900x400+5+5')
        n = 50
        m = 50
        nadpisi = False

        canv = Canvas(root, width=820, height=380, bg="gold", cursor='pencil')
        can = Canvas(canv,  width=830, height=350,  bg="gold" )
        # создаём полосу прrокруткtи для холста для frame8 and canvas9 для табеля
        vsb20 = Scrollbar(canv, orient="horizontal")
        vsb20.pack(side="bottom", fill="x", expand=False)
        can.configure(xscrollcommand=vsb20.set)
        vsb20.configure(command=can.xview)
        vsb8 = Scrollbar(canv, orient="vertical")
        vsb8.pack(side="right", fill="y", expand=False)
        can.configure(yscrollcommand=vsb8.set)
        vsb8.configure(command=can.yview)
        can.pack(side="left", fill="both", expand=True)
        # создаём фрэйм для виджетов на холсте, чтобы их прокручивать
        scrolled_frame8 = Frame(can, background=can.cget('bg'))
        can.create_window((4, 4), window=scrolled_frame8, anchor="nw")

        def on_configure8(event):
            """Set the scroll region to encompass the scrolled frame"""
            can.configure(scrollregion=can.bbox("all"))
        scrolled_frame8.bind("<Configure>", on_configure8)
        can.create_line(55 + n, 917, 55 + n, 100, width=2, arrow=LAST)
        can.create_line(100, 665 - m, 1000 + n, 665 - m, width=2, arrow=LAST)
        canv.place(x=20, y=0)
        can.create_text(400, 640, text='числа  и часы в месяце', fill='blue', font=('Arial', 10, 'bold'))
        if nai == 'C':
            can.create_text(35, 320, text='т\nе\nм\nп\nе\nр\nа\nт\nу\nр\n а', fill='green', font=('Arial', 10, 'bold'))
        else:
            can.create_text(35, 300, text='к\nо\nл\nи\nч\nе\nс\nт\nв\nо\n \nр\nу\nб\nл\nе\nй', fill='green', font=('Arial', 20, 'bold'))
            
        kg = []
        num = []
        st = 1
        for i in range(-30, 40):  # ось у с килограммами
            if i % 5 == 0:
               can.create_text(40 + n, 665 - st * i * 10 - m, text=str(i), fill='green', font=('Arial', 10, 'bold'), tags='del')
               can.create_line(50 + n, 665 - st * i * 10 - m, 1000 + n, 665 - st * i * 10 - m, fill='gray', width=1, tags='del')
        color = ['Indigo', 'LimeGreen', 'SaddleBrown', 'red', 'green', 'orange', 'blue', 'purple', 'DarkOrange', 'black', 'MediumVioletRed','DarkRed']
        def preobrag(slo_date, li):#перевод 'kalkulator.txt' в формот 'people.txt'
            global g
            sp_al = li
            if file_look == 'kalkulator.txt':
                for i in range(len(sp_al)):
                    s = sp_al[i].split()
                    date = s[0]
                    if date in slo_date:
                        slo_date[date].append(int(s[2]))
                    else:
                        slo_date[date] = []
                        slo_date[date].append(int(s[2]))
                #print(slo_date)
                for date in slo_date:
                    slo_date[date] = int(math.fsum(slo_date[date]))
                #print(slo_date)
                g = []
                for date in slo_date:
                    g.append(date + ' ' + str(slo_date[date]))

        def setka(total, mesj):
            global li, st, mon, kg
            mon = []
            kg = []
            slo_date = {}
            print('mon=', mon)
            if total:
                with open(file_look, 'r', encoding='utf-8') as file:
                    line = file.read()
                    li = line.splitlines()
                    if file_look == 'kalkulator.txt':
                        preobrag(slo_date, li)
                        li = g
                    #print(li)
                    stri = li[1].split()
                    mon.append(stri[3][3:5])
                    for i in range(len(li)):
                        sp = li[i].split()
                        kg.append(int(sp[z]))
                        num.append(int(sp[3][0:2]))
                        if mon[-1] != sp[3][3:5]:
                            mon.append(sp[3][3:5])
                    print(kg)
                    print(num)

            else:
                with open(file_look, 'r', encoding='utf-8') as file:
                    line = file.read()
                    li = line.splitlines()
                    if file_look == 'kalkulator.txt':
                        preobrag(slo_date, li)
                        li = g
                    for i in range(0, len(li)):
                        sp1 = li[i].split()
                        if mesj == sp1[3][3:5]:
                            kg.append(int(sp1[z]))
            print('месяцы', mon)
            try:
                print(min(kg))
                max_kg = min(kg)
                print(max_kg)
                if max_kg < 100:
                    k = max_kg + 100
                elif max_kg >= 100 and max_kg <= 1000:
                    k = max_kg + 200
                elif max_kg >= 1000 and max_kg <= 10000:
                    k = max_kg + 500
                elif max_kg >= 10000 and max_kg <= 100000:
                    k = max_kg + 2000
                elif max_kg >= 100000:
                    k = max_kg + 20000
                ste = 600 / (k // 10 * 10)
                print('ste=', ste)
                st = ste
                print('st=', st)
                print(k)
                print(k // 10)
                for i in range(32):  # ось х с числами месяца
                    canv.create_text(55 + i * 30 + n, 675 - m, text=str(i), fill='blue', font=('Arial', 10, 'bold'))
                    canv.create_line(55 + i * 30 + n, 663-m, 55 + i * 30 + n, 50 - m, width=1, fill='gray', tags='del')
                for i in range(k // 10 + 1):  # ось у с килограммами
                    if ste >= 0.1 and ste <= 2:
                        if i % 10 == 0:
                            canv.create_text(40 + n, 665 - st * i * 10 - m, text=str(i * 10), fill='green', font=('Arial', 10, 'bold'), tags='del')
                            canv.create_line(50 + n, 665 - st * i * 10 - m, 1000 + n, 665 - st * i * 10 - m, fill='gray', width=1, tags='del')
                    elif ste <= 0.1:
                        if i % 100 == 0:
                            canv.create_text(40 + n, 665 - st * i * 10 - m, text=str(i * 10), fill='green', font=('Arial', 10, 'bold'), tags='del')
                            canv.create_line(50 + n, 665 - st * i * 10 - m, 1000 + n, 665 - st * i * 10 - m, width=1, tags='del', fill='gray')

                    else:
                        canv.create_text(40 + n, 665 - st * i * 10 - m, text=str(i * 10), fill='green',
                                         font=('Arial', 10, 'bold'), tags='del')
                        canv.create_line(50 + n, 665 - st * i * 10 - m, 1000 + n, 665 - st * i * 10 - m, width=1,
                                         tags='del', fill='gray')
            except ValueError:
                print('в этом месяце нет данных')
        def diagr(mesj, cvet, k, nai, tot_sum):
            global nadpisi, total, t, st, li, g, total_del
            kg1 = []
            num1 = []
            l = {}
            l_num = {}
            l_kg = {}
            tex = {}
            tex1 = {}
            slo_date = {}
            print('month = ', mesj)
            inde = mes3.index(mesj)
            mesja = mes[inde]
            print(mesja)
            if total == True:
                ind = mes.index(mesja)
                mesja1 = mes2[ind]
                print(mesja1)
                tot = []
                with open(file_look, 'r') as f:
                    all = f.read()
                    sp_all = all.splitlines()
                    if file_look == 'kalkulator.txt':
                        preobrag(slo_date, sp_all)
                        sp_all = g
                    for i in range(len(sp_all)):
                        s = sp_all[i].split()
                        if s[3][3:5] == mesj:
                            tot.append(int(s[z]))
                            #print(tot)
                summer = math.fsum(tot)
                tot_sum.append(summer)
                print('summer=', summer)
                canv.create_line(120, t, 160, t, width=5, fill=cvet, smooth=True, tags='del')
                canv.create_text(255, t, text=mesja1+' - '+str(summer), font=('Arial', 14, 'bold'), fill=cvet, tags='del')
            for i in range(0, len(li)):
                sp1 = li[i].split()
                if mesj == sp1[3][3:5]:
                    kg1.append(int(sp1[z]))
                    num1.append(int(sp1[3][0:2]))
                    for j in range(len(kg1)):  # точки графика число и кг.
                        canv.create_oval(50 + num1[j] * 30 + n, 660 - st * kg1[j] - m, 50 + num1[j] * 30 + n + 8,
                                         660 - st * kg1[j] + 8 - m, fill=cvet, outline=cvet, tags='del')
                        if j > 0:
                            canv.create_line(50 + num1[j - 1] * 30 + 5 + n, 660 - st * kg1[j - 1] + 5 - m,
                                             50 + num1[j] * 30 + 5 + n, 660 - st * kg1[j] + 5 - m, width=3, fill=cvet, tags='del')
                        tex1[k, j] = str(num1[j]) + mesja + ': ' + str(kg1[j]) + nai
                        tex[k, j] = str(kg1[j]) + nai
                        l_num[k, j] = 50 + num1[j] * 30 + 14 + n  # по оси х числа месяца, координата х
                        l_kg[k, j] = 655 - st * kg1[j] - m  # по оси у количество кг, координата у
            butt = {}
            def but(k, g):
                butt[k, g] = Button(canv, text=tex[k, g], fg='black', font=('Arial', 8, 'bold'))  # надписи над точками
                butt[k, g].place(x=l_num[k, g], y=l_kg[k, g])
                def text1(k, g):
                    canv.delete('del2')
                    canv.create_text(640, 650, text=tex1[k, g],
                                     font=('Arial', 20, 'bold'),
                                     fill='MidnightBlue', tags='del2')
                butt[k, g].config(command=lambda: text1(k, g))
            if nadpisi == True:
                        #t = 140
                canv.delete('del3')
                canv.create_text(930, 650, text='За месяц: ' + str(sum(kg1)),
                                         font=('Arial', 20, 'bold'),
                                         fill='red', tags='del3')
                for g in range(len(kg1)):
                    but(k, g)

            nadpisi = False
        total = False
        total_del = False
        def total_di():
            global total, t, mon, total_del
            if  total_del == False:
                total_del = True
                total = True
                #clear()
                t = 0
                total_summer = []
                setka(total, '')
                for mo in range(len(mon)):
                    t = t+20
                    diagr(mon[mo], color[mo], mo+1, nai, total_summer)
                canv.create_text(690, 650, text='Всего: ' + str(math.fsum(total_summer)) + nai,
                                 font=('Arial', 20, 'bold'),
                                 fill='MidnightBlue', tags='del2')
            else:
                messagebox.showinfo('внимание', 'очистите, нажав "del" ')

        def selected(event):
            global nadpisi, total, total_del
            if total_del == False:
                nadpisi = True
                total = False
                total_del = True
                #clear()
                m1 = combobox.get()
                ind = mes2.index(m1)
                setka(total, mes3[ind])
                diagr(mes3[ind], random.choice(color), ind, nai, [])
            else:
                messagebox.showinfo('внимание', 'очистите, нажав "del" ')
        total_diagr = Button(root, text='общая', command=total_di, width=8)
        total_diagr.place(x=720, y=50)

        def clear():
            global total, t, total_del
            canv.delete('del')
            canv.delete('del2')
            canv.delete('del3')
            total = False
            total_del = False
            for w in canv.winfo_children():
                if w.winfo_class() == "Button":
                    w.destroy()

        clean = Button(root, text='del', command=clear, width=8)
        clean.place(x=720, y=110)
        mes = ['месяц', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
               'ноября', 'декабря']
        mes2 = ['месяц', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
                'Ноябрь', 'Декабрь']
        mes3 = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        combobox = ttk.Combobox(root, values=mes2, state="readonly", width=7, font=('Comic', 10, 'bold'))
        combobox.place(x=720, y=80)
        inf = Label(root, bg='lightblue', fg='blue', font=('Arial', 20, 'bold'))
        # inf.place(x=710, y=50)#y=150
        combobox.bind("<<ComboboxSelected>>", selected)
        combobox.set('месяц')
        root.mainloop()

    diagr.config(command=lambda: diagra('temperature.txt', 5, 'C.'))
    def look_col():
        text2.delete('1.0', END)
        with open('temperature.txt', 'r', encoding='utf-8') as f:
            fi = f.read()
            text2.insert('1.0', fi)
    look.config(command=look_col)
    def sbrosit():
        text2.delete('1.0', END)
    sbros.config(command=sbrosit)
    hour = ['22', '23', '24', '01', '02', '03', '04', '05', '06', '07']
    def vivod(data):
        #global not_sale
        text2.focus()
        text2.insert('1.0', 'в ночь с ' + data + ': ')
        def save_col(d):
            #text2.delete('1.0', END)
            s = text2.get('1.0', END)
            print('длина строки: ', len(s))
            print(text2.get('1.0', END))
            if len(s) <= 20 or len(s) > 40:
                messagebox.showwarning('предупреждение!!!', 'действие выполнить невозможно!!!\nвведите количество покупателей!!!')
            else:
                with open('temperature.txt', 'a+') as f:
                    f.write(s)
                    messagebox.showinfo('внимание!!!',
                                           'запись внесена!!!')
        def chas(h):
            text2.insert(END, h['text'] + ': ')

        i_cheki.config(command=lambda: save_col(data))
        kn_hour_22.config(command=lambda: chas(kn_hour_22))
        kn_hour_24.config(command=lambda: chas(kn_hour_24))
        kn_hour_02.config(command=lambda: chas(kn_hour_02))
        kn_hour_04.config(command=lambda: chas(kn_hour_04))
        kn_hour_06.config(command=lambda: chas(kn_hour_06))
        kn_hour_21.config(command=lambda: chas(kn_hour_21))
        kn_hour_23.config(command=lambda: chas(kn_hour_23))
        kn_hour_01.config(comman=lambda: chas(kn_hour_01))
        kn_hour_03.config(command=lambda: chas(kn_hour_03))
        kn_hour_05.config(command=lambda: chas(kn_hour_05))
        p = 0
        total_buy = 0
        not_sale = False
         

    def update_text(event):
        text.delete('1.0', END)
        text2.delete('1.0', END)
        cal.config(selectbackground="red")
        data = str(cal.selection_get())
        print('выбранная дата : ', data)
        new_data_format = data[8:10] + '-' + data[5:7] + '-' + data[0:4]
        print(new_data_format)
        vivod(new_data_format)
        #itog_day2(new_data_format[0:5])
        kn.config(command=lambda: look_date(new_data_format))

    cal.bind("<<CalendarSelected>>", update_text)
    wind.mainloop()
total_buyers()