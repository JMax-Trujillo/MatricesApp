from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.metrics import dp, sp
from kivy.core.window import Window

class Screen_btn(Button):
    def __init__(self, screen, direction, goal, **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
        self.size_hint=(None, None)
        self.size=(Window.width*0.3, Window.height*0.2)
        self.pos_hint={'center_x':0.5, 'center_y':0.3}
    
    def on_press(self, *args):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal