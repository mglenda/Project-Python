from tkinter import Widget
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics', 'width', '1366')
Config.set('graphics', 'height', '768')

class MyLayout(GridLayout):
    text = 'auto'
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MyApp(App):
    def build(self):
        #Window.fullscreen = 'auto'
        #Window.fullscreen = False
        fl = MyLayout(size = Window.size)
        fl.rows = 2
        fl.cols = 1
        fl.padding = [50, 50, 50, 50]
        fl.spacing = [20,20]
        
        print(fl.rows)

        b1 = Button(text =fl.text)
        b2 = Button(text =fl.text)
        fl.add_widget(b1)
        fl.add_widget(b2)

        return fl


MyApp().run()