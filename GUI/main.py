import kivymd
from kivymd.app import MDApp
from kivymd.uix.floatlayout import FloatLayout
import login_card as login
from kivy.core.window import Window

class MainLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    

class main(MDApp):
    def build(self):
        Window.maximize()
        self.title = 'Data Toolkits'
        self.root = MainLayout()
        self.root.add_widget(login.LoginCard())
        return
    
    def sign_in(self):
        print('You were logged in successfully.')

def exitApp():
    MDApp.get_running_app().stop()

def enterApp():
    MDApp.get_running_app().sign_in()

if __name__ == "__main__":
    app = main()
    app.run()