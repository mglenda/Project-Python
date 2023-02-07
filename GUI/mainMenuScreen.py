from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
import GUI.mainMenuComponents as comp
import main as app
from itertools import cycle
import core.constants as const

Builder.load_file('GUI\\mainMenuScreen.kv')

class mainMenuScreen(MDFloatLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.menuButtons = [
            self.ids.head.ids.btn_home 
            ,self.ids.head.ids.btn_toolkits 
        ]
        for btn in self.menuButtons:
            btn.bind(on_release=self.load_section)
        self.ids.footer.ids.btn_exit.bind(on_release=app.exitApp)
        app.bindKey(func=self.load_next_section,key=const.key_TAB)

        self.load_section()
    
    def button_activate(self,btn):
        for b in self.menuButtons:
            if b.isActive():
                b.deactive()
        btn.activate()

    def load_next_section(self):
        try:
            b = self.menuButtons[self.curSec + 1]
        except IndexError:
            b = self.menuButtons[0]
        self.load_section(btn=b)

    def load_section(self,btn=None):
        btn = self.ids.head.ids.btn_home if btn == None else btn
        self.curSec = self.menuButtons.index(btn)
        if not btn.isActive():
            self.button_activate(btn=btn)
        #Section Identify
        if btn == self.ids.head.ids.btn_home:
            self.load_home()
        elif btn == self.ids.head.ids.btn_toolkits:
            self.load_toolkits()

    def load_home(self):
        pass

    def load_toolkits(self):
        pass