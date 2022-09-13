from queue import Empty
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

class CaptionLabel(Label):
    pass

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        quest_frame = QuestionLayout(anchor_x ='center', anchor_y ='center',size_hint=(1, .4))
        self.answer_frame = AnswerLayout(size_hint=(1, .6))
        self.add_widget(quest_frame)
        self.add_widget(self.answer_frame)
        self.question = CaptionLabel(size_hint=(1.0, 1.0), halign="center", valign="middle")
        self.question.bind(size = self.question.setter('text_size'))
        quest_frame.add_widget(self.question)
        self.answer_frame.padding = [50, 0, 50, 50]
        self.answer_frame.spacing = [10,10]
    
    def nextQuestion(self):
        self.answer_frame.rows = 2
        self.answer_frame.cols = 2
        self.answer_frame.clear_widgets()
        if len(app_data) > 0:
            self.question.text = app_data[0]['quest']
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

    def onPress(self,*args):
        self.pressed = True
    
    def onRelease(self,*args):
        self.pressed = False
        if self.valid == 'y':
            print('yes')
        else:
            print('no')
        App.get_running_app().root.nextQuestion()
    
    def on_mouseover(self, window, pos):
        self.hovered = self.collide_point(*pos)
        if self.hovered:
            self.background_color = [0,1,0,1]
        else:
            self.background_color = [1,1,1,1]
        
    
class MyApp(App):
    def build(self):
        load_buttons_data()
        self.root = MainLayout(orientation='vertical')
        self.root.nextQuestion()
        return self.root


MyApp().run()