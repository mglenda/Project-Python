from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
import GUI.mainMenuComponents as comp
import main as app

Builder.load_file('GUI\\mainMenuScreen.kv')

class mainMenuScreen(MDFloatLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ids.footer.ids.btn_exit.bind(on_release=app.exitApp)