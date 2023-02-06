from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton
from kivymd.uix.tooltip import MDTooltip
from kivy.animation import Animation

Builder.load_file('GUI\\mainMenuComponents.kv')

class MainMenuButton(MDIconButton, MDTooltip):
    bg_cl_enter = [1, 1, 1, 0.2]
    bg_cl_normal = [1, 1, 1, 0]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_enter(self, *args) -> None:
        self.md_bg_color = self.bg_cl_enter
        Animation(scale_x=1.15,scale_y=1.15,t="out_quad",d=0.2,).start(self)
        return super().on_enter(*args)

    def on_leave(self) -> None:
        self.md_bg_color = self.bg_cl_normal
        Animation(scale_x=1,scale_y=1,t="out_quad",d=0.2,).start(self)
        return super().on_leave()

class MainMenuFooter(MDBoxLayout):
    pass

class MainMenuSide(MDBoxLayout):
    pass