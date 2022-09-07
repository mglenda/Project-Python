## Sample Python application demonstrating the
## How to change button position and size in Kivy.
###################################################
# import modules
import kivy
 
# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App
 
# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button
 
# This layout allows you to set relative coordinates for children.
from kivy.uix.floatlayout import FloatLayout
 
# To change the kivy default settings
# we use this module config
from kivy.config import Config
     
# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)
 
# creating the App class
class Pos_Size_App(App):
     
    def build(self):
 
        # A Relative Layout with a size of (300, 300) is created
        rl = FloatLayout(size =(1000, 1000))
         
        # creating button
        # size of button is 20 % by height and width of layout
        # position is 'center_x':.7, 'center_y':.5
        b1 = Button(size_hint =(.2, .2),
                    pos_hint ={'center_x':.7, 'center_y':.5},
                    text ="pos_hint")
 
        # creating button
        # size of button is 20 % by height and 50 % width of layout
        b2 = Button(size_hint =(.5, .2), 
                    text ="size_hint")
         
         
 
        # adding button to widget
        rl.add_widget(b1)
        rl.add_widget(b2)
         
        # returning widget
        return rl
 
# run the App
if __name__ == "__main__":
    Pos_Size_App().run()