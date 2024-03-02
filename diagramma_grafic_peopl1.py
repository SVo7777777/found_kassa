import random
from tkinter import *
from tkinter import ttk, messagebox, filedialog
import math
import datetime

root = Tk()
root.geometry('1200x700+5+5')
n = 50
m = 50
canv = Canvas(root, width=1120, height=680, bg="pink", cursor='pencil')
canv.create_line(45+n, 1000, 45+n, 50, width=2, arrow=LAST)
canv.create_line(10, 650-m, 1000+n, 650-m, width=2, arrow=LAST)
canv.place(x=20,y=0)
canv.create_text(400, 640, text='числа в месяце', fill='blue', font=('Arial', 20, 'bold'))
canv.create_text(35, 300, text='к\nо\nл\nи\nч\nе\nс\nт\nв\nо', fill='green', font=('Arial', 20, 'bold'))
kg = []
num = []
mon = []
color = ['green', 'orange', 'red', 'blue']
with open('people.txt', 'r') as file:
    line = file.read()
    li = line.splitlines()
    print(li)
    st = li[1].split()
    mon.append(st[0][3:5])
    for i in range(len(li)):
        sp = li[i].split()
        kg.append(int(sp[1]))
        num.append(int(sp[0][0:2]))
        if mon[-1] != sp[0][3:5]:
            mon.append(sp[0][3:5])
        #print(sp[5])
#print(kg)
print(mon)
print(max(kg))
max_kg = max(kg)
print(max_kg)
k = max_kg + 10
print(k)
print(k // 10)
for i in range(32):#ось х с числами месяца
    canv.create_text(50 + i * 30 + n, 660-m, text=str(i),  fill='blue', font=('Arial', 10, 'bold'))
for i in range(k // 10 + 1):#ось у с килограммами
    canv.create_text(30+n, 660 - 5 * i * 10-m, text=str(i * 10), fill='green', font=('Arial', 10, 'bold'))

def diagr(mesj, cvet):
    global nadpisi, total, t
    kg1 = []
    num1 = []
    print('month = ', mesj)
    inde = mes3.index(mesj)
    mesja = mes[inde]
    print(mesja)
    if total == True:
        ind = mes.index(mesja)
        mesja1 = mes2[ind]
        print(mesja1)
        canv.create_line(120, t, 160, t,  width=5, fill=cvet, smooth=True, tags='del')
        canv.create_text(210, t, text=mesja1, font=('Arial', 12), fill=cvet, tags='del')
        t = t + 20
    for i in range(1, len(li)):
        sp1 = li[i].split()
        if mesj == sp1[0][3:5]:
            kg1.append(int(sp1[1]))
            num1.append(int(sp1[0][0:2]))
            #print(kg1)
            #print(num1)
            for j in range(len(kg1)):#точки графика число и кг.
                canv.create_oval(50 + num1[j] * 30+n, 660 - 5 * kg1[j]-m, 50 + num1[j] * 30 + n + 12, 660 - 5 * kg1[j] + 12-m, fill=cvet, outline=cvet, tags='del')
                if j > 0:
                    canv.create_line(50 + num1[j-1] * 30+5+n, 660 - 5 * kg1[j-1]+5-m, 50 + num1[j] * 30+5+n, 660 - 5 * kg1[j]+5-m, width=5, fill=cvet, smooth=True, tags='del')

                #canv.create_text(50 + num[j] * 30 + 79+n, 664 - 5 * kg[j]-m, text=str(num[j]) + 'июня: ' + str(kg[j]) + 'кг.', anchor=CENTER,fill='black', font=('Arial', 14, 'bold'))
                l = Label(canv, text=str(num1[j]) + mesja + ' ' + str(kg1[j]) + 'чел.',  fg=cvet, font=('Arial', 8))
                if nadpisi == True:
                    l.place(x=50 + num1[j] * 30 + 14+n, y=655 - 5 * kg1[j]-m)
    nadpisi = False

                #root.root_attributes("-transparentcolor", cvet)
            # canv.create_oval(50+2*30, 660-5*num[j],50+2*30+5, 660-5*num[j]+5, fill='blue')
nadpisi = False
total = False

def total_di():
    global total, t
    total = True
    t = 20
    for mo in range(len(mon)):
        diagr(mon[mo], color[mo])
def selected(event):
    global nadpisi
    nadpisi = True
    m1 = combobox.get()
    ind = mes2.index(m1)
    diagr(mes3[ind], random.choice(color))
total_diagr = Button(root, text='общая', command=total_di, width=8)
total_diagr.place(x=1120, y=50)
def clear():
    global total
    canv.delete('del')
    total = False
    for w in canv.winfo_children():
        if w.winfo_class() == "Label":
            w.destroy()

clean = Button(root, text='del', command=clear, width=8)
clean.place(x=1120, y=110)
mes = ['месяц', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
mes2 = ['месяц', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
mes3 = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
combobox = ttk.Combobox(root, values=mes2, state="readonly", width=7, font=('Comic', 10, 'bold'))
combobox.place(x=1120, y=80)
inf = Label(root, bg ='lightblue', fg='blue', font=('Arial', 20, 'bold'))
#inf.place(x=710, y=50)#y=150
combobox.bind("<<ComboboxSelected>>", selected)
combobox.set('месяц')
root.mainloop()
