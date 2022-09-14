import kivy
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.config import Config
from kivy.graphics import *
import xml.etree.ElementTree as ET

kivy.require("2.1.0")

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

app_data = []
buttons_data_filename = "buttons_data.xml"

def load_buttons_data():
    try:
        myroot = ET.parse(buttons_data_filename).getroot()
        for q in myroot.findall('task'):
            t_d = {"type" : q.attrib['type'], "quest" : q.find("question").find("description").text, "font_size" : q.find("question").find("font_size").text}
            if t_d['type'] == 'q':
                b_l = []
                for b in q.findall('button'):
                    b_l.append({"desc" : b.find('description').text,"val" : b.find('valid').text})
                t_d["buttons"] = b_l
            app_data.append(t_d)
    except AttributeError:
        raiseErrorPopup('An error has occured during buttons_data.xml parsing, please check file validity.')
    except FileNotFoundError:
        raiseErrorPopup(buttons_data_filename + ' file is missing')


def App_Quit(*args):
    App.get_running_app().stop()

class PopUpButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_release=App_Quit)

def raiseErrorPopup(msg):
    content = PopUpButton(text=msg)
    popup = Popup(title='Error',content=content, auto_dismiss=False,size_hint=(None, None), size=(250, 250))
    popup.open()

class AnswerLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class QuestionLayout(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class QuestionLabel(Label):
    pass

class MenuLayout(BoxLayout):
    pass

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_frame = MenuLayout(orientation='horizontal', size_hint=(1, .1))
        quest_frame = QuestionLayout(anchor_x ='center', anchor_y ='center',size_hint=(1, .55))
        self.answer_frame = AnswerLayout(size_hint=(1, .35))
        self.add_widget(self.menu_frame)
        self.add_widget(quest_frame)
        self.add_widget(self.answer_frame)
        self.question = QuestionLabel(size_hint=(1, 1), halign="center", valign="middle")
        quest_frame.add_widget(self.question)
        self.answer_frame.padding = [10, 0, 10, 10]
        self.answer_frame.spacing = [10,10]
    
    def nextQuestion(self):
        self.answer_frame.rows = 2
        self.answer_frame.cols = 2
        self.answer_frame.clear_widgets()
        if len(app_data) > 0:
            self.question.text = app_data[0]['quest']
            self.question.font_size = app_data[0]['font_size']
            for b in app_data[0]['buttons']:
                self.answer_frame.add_widget(AnswerButton(text = b["desc"],valid=b["val"]))
            app_data.pop(0)
    

class AnswerButton(Button):
    def __init__(self, valid, **kwargs):
        super().__init__(**kwargs)
        self.valid = valid
        self.pressed = False
        self.hovered = False
        Window.bind(mouse_pos=self.on_mouseover)
        Window.bind(on_mouse_down=self.on_mouse_down)
        Window.bind(on_mouse_up=self.on_mouse_up)
        self.b_col = self.normal_col

    def onPress(self):
        pass
    
    def onRelease(self):
        if self.valid == 'y':
            print('yes')
        else:
            print('no')
        App.get_running_app().root.nextQuestion()
    
    def on_mouseover(self, window, pos):
        self.hovered = self.collide_point(*pos)
        if self.hovered and not self.pressed:
            self.b_col = self.hover_col
        elif not self.pressed:
            self.b_col = self.normal_col

    def on_mouse_down(self, window, x, y, button, modifiers):
        if self.hovered:
            self.pressed = True
            self.b_col = self.press_col
            self.onPress()

    def on_mouse_up(self, window ,x, y,button, modifiers):
        if self.hovered:
            if self.pressed:
                self.onRelease()
            self.b_col = self.hover_col
        else:
            self.b_col = self.normal_col
        self.pressed = False
    
class MyApp(App):
    def build(self):
        load_buttons_data()
        self.root = MainLayout(orientation='vertical')
        self.root.nextQuestion()
        return self.root

MyApp().run()