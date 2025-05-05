# archivo welcome.py

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.uix.widget import Widget

class ScreenButton(Button):
    def __init__(self, screen, goal, direction, **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.goal = goal
        self.direction = direction
        self.text = 'Ingresar'
        self.font_size = 24
        self.size_hint = (None, None)
        self.size = (dp(200), dp(50))
        self.pos_hint = {"center_x": 0.5}

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class Login(FloatLayout):
    def __init__(self, screen, **kwargs):
        super().__init__(**kwargs)
        self.screen = screen

        # Caja centrada
        login_box = BoxLayout(
            orientation='vertical',
            spacing=dp(15),
            padding=dp(30),
            size_hint=(None, None),
            size=(dp(400), dp(400)),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        # Fondo redondeado para el login
        with login_box.canvas.before:
            Color(192/255, 232/255, 249/255, 0.85)
            self.bg = RoundedRectangle(size=login_box.size, pos=login_box.pos, radius=[20])
        login_box.bind(pos=self.update_bg, size=self.update_bg)

        # Widgets del login
        title = Label(text='Iniciar Sesión', font_size=32, size_hint=(1, None), height=dp(50), color=(0, 0, 0, 1), pos_hint={"center_x": 0.5, "center_y": 0.90})
        username = TextInput(hint_text='Usuario', font_size=20, size_hint=(1, None), height=dp(50), multiline=False)
        password = TextInput(hint_text='Contraseña', font_size=20, size_hint=(1, None), height=dp(50), multiline=False, password=True)
        btn_screen = ScreenButton(self.screen, direction='up', goal='home')

        # Agregar widgets al layout
        login_box.add_widget(title)
        login_box.add_widget(Widget(size_hint_y=None, height=dp(40)))
        login_box.add_widget(username)
        login_box.add_widget(password)
        login_box.add_widget(btn_screen)

        self.add_widget(login_box)

    def update_bg(self, *args):
        self.bg.size = self.children[0].size
        self.bg.pos = self.children[0].pos
