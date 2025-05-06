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

class HomeWork_input(FloatLayout):
    def __init__(self, add_task_callback=None,**kwargs):
        super().__init__(**kwargs)
        self.size_hint=(.9, .2)
        self.pos_hint = {'center_x':.5, 'center_y':.725}
        
        with self.canvas.before:
            Color(0.2,0.2,0.456,1)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update, pos=self.update)
        
        title = Label(text='Tarea:', font_size=sp(20), size_hint=(.45,.3), pos_hint={'center_x': 0.25, 'center_y': 0.72})
        add_input = TextInput(hint_text='Escribe una tarea', font_size=sp(20), size_hint=(.90, .3), pos_hint={'center_x': .5, 'center_y': .3})
        add_btn = Add_btn(on_add_callback=lambda: add_task_callback(add_input.text))

        self.add_widget(title)
        self.add_widget(add_btn)
        self.add_widget(add_input)
        
    def update(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class Add_btn(Button):
    def __init__(self, on_add_callback ,**kwargs):
        super().__init__(**kwargs)
        self.on_add_callback = on_add_callback
        self.text = "Agregar"
        self.font_size = sp(20)
        self.size_hint = (.45, .3)
        self.pos_hint = {'center_x':.75, 'center_y':.72}

    def on_press(self, *args):
        if self.on_add_callback:
            self.on_add_callback()

class HomeWork_output(BoxLayout):
    def __init__(self, nombre ,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.nombre = nombre
        
        with self.canvas.before:
            Color(.2,.5,.1,1)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update, pos=self.update)
        check = CheckBox()
        delete_btn = Button(text='X', font_size=sp(20))
        work = Label(text=f'{self.nombre}', font_size=sp(20))
        
        self.add_widget(check)
        self.add_widget(delete_btn)
        self.add_widget(work)
    
    def update(self, *args):
        self.rect.size=self.size
        self.rect.pos=self.pos