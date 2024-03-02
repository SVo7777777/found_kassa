from tkinter import *
from tkinter import ttk, messagebox, filedialog
import math
import datetime
from tkcalendar import Calendar, DateEntry
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
root.title("фазенда")
root.geometry("1200x535+2+2")#1300x460+200+2; 1500x600+5+5
root['bg'] = 'orange'
root.overrideredirect(0)
#root.attributes("-topmost", True)
root.resizable()
root.option_add("*tearOff", FALSE)
dirname, filename = os.path.split(os.path.realpath(__file__))
def rew_tabl(buyers):
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
            if buyers:
                total_buyers()
                win.destroy()
            else:
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
    #wind1.destroy()
    wind = Tk()
    wind.title('итог за день')
    wind.geometry('400x200+500+500')
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
            if len(s) == 4:
                if s[0][0:5] == da[0] and s[3] == 'перевод':
                    per.append(int(s[2]))
            else:
                if s[0][0:5] == da[0]:
                    nal.append(int(s[2]))
    print(math.fsum(per))
    print(math.fsum(nal))
    l_per.config(font=("Arial", 16), text='Всего переводов за ' + data + ': ' + str(math.fsum(per)))
    l.config(font=("Arial", 16), text='Всего наличными за ' + data + ': ' + str(math.fsum(nal)))
    l2.config(font=("Arial", 16), text='Итого за ' + data + ': ' + str(math.fsum(nal) + math.fsum(per)))
def total_che():
    global wind1
    wind1 = Tk()
    wind1.title('итог за день')
    wind1.geometry('400x200+500+400')
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
    wind.title('ИТОГИ')
    wind.geometry('770x520+300+260')
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
    cal = Calendar(wind, font="Arial 14", selectmode='day', locale='ru_RU',
                   mindate=mindate, maxdate=maxdate, disabledforeground='blue', background="blue",
                   foreground="white",
                   selectbackground="blue",
                   normalbackground="Khaki",
                   weekendbackground="SaddleBrown",
                   weekendforeground="white",
                   cursor="hand1", year=currentYear, month=currentMonth, day=currentDay)
    # cal.pack(fill="both", expand=True)
    # cal.grid((row=0, column=0)
    cal.place(x=385, y=10)
    #текущая дата всегда выделена
    today_date = datetime.date(year=currentYear, month=currentMonth, day=currentDay)
    cal.calevent_create(today_date, 'Hello World', 'today_date')
    cal.tag_config('today_date', background='blue', foreground='white')
    text = tk.Text(wind, width=30, height=11, bg="Khaki", font=('Arial', 16, 'bold'),
                   fg='Maroon', wrap=tk.WORD)
    text.place(x=10, y=10)
    Label(wind, text='Количество покупателей:',  bg='Goldenrod', bd=0, fg='white',
                     font=('Arial', 18, 'bold')).place(x=10, y=280)

    text2 = tk.Text(wind, width=17, height=8, bg="PaleGoldenrod", font=('Arial', 16, 'bold'),
                   fg='Maroon', wrap=tk.WORD)
    text2.place(x=10, y=320)
    text2.focus()
    i_cheki = Button(wind, text='внести', width=13,  bd=1, bg='SaddleBrown', fg='white',
                     font=('Arial', 12, 'bold'))
    i_cheki.place(x=230, y=320)
    look = Button(wind, text='проссмотреть', width=13, bd=1, bg='SaddleBrown', fg='white',
                     font=('Arial', 12, 'bold'))
    look.place(x=230, y=360)
    diagr = Button(wind, text='диаграмма', width=13, bd=1, bg='SaddleBrown', fg='white',
                  font=('Arial', 12, 'bold'))
    diagr.place(x=230, y=400)

    sbros = Button(wind, text='сброс', width=13, bd=1, bg='SaddleBrown', fg='white',
                   font=('Arial', 12, 'bold'))
    sbros.place(x=230, y=440)
    kn = Button(wind, text='отдали', width=13, bd=1, bg='SaddleBrown', fg='white',
                   font=('Arial', 12, 'bold'))
    kn.place(x=230, y=480)
    kn_diagr_money = Button(wind, text='диаграмма продаж', width=24, bd=1, bg='blue', fg='white',
                font=('Arial', 18, 'bold'))
    kn_diagr_money.place(x=385, y=260)
    l_per = Label(wind, font=("Arial", 16, 'bold'), text='Всего переводов за ', bg='Goldenrod', bd=0, fg='white')
    l_per.place(x=370, y=320)
    l = Label(wind, font=("Arial", 16, 'bold'), text='Всего наличными за ', bg='Goldenrod', bd=0, fg='white')
    l.place(x=370, y=350)
    l2 = Label(wind, font=("Arial", 25, 'bold'), text='Итого за ', bg='Goldenrod', bd=0, fg='white',)
    l2.place(x=400, y=400)
    def otdali():
        text2.delete('1.0', END)
        with open('otdali.txt', 'r', encoding='utf-8') as f:
            fi = f.read()
            text2.insert('1.0', fi)
    kn.config(command=otdali)
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
        root.geometry('1200x700+5+5')
        n = 50
        m = 50
        nadpisi = False

        canv = Canvas(root, width=1120, height=680, bg="white", cursor='pencil')
        canv.create_line(55 + n, 617, 55 + n, 0, width=2, arrow=LAST)
        canv.create_line(100, 665 - m, 1000 + n, 665 - m, width=2, arrow=LAST)
        canv.place(x=20, y=0)
        canv.create_text(400, 640, text='числа в месяце', fill='blue', font=('Arial', 20, 'bold'))
        if nai == 'чел.':
            canv.create_text(35, 300, text='к\nо\nл\nи\nч\nе\nс\nт\nв\nо\n \nл\nю\nд\nе\nй', fill='green', font=('Arial', 20, 'bold'))
        else:
            canv.create_text(35, 300, text='к\nо\nл\nи\nч\nе\nс\nт\nв\nо\n \nр\nу\nб\nл\nе\nй', fill='green', font=('Arial', 20, 'bold'))

        kg = []
        num = []
        mon0 = []
        st = 1
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
                #print('будущее li: ', g)
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
                    #print(li)
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
                        if s[0][3:5] == mesj:
                            tot.append(int(s[z]))
                            #print(tot)
                summer = math.fsum(tot)
                tot_sum.append(summer)
                print('summer=', summer)
                canv.create_line(120, t, 160, t, width=5, fill=cvet, smooth=True, tags='del')
                canv.create_text(255, t, text=mesja1+' - '+str(summer), font=('Arial', 14, 'bold'), fill=cvet, tags='del')
                #t = t + 20
            for i in range(0, len(li)):
                sp1 = li[i].split()
                if mesj == sp1[0][3:5]:
                    kg1.append(int(sp1[z]))
                    num1.append(int(sp1[0][0:2]))
                    #print('людей', kg1)
                    #print('число', num1)
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
                        #t = 140
                canv.delete('del3')
                canv.create_text(930, 650, text='За месяц: ' + str(sum(kg1)),
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

    diagr.config(command=lambda: diagra('people.txt', 1, 'чел.'))
    kn_diagr_money.config(command=lambda: diagra('kalkulator.txt', 1, 'p.'))
    def look_col():
        text2.delete('1.0', END)
        with open('people.txt', 'r') as f:
            fi = f.read()
            text2.insert('1.0', fi)
    look.config(command=look_col)
    def sbrosit():
        text2.delete('1.0', END)
    sbros.config(command=sbrosit)
    hour = ['08', '09', '10', '11', '12', '13', '14', '15', '16', '17']
    def vivod(data):
        #global not_sale
        text2.focus()
        text2.insert('1.0', data + ': ')
        def save_col(d):
            #text2.delete('1.0', END)
            s = text2.get('1.0', END)
            print('длина строки: ', len(s))
            print(text2.get('1.0', END))
            if len(s) <= 13 or len(s) > 20:
                messagebox.showwarning('предупреждение!!!', 'действие выполнить невозможно!!!\nвведите количество покупателей!!!')
            else:
                with open('people.txt', 'a+') as f:
                    f.write(s)
                    messagebox.showinfo('внимание!!!',
                                           'запись внесена!!!')

        i_cheki.config(command=lambda: save_col(data))


        p = 0
        total_buy = 0
        not_sale = False
        with open('kalkulator.txt', 'r') as f:
            all = f.read()
            sp_all = all.splitlines()
            print('выбранная дата: ', data)

            for hou in range(len(hour) - 1):
                #print(hour[hou])

                for i in range(len(sp_all)):
                    s = sp_all[i].split()
                    if s[0] == data:
                        if hour[hou] == s[1][0:2]:
                            p = p + 1
                    else:
                        not_sale = ' в этот час не было продаж'

                #print(hour[hou], ' in date ', data, ' num ', p)
                text.insert(END, '\n          : ' + hour[hou] + '-' + hour[hou + 1] + ' - ' + str(p) + ' чел.')
                total_buy = total_buy + p
                #print('всего ', data, ' : ' + hour[hou] + '-' + hour[hou + 1] + ' - ' + str(total_buy))
                if total_buy == 0:
                    not_sale = True
                p = 0
            if not_sale == True:
                text.insert('1.0', data + ': \nв этот день не было продаж')
                not_sale = False
            else:
                text.insert('1.0', data + ': \nв этот день было: ' + str(total_buy) + ' чел.')

    def update_text(event):
        text.delete('1.0', END)
        text2.delete('1.0', END)

        cal.config(selectbackground="red")
        data = str(cal.selection_get())
        print('выбранная дата : ', data)
        new_data_format = data[8:10] + '-' + data[5:7] + '-' + data[0:4]
        print(new_data_format)

        vivod(new_data_format)
        itog_day2(new_data_format[0:5])

    cal.bind("<<CalendarSelected>>", update_text)
#создаём меню
main_menu = Menu(root, fg='blue', bg='orange', font=('Comic',40, 'bold'), bd=2)
main_menu.configure(fg='blue', bg='orange', font=('Comic',40, 'bold'), bd=2)
main_menu['fg'] = 'green'
file_menu = Menu()
file_menu.add_command(label="open_calculator", command=lambda: rew_tabl(False))
#file_menu.add_command(label="itog_day", command=total_che)
file_menu.add_command(label="col", command=col)
file_menu.add_command(label="itog_day", command=lambda: rew_tabl(True))

root.config(menu=main_menu)
main_menu.add_cascade(label="open", menu=file_menu)

#для кассового чека
canvas9 = Canvas(root, width=200, height=460, borderwidth=0, background="DarkKhaki")
canvas9.pack(side="left", fill="both", expand=True)
canvas10 = Canvas(root, width=250, height=900, borderwidth=0, background="BurlyWood")
canvas10.place(x=580, y=0)
sum_chek = Label(canvas10, text=' 0.0 р. ', fg='red', width=14, font=('Arial', 20, 'bold'))
sum_chek.place(x=5, y=200)
sd_chek = Label(canvas10, text='Сдача с оплаты: ', width=14, font=('Arial', 20, ''))
sd_chek.place(x=10, y=350)
vv_sum = Entry(canvas10, width=14, justif='center', font=('Arial', 20, 'bold'))
vv_sum.place(x=35, y=400)
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
                    but[(z, j)] = Button(scrolled_frame8, text='del', width=4, fg='blue',
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
            sum_chekf()
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



chek_itogo = Button(canvas10, text='сумма', fg='red', width=9, bd=0, command=sum_chekf, font=('Arial', 37, 'bold'))
chek_itogo.place(x=0, y=100)
chek_sdacha = Button(canvas10, text='сдача', fg='lightgreen', width=9, bd=0, command=sdacha_chekf, font=('Arial', 37, 'bold'))
chek_sdacha.place(x=0, y=250)

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
    wind2.title('итоги')
    wind2.geometry('600x200+500+300')
    now_chek = datetime.datetime.now()
    data1 = now_chek.strftime("%d-%m")
    data2 = now_chek.strftime("%d-%m-%Y %H:%M")
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
            print('с какого', s_kakogo)
            for i in range(len(sp_all)):
                s = sp_all[i].split()
                if len(s) == 4:
                    if s[3] == 'перевод':
                        per.append(int(s[2]))
                else:
                        nal.append(int(s[2]))
        print(math.fsum(per))
        print(math.fsum(nal))
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
                #print(s)
                #print(s[0][3:5])
                if len(s) == 4:
                    if s[0][3:5] == m and s[3] == 'перевод':
                        per.append(int(s[2]))
                else:
                    if s[0][3:5] == m:
                        nal.append(int(s[2]))
        print(math.fsum(per))
        print(math.fsum(nal))
        l_per.config(text='Всего переводов за ' + data + ': ' + str(math.fsum(per)))
        l.config(text='Всего наличными за ' + data + ': ' + str(math.fsum(nal)))
        l2.config(text='Итого за ' + data + ': ' + str(math.fsum(nal) + math.fsum(per)))

    def itog_m():
        wind2 = Tk()
        wind2.title('итог за месяц')
        wind2.geometry('300x50+500+550')
        l = Label(wind2, text='Введите номер месяца по образцу (месяц: 04):')
        l.place(x=10, y=0)
        e = Entry(wind2)
        e.place(x=10, y=17)
        e.focus()

        def dest():
            wind2.destroy()

        e.bind('<Return>', lambda en: (itog_mon(e.get()), dest()))

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

    i_cheki = Button(wind2, text='итог за сегодня', width=13, command=lambda: itog_day(data1), bd=1,
                     font=('Arial', 12, ''))
    i_cheki.place(x=10, y=160)
    i_mon = Button(wind2, text='итог за месяц', width=12, command=lambda: itog_m(), bd=1,
                     font=('Arial', 12, ''))
    i_mon.place(x=145, y=160)
    i_all = Button(wind2, text='общий итог', width=12, command=lambda: itog_y(), bd=1,
                   font=('Arial', 12, ''))
    i_all.place(x=270, y=160)
#id_cheki = Button(wind2, text='итог за день', width=14, command=itog_d, bd=1, font=('Arial', 12, ''))
#id_cheki.place(x=200, y=130)
def discount(p):
    try:
        s = chek_itogo['text']
        print(s)
        sp = s.split(".")
        print(sp)
        su = int(sp[0])
        new_sum = su - su * 0.01 * p
        chek_itogo['text'] = str(new_sum)
    except ValueError:
        messagebox.showwarning('ValueError', 'Дейслвие выполнить невозможно!!!')


up_chek = Button(canvas10, text='очистить', width=10, command=chek_up, bd=0, font=('Arial', 30, ''))
up_chek.place(x=10, y=10)
save_sum = Button(canvas10, text='rew', fg='gray', width=4, command=rew_sum, bd=0, font=('Arial', 15, ''))
save_sum.place(x=1, y=400)
save_sum = Button(canvas10, text='5 %', width=4, command=lambda: discount(5), bd=0, font=('Arial', 15, ''))
save_sum.place(x=5, y=440)
save_sum = Button(canvas10, text='10 %', width=4, command=lambda: discount(10), bd=0, font=('Arial', 15, ''))
save_sum.place(x=66, y=440)
save_sum = Button(canvas10, text='15 %', width=4, command=lambda: discount(15), bd=0, font=('Arial', 15, ''))
save_sum.place(x=127, y=440)
save_sum = Button(canvas10, text='20 %', width=4, command=lambda: discount(20), bd=0, font=('Arial', 15, ''))
save_sum.place(x=188, y=440)
save_sum = Button(canvas10, text='25 %', width=4, command=lambda: discount(25), bd=0, font=('Arial', 15, ''))
save_sum.place(x=6, y=480)
save_sum = Button(canvas10, text='30 %', width=4, command=lambda: discount(30), bd=0, font=('Arial', 15, ''))
save_sum.place(x=66, y=480)
save_sum = Button(canvas10, text='35 %', width=4, command=lambda: discount(35), bd=0, font=('Arial', 15, ''))
save_sum.place(x=127, y=480)
save_sum = Button(canvas10, text='40 %', width=4, command=lambda: discount(40), bd=0, font=('Arial', 15, ''))
save_sum.place(x=188, y=480)
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
