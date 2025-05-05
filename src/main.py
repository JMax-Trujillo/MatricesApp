# archivo main.py

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from welcome import ScreenButton, Login
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

class Welcome(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        master = FloatLayout()
        with self.canvas.before:
            self.background = Image(source='../img/login_fondo.png', allow_stretch=True, keep_ratio=False)
        centro = Login(self)
        master.add_widget(self.background)
        master.add_widget(centro)
        self.add_widget(master)

class Home(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(Label(text='Helloooo', font_size=40))

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Welcome(name='welcome'))
        sm.add_widget(Home(name='home'))
        return sm

if __name__ == '__main__':
    MainApp().run()