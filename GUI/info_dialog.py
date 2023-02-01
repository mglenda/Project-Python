from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivy.core.window import Window
import main as app

Builder.load_file('GUI\\info_dialog.kv')

#types: okOnly,yesNo

def create_dialog(**kargs):
    print(kargs['type'])
    return info_dialog(text=kargs['text']
            ,title=kargs['title'])

class info_dialog(MDDialog):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        app.bindEnter(app.destroy,False,widget=self)