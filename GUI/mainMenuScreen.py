from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
import GUI.mainMenuComponents as comp
import main as app
from itertools import cycle
import core.constants as const
import core.imports as imports
from kivymd.uix.widget import Widget

Builder.load_file('GUI\\mainMenuScreen.kv')

class MainMenuScreen(MDFloatLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.menuButtons = [
            self.ids.head.ids.btn_home 
            ,self.ids.head.ids.btn_imports 
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
            elif btn == self.ids.head.ids.btn_imports:
                self.load_imports()

    def refresh_screen(self,screen=None):
        try:
            self.remove_widget(self.screen)
        except AttributeError:
            pass
        self.screen = screen
        if screen != None:
            self.add_widget(screen)

    def load_home(self):
        app.unbindDropFunc()
        self.refresh_screen(comp.MainScreen())
        self.title = self.screen.ids.title
        self.menu_layout = self.screen.ids.menu_layout
        self.title.text = 'Home'
        imports = comp.MenuCardButtonContainer(mainScreen=self)
        imports.set_title('Imports')
        imports.set_icon('database-cog')
        imports.bind(on_release=lambda x=self: x.mainScreen.load_section(x.mainScreen.menuButtons[1]))
        self.menu_layout.add_widget(imports)
        self.menu_layout.add_widget(Widget())
        
    def load_imports(self):
        self.refresh_screen(comp.ImportScreen())
        app.bindDropFunc(self.load_import_data)

    def load_import_data(self,filename):
        print(imports.load_import(filename.decode("utf-8")))
