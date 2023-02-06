from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivy.core.window import Window
from GUI.focusInheritance import FocusButton
import main as app
import core.constants as const

Builder.load_file('GUI\\info_dialog.kv')

#types: okOnly,yesNo

def create_dialog(**kargs):
    i_d = None
    if kargs['type'] == 'okOnly':
        i_d = info_dialog(buttons=[
                info_okButton(
                    text="Ok"
                    ,on_release=lambda _: i_d.dismiss()
                    )
                ]
                ,type='alert'
            )
        app.bindKey(func=i_d.dismiss,key=const.key_ENTER)

    i_d.text = i_d.text.format(kargs['text'])
    i_d.title = i_d.title.format(kargs['title'])
    return i_d

class info_dialog(MDDialog):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
    def dismiss(self, *_args, **kwargs):
        _return = super().dismiss(*_args, **kwargs)
        app.unbindKey(key=const.key_ENTER, _former=True)
        return _return

class info_okButton(FocusButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)