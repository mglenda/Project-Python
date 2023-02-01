from kivymd.uix.card import MDCard
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.core.window import Window
import GUI.focusButton
import GUI.info_dialog as i_dlg
import main as app
import core.login as l

Builder.load_file('GUI\\login_card.kv')

class PasswordTextField(MDRelativeLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class UserNameTextField(MDTextField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class LoginCard(MDCard):

    def __init__(self) -> None:
        super().__init__()
        self.ids.uid.focus = True
        self.ids.btn_login.bind(on_press=self.button_click)
        self.ids.btn_close.bind(on_press=self.button_click)
        app.bindEnter(self.login,True)

    def button_click(self,btn):
        if btn == self.ids.btn_login:
            self.login()
        else:
            app.exitApp()

    def login(self):
        uid = self.ids.uid.text
        pwd = self.ids.pwd_field.ids.pwd.text
        if l.login_verify(uid,pwd):
            app.destroy(self)
            app.enterApp()
        else:
            app.display(i_dlg.create_dialog(
                text="Something happened, but is unclear what exactly."
                ,title="Warning"
                ,type='okOnly'
            ))