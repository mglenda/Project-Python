import kivy
from kivy.uix.label import Label
from tkinter import Widget
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.config import Config
import xml.etree.ElementTree as ET

kivy.require("2.1.0")

Config.set('graphics', 'width', '1366')
Config.set('graphics', 'height', '768')
Config.set('graphics', 'borderless', '1')

app_data = []
buttons_data_filename = "buttons_data.xml"

def load_buttons_data():
    try:
        myroot = ET.parse(buttons_data_filename).getroot()
        for q in myroot.findall('task'):
            t_d = {"type" : q.attrib['type'], "quest" : q.find("question").text}
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

def raiseErrorPopup(msg):
    content = Button(text=msg)
    popup = Popup(title='Error',content=content, auto_dismiss=False,size_hint=(None, None), size=(400, 400))
    content.bind(on_press=App.get_running_app().stop)
    popup.open()

class AnswerLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class QuestionLayout(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        quest_frame = QuestionLayout(anchor_x ='center', anchor_y ='center',size_hint=(1, .4))
        answer_frame = AnswerLayout(size_hint=(1, .6))
        self.add_widget(quest_frame)
        self.add_widget(answer_frame)
        question = Label(size_hint=(1.0, 1.0), halign="center", valign="middle")
        question.bind(size = question.setter('text_size'))
        quest_frame.add_widget(question)
        answer_frame.rows = 2
        answer_frame.cols = 2
        answer_frame.padding = [50, 0, 50, 50]
        answer_frame.spacing = [10,10]
        if len(app_data) > 0:
            question.text = app_data[0]['quest']
            for b in app_data[0]['buttons']:
                answer_frame.add_widget(AnswerButton(text = b["desc"],valid=b["val"]))

class AnswerButton(Button):
    def __init__(self, valid, **kwargs):
        super().__init__(**kwargs)
        self.valid = valid

    def onClick(self,*args):
        if self.valid == 'y':
            print('yes')
        else:
            print('no')
    
class MyApp(App):
    def build(self):
        load_buttons_data()
        self.root = MainLayout(orientation='vertical')
        return self.root


MyApp().run()