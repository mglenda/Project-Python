from kivymd.uix.behaviors.focus_behavior import FocusBehavior
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.navigationrail import MDNavigationRailItem
from kivy.lang import Builder

Builder.load_file('GUI\\focusInheritance.kv')

class FocusButton(MDRaisedButton, FocusBehavior):
    pass