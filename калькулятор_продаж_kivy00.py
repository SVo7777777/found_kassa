from kivy.app import App
from kivy.base import runTouchApp
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

layout0 = BoxLayout(orientation="horizontal")
layout1 = BoxLayout(orientation="vertical", padding=10, size_hint=(.4, 1))
layout = GridLayout(cols=1, spacing=1, size_hint_y=None)
root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
root.add_widget(layout)

clear = Button(text='Очистить', font_size=62, markup=True)
solution = Label(text='0.0p.', size_hint=(1, .6), color=[1, 0, 0, 1])
summer = Button(text='Сумма', markup=True, font_size=82, size_hint=(1, 2), color=[1, 0, 0, 1])
change = Button(text='Сдача с суммы', size_hint=(1, .7))
ch = TextInput(text='', halign="center", font_size=45, size_hint=(1, .7))
digkey = Button(text='digit-keyb', font_size=42,)
rew = Button(text='rew', font_size=42)
proc = Button(text='%', font_size=42,)
            #multiline=False, readonly=True, )
layout1.add_widget(clear)
layout1.add_widget(solution)
layout1.add_widget(summer)
layout1.add_widget(change)
layout1.add_widget(ch)
layout1.add_widget(digkey)
layout1.add_widget(rew)
layout1.add_widget(proc)
        # Make sure the height is such that there is something to scroll.

layout.bind(minimum_height=layout.setter('height'))
#layout.add_widget(layout1)
layout0.add_widget(root)
layout0.add_widget(layout1)
but = {}
entry = {}
for i in range(50):
    h_layout = BoxLayout(height=40, size_hint=(None, None))
    for j in range(6):
        if j == 5:
            but[i, j] = Button(text='del', halign="center", font_size=25, size_hint=(None, None), height=40)
            h_layout.add_widget(but[i, j])
        else:
            entry[i, j] = TextInput(halign="center", cursor_color=[0, 0, 1, 1], font_size=25, size_hint=(None, None), height=40, multiline=False)
            h_layout.add_widget(entry[i, j])
            if j == 1:
                entry[i, j].text = 'x'
            if j == 3:
                entry[i, j].text = '='
            if j == 0:
                entry[i, j].halign = 'right'
            if j == 2:
                entry[i, j].halign = 'left'

    layout.add_widget(h_layout)
def my_function(keycode):
    if keycode == 40:
        entry[1, 2].focus = True
        print('hi')



entry[1, 0].focus = True
entry[1, 0].bind(on_key_down=lambda keycode: (my_function)) #focus(), un_bind(0)))
runTouchApp(layout0)





