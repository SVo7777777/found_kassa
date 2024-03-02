from kivy.app import App
from kivy.base import runTouchApp
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

layout = BoxLayout(orientation="horizontal", padding=10)

layout1 = BoxLayout(orientation="vertical")
layout2 = GridLayout(cols=1, spacing=10, size_hint_y=1)

label = Label(text="Hello, World!")
layout1.add_widget(label)

button = Button(text="Click me!")
layout1.add_widget(button)
        # Make sure the height is such that there is something to scroll.
layout2.bind(minimum_height=layout.setter('height'))
#layout.add_widget(layout1)
layout.add_widget(layout2)

for i in range(20):
    h_layout = BoxLayout()
    for j in range(7):
        button = TextInput(halign="center", font_size=25)
        h_layout.add_widget(button)
    layout2.add_widget(h_layout)
root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
root.add_widget(layout2)
runTouchApp(root)





