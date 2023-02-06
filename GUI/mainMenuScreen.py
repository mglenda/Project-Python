from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
from GUI.mainMenuSide import mainMenuSide
from GUI.mainMenuFooter import mainMenuFooter

Builder.load_file('GUI\\mainMenuScreen.kv')

class mainMenuScreen(MDFloatLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_widget(mainMenuFooter())
        self.add_widget(mainMenuSide())