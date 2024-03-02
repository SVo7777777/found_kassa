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
    wind.title('КАЛЕНДАРЬ СБОРА ТОМАТОВ В 2023 ГОДУ')
    wind.geometry('770x260+10+300')
    wind['bg'] = 'Tomato'  # 'Goldenrod'
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
                   normalbackground="LightSalmon",
                   weekendbackground="DarkRed",
                   weekendforeground="white",
                   cursor="hand1", year=currentYear, month=currentMonth, day=currentDay)
    # cal.pack(fill="both", expand=True)
    # cal.grid((row=0, column=0)
    cal.place(x=385, y=10)
    # текущая дата всегда выделена
    today_date = datetime.date(year=currentYear, month=currentMonth, day=currentDay)
    cal.calevent_create(today_date, 'Hello World', 'today_date')
    cal.tag_config('today_date', background='blue', foreground='white')
    text = tk.Text(wind, width=30, height=11, bg="Pink", font=('Arial', 16, 'bold'),
                   fg='Maroon', wrap=tk.WORD)
    #text.place(x=10, y=10)
    ##Label(wind, text='Количество покупателей:',  bg='Goldenrod', bd=0, fg='white',
          #font=('Arial', 18, 'bold')).place(x=10, y=280)

    text2 = tk.Text(wind, width=17, height=8, bg="Pink", font=('Arial', 16, 'bold'),
                    fg='Maroon', wrap=tk.WORD)
    text2.place(x=10, y=10)
    text2.focus()
    i_cheki = Button(wind, text='внести', width=13,  bd=1, bg='DarkRed', fg='white',
                     font=('Arial', 12, 'bold'))
    i_cheki.place(x=230, y=10)
    look = Button(wind, text='проссмотреть', width=13, bd=1, bg='DarkRed', fg='white',
                  font=('Arial', 12, 'bold'))
    look.place(x=230, y=50)
    diagr = Button(wind, text='диаграмма', width=13, bd=1, bg='DarkRed', fg='white',
                   font=('Arial', 12, 'bold'))
    diagr.place(x=230, y=170)

    sbros = Button(wind, text='сброс', width=13, bd=1, bg='DarkRed', fg='white',
                   font=('Arial', 12, 'bold'))
    sbros.place(x=230, y=130)
    kn = Button(wind, text='по дате', width=13, bd=1, bg='DarkRed', fg='white',
                font=('Arial', 12, 'bold'))
    kn.place(x=230, y=90)
    kn_diagr_money = Button(wind, text='диаграмма продаж', width=24, bd=1, bg='blue', fg='white',
                            font=('Arial', 18, 'bold'))
    #kn_diagr_money.place(x=385, y=260)
    l_per = Label(wind, font=("Arial", 16, 'bold'), text='Всего переводов за ', bg='Goldenrod', bd=0, fg='white')
    #l_per.place(x=370, y=320)
    l = Label(wind, font=("Arial", 16, 'bold'), text='Всего наличными за ', bg='Goldenrod', bd=0, fg='white')
    #l.place(x=370, y=350)
    l2 = Label(wind, font=("Arial", 25, 'bold'), text='Итого за ', bg='Goldenrod', bd=0, fg='white')
    #l2.place(x=400, y=400)
    mes = ['месяц', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
           'ноября', 'декабря']
    mes3 = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    def otdali():
        #text2.delete('1.0', END)

        with open('tomatos.txt', 'r') as f, open('tomatos1.txt', 'a+') as f1:
            fi = f.read()
            sp = fi.splitlines()
            print(sp)
            for i in range(1, len(sp)):
                s = sp[i].split()
                ind = mes.index(s[1])
                if len(s[0]) == 1:
                    line = '0' + s[0] + '-' + mes3[ind] + '-' + s[2] + ': ' + s[5]
                else:
                    line = s[0] + '-' + mes3[ind] + '-' + s[2] + ': ' + s[5]

                print(line)
                f1.write(line + '\n')
            #text2.insert('1.0', fi)

    def look_date(data):
        ne_sobirali = True
        with open('tomatos1.txt', 'r') as f:
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
            text2.insert('1.0', 'не собирали в этот день')

    def diagra(file_look, z, nai):
        global nadpisi, total, total_del
        root = Tk()
        root.geometry('1200x700+5+5')
        n = 50
        m = 50
        nadpisi = False

        canv = Canvas(root, width=1120, height=680, bg="white", cursor='pencil')
        canv.create_line(55 + n, 617, 55 + n, 0, width=2, arrow=LAST)
        canv.create_line(100, 665 - m, 1000 + n, 665 - m, width=2, arrow=LAST)
        canv.place(x=20, y=0)
        canv.create_text(400, 640, text='числа в месяце', fill='blue', font=('Arial', 20, 'bold'))
        canv.create_text(35, 300, text='\nк\nи\nл\nо\nг\nр\nа\nм\nм\nы', fill='green', font=('Arial', 20, 'bold'))
        kg = []
        num = []
        mon0 = []
        st = 1
        color = ['Indigo', 'LimeGreen', 'SaddleBrown', 'red', 'green', 'orange', 'blue', 'BlueViolet', 'DarkGoldenRod', 'Fuchsia', 'black', 'MediumVioletRed']
        def preobrag(slo_date, li)  :  # перевод 'kalkulator.txt' в формот 'people.txt'
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
                print(slo_date)
                for date in slo_date:
                    slo_date[date] = int(math.fsum(slo_date[date]))
                print(slo_date)
                g = []
                for date in slo_date:
                    g.append(date + ' ' + str(slo_date[date]))
                print('будущее li: ', g)
                li = g
        def setka(total, mesj):
            global li, st, mon, kg
            mon = []
            kg = []
            slo_date = {}
            print('mon=', mon)
            if total:
                with open(file_look, 'r') as file:
                    line = file.read()
                    li = line.splitlines()
                    if file_look == 'kalkulator.txt':
                        preobrag(slo_date, li)
                        li = g
                    print(li)
                    stri = li[1].split()
                    mon.append(stri[0][3:5])
                    for i in range(len(li)):
                        sp = li[i].split()
                        kg.append(int(sp[z]))
                        num.append(int(sp[0][0:2]))
                        if mon[-1] != sp[0][3:5]:
                            mon.append(sp[0][3:5])
                    # print(sp[5])
            # print(kg)
            else:
                with open(file_look, 'r') as file:
                    line = file.read()
                    li = line.splitlines()
                    if file_look == 'kalkulator.txt':
                        preobrag(slo_date, li)
                        li = g
                    for i in range(0, len(li)):
                        sp1 = li[i].split()
                        if mesj == sp1[0][3:5]:
                            kg.append(int(sp1[z]))
            print('месяцы', mon)
            print(max(kg))
            max_kg = max(kg)
            print(max_kg)
            if max_kg < 100:
                k = max_kg + 10
            elif max_kg >= 100 and max_kg <= 1000:
                k = max_kg + 100
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
                canv.create_line(55 + i * 30 + n, 663 -m, 55 + i * 30 + n, 50 - m, width=1, fill='gray', tags='del')
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
            #print('month = ', mesj)
            inde = mes3.index(mesj)
            mesja = mes[inde]
            #print(mesja)

            if total == True:
                ind = mes.index(mesja)
                mesja1 = mes2[ind]
                #print(mesja1)
                tot = []
                with open(file_look, 'r') as f:
                    all = f.read()
                    sp_all = all.splitlines()
                    if file_look == 'ogurci.txt':
                        preobrag(slo_date, sp_all)
                        sp_all = g
                    for i in range(len(sp_all)):
                        s = sp_all[i].split()
                        if s[0][3:5] == mesj:
                            tot.append(int(s[z]))
                            # print(tot)
                summer = math.fsum(tot)
                tot_sum.append(summer)
                #print('summer=', summer)
                canv.create_line(120, t, 160, t, width=5, fill=cvet, smooth=True, tags='del')
                canv.create_text(255, t, text=mesja1 + ' -  ' + str(summer) + 'кг.', font=('Arial', 14, 'bold'), fill=cvet, tags='del')
                # t = t + 20
            for i in range(0, len(li)):
                sp1 = li[i].split()
                if mesj == sp1[0][3:5]:
                    kg1.append(int(sp1[z]))
                    num1.append(int(sp1[0][0:2]))
                    # print('людей', kg1)
                    # print('число', num1)
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

                # for g in range(len(kg1)):
                # but(k, g)

            '''print(l_num)
            print(l_kg)
            print(l)
            print(tex)'''
            if nadpisi == True:
                # t = 140
                canv.delete('del3')
                canv.create_text(930, 650, text='За месяц: ' + str(sum(kg1)) + 'кг.',
                                 font=('Arial', 20, 'bold'),
                                 fill='red', tags='del3')
                for g in range(len(kg1)):
                    but(k, g)

            nadpisi = False

            # root.root_attributes("-transparentcolor", cvet)
            # canv.create_oval(50+2*30, 660-5*num[j],50+2*30+5, 660-5*num[j]+5, fill='blue')

        total = False
        total_del = False

        def total_di():
            global total, t, mon, total_del
            if total_del == False:
                total = True
                total_del = True
                # clear()
                t = 0
                total_summer = []
                setka(total, '')
                for mo in range(len(mon)):
                    t = t + 20
                    diagr(mon[mo], color[mo], mo + 1, nai, total_summer)
                canv.create_text(690, 650, text='Всего собрано: ' + str(math.fsum(total_summer)) + 'кг.',
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
                # clear()
                m1 = combobox.get()
                ind = mes2.index(m1)
                setka(total, mes3[ind])
                diagr(mes3[ind], random.choice(color), ind, nai, [])
            else:
                messagebox.showinfo('внимание', 'очистите, нажав "del" ')


        total_diagr = Button(root, text='общая', command=total_di, width=8)
        total_diagr.place(x=1120, y=50)

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
        clean.place(x=1120, y=110)
        mes = ['месяц', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
               'ноября', 'декабря']
        mes2 = ['месяц', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
                'Ноябрь', 'Декабрь']
        mes3 = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        combobox = ttk.Combobox(root, values=mes2, state="readonly", width=7, font=('Comic', 10, 'bold'))
        combobox.place(x=1120, y=80)
        inf = Label(root, bg='lightblue', fg='blue', font=('Arial', 20, 'bold'))
        # inf.place(x=710, y=50)#y=150
        combobox.bind("<<ComboboxSelected>>", selected)
        combobox.set('месяц')
        root.mainloop()

    diagr.config(command=lambda: diagra('tomatos1.txt', 1, 'кг.'))
    #kn_diagr_money.config(command=lambda: diagra('kalkulator.txt', 1, 'p.'))

    def look_col():
        text2.delete('1.0', END)
        with open('tomatos1.txt', 'r') as f:
            fi = f.read()
            text2.insert('1.0', fi)

    look.config(command=look_col)

    def sbrosit():
        text2.delete('1.0', END)

    sbros.config(command=sbrosit)
    hour = ['08', '09', '10', '11', '12', '13', '14', '15', '16', '17']

    def vivod(data):
        # global not_sale
        text2.focus()
        text2.insert('1.0', data + ': ')

        def save_col(d):
            # text2.delete('1.0', END)
            s = text2.get('1.0', END)
            print('длина строки: ', len(s))
            print(text2.get('1.0', END))
            if len(s) <= 13 or len(s) > 20:
                messagebox.showwarning('предупреждение!!!',
                                       'действие выполнить невозможно!!!\nвведите количество огурцов!!!')
            else:
                with open('tomatos1.txt', 'a+') as f:
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
        #itog_day2(new_data_format[0:5])
        kn.config(command=lambda: look_date(new_data_format))
    cal.bind("<<CalendarSelected>>", update_text)
    #sbros.config(command=otdali)
    wind.mainloop()
# создаём меню

total_buyers()