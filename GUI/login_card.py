from kivymd.uix.card import MDCard
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.core.window import Window
import GUI.info_dialog as i_dlg
import main as app
import core.login as l
import core.db_actions as con
import core.constants as const

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
        self.ids.btn_login.bind(on_release=self.login)
        self.ids.btn_close.bind(on_release=app.exitApp)
        app.bindKey(func=self.login,key=const.key_ENTER)
        app.bindKey(func=app.exitApp,key=const.key_ESC)

    def login(self,btn=None):
        uid = self.ids.uid.text
        pwd = self.ids.pwd_field.ids.pwd.text
        if con.check_ping('10.10.10.218'):
            if l.login_verify(uid,pwd):
                app.destroy(self)
                app.enterApp()
                app.unbindKey(const.key_ENTER)
                app.unbindKey(const.key_ESC)
            else:
                i_dlg.create_dialog(
                    text="Looks like you've provided invalid username and password combination."
                    ,title="Unable To Login"
                    ,type='okOnly'
                ).open()
        else:
            i_dlg.create_dialog(
                text="Cannot connect to the server."
                ,title="Warning"
                ,type='okOnly'
            ).open()