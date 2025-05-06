'''
Objetivo: Crear una app de lista de tareas (To-Do App) sencilla.
Características mínimas:
Una caja de texto para escribir tareas.
Un botón para agregar la tarea a una lista.
Una lista que muestre las tareas.
Un botón para eliminar una tarea seleccionada.
'''

from kivy.app import App
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
from kivy.uix.widget import Widget
# dp es para dimensiones fisicas
# sp para textos
from welcome import Screen_btn
from home import HomeWork_input, HomeWork_output

class Welcome(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        with self.canvas.before:
            Color(0.2, 0.6, 0.8, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update, pos=self.update)
        
        master = FloatLayout()

        title = Label(text='Bienvenidos a mi ToDoList', font_size=sp(40), size_hint=(.8, .2), pos_hint={'center_x': .5, 'center_y':.7 })
        screen_btn = Screen_btn(screen=self ,direction='up', font_size=sp(40) ,goal='home', text="Start", size_hint=(.3, .1), pos_hint={'center_x': .5, 'center_y':.4 })
        
        # master.add_widget(self.bg)
        master.add_widget(title)
        master.add_widget(screen_btn)
        self.add_widget(master)
        
    def update(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class Home(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        with self.canvas.before:
            Color(0.3, 0.2, 0.4, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update, pos=self.update)

        master = FloatLayout()
        texto = Label(text='ToDoList', font_size=sp(40), size_hint=(0.4, 0.2), pos_hint={'center_x': .5, 'center_y': .9})
        homework_input = HomeWork_input(add_task_callback=self.add_task)
        self.homework_box = BoxLayout(
            padding=dp(30),
            spacing=dp(30),
            orientation='vertical',
            size_hint=(0.9, 0.15),
            pos_hint={'center_x': .5, 'center_y': .6}
            )
        
        
        master.add_widget(texto)
        master.add_widget(homework_input)
        master.add_widget(self.homework_box)
        self.add_widget(master)
    
    def update(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
    
    def add_task(self, tarea_texto):
        if tarea_texto.strip():
            tarea = HomeWork_output(nombre=tarea_texto)
            self.homework_box.add_widget(tarea)

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Welcome(name='welcome'))
        sm.add_widget(Home(name='home'))
        return sm

if __name__ == '__main__':
    MainApp().run()