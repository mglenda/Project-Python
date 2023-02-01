import kivymd
from kivymd.app import MDApp
from kivymd.uix.floatlayout import FloatLayout
import GUI.login_card as login
from kivy.core.window import Window

class MainLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
class main(MDApp):
    enterFunc = None
    enterParams = None
    enterKeep = False
    _enterFunc = None
    _enterParams = None

    def build(self):
        Window.maximize()
        self.title = 'Data Toolkits'
        self.root = MainLayout()
        self.root.add_widget(login.LoginCard())
        Window.bind(on_key_down=self._on_keyboard_down)
        return

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40 and self.enterFunc is not None:
            func,params = self.enterFunc,self.enterParams
            if not self.enterKeep:
                self.enterFunc = self._enterFunc
                self.enterParams = self._enterParams
            func(**params)
    
    def sign_in(self):
        pass

def bindEnter(func,keep,**kargs):
    app = MDApp.get_running_app()
    app._enterFunc = app.enterFunc
    app._enterParams = app.enterParams
    app.enterFunc = func
    app.enterParams = kargs
    app.enterKeep = keep

def exitApp():
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