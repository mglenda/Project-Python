from kivy.config import Config

#Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '1400')
Config.set('graphics', 'height', '800')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('kivy', 'exit_on_escape', '0')

import kivymd
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
import GUI.login_card as login
import GUI.mainMenuScreen as myScreen
from kivy.core.window import Window

class MainLayout(MDFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
class main(MDApp):
    _binders = {}
    _keyLock = {}

    def build(self):
        Window.maximize()
        self.title = 'Data Toolkits'
        self.root = MainLayout()
        #self.root.add_widget(login.LoginCard())
        self.root.add_widget(myScreen.MainMenuScreen())
        Window.bind(on_key_down=self._on_keyboard_down)
        return

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if self.isKeyUnlocked(keyCode=keycode):
            self.exec_keyFunc(keyCode=keycode)

    def exec_keyFunc(self,keyCode):
        self.keyLock(keyCode=keyCode)
        if str(keyCode) in self._binders.keys() and self._binders[str(keyCode)] != None:
            self._binders[str(keyCode)]['func'](**self._binders[str(keyCode)]['funcKargs'])
        self.keyUnlock(keyCode=keyCode)

    def isKeyUnlocked(self,keyCode):
        return True if str(keyCode) not in self._keyLock.keys() else not self._keyLock[str(keyCode)]

    def keyLock(self,keyCode):
        self._keyLock[str(keyCode)] = True

    def keyUnlock(self,keyCode):
        self._keyLock[str(keyCode)] = False
    
    def sign_in(self):
        self.root.add_widget(myScreen.MainMenuScreen())

def bindKey(func,key,**kargs):
    app = MDApp.get_running_app()
    if str(key) not in app._binders.keys() or app._binders[str(key)] == None:
        app._binders[str(key)] = {
            'func': func
            ,'funcKargs': kargs
            ,'__func':None
            ,'__funcKargs':None
        }
    else:
        app._binders[str(key)]['__func'] = app._binders[str(key)]['func']
        app._binders[str(key)]['__funcKargs'] = app._binders[str(key)]['funcKargs']
        app._binders[str(key)]['func'] = func
        app._binders[str(key)]['funcKargs'] = kargs

def unbindKey(key,_former=False):
    app = MDApp.get_running_app()
    if str(key) in app._binders.keys() and app._binders[str(key)] != None:
        if _former:
            app._binders[str(key)]['func'] = app._binders[str(key)]['__func']
            app._binders[str(key)]['funcKargs'] = app._binders[str(key)]['__funcKargs']
            app._binders[str(key)]['__func'] = None
            app._binders[str(key)]['__funcKargs'] = None
        else:
            app._binders[str(key)] = None

def exitApp(btn=None):
    MDApp.get_running_app().stop()

def enterApp():
    MDApp.get_running_app().sign_in()

def display(widget):
    MDApp.get_running_app().root.add_widget(widget)

def destroy(widget):
    MDApp.get_running_app().root.remove_widget(widget)

if __name__ == "__main__":
    app = main()
    app.run()