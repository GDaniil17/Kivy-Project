import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from Trier import Quiz
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from Trier import Quiz

#########################################################

import glob
import os
import random
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

r = ['Сражения','Мировая история','Правители','Реформы',"Войны и Восстания"]
direct = {'Сражения': 'Battles.txt', 'Мировая история': 'Global History.txt', 'Правители': 'Princes.txt', 'Реформы': 'Reformations.txt', 'Войны и Восстания': 'Wars and Rebellions.txt'}

class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != self.password.text and self.text.namee != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class TestWindow(Screen, Widget):
    RandomChoice = {}
    lis = {}
    #avaliable_lis = {}
    refreshed = {"": "Daniil.txt"}
    button_grid = GridLayout(cols=1)  # , size_hint_x=0.5)
    #dictionary = {}
    buttons = []
    cur_theme = ""
    
    def refresh(self, state):
        self.refreshed = {}
        for i in [i for i in os.listdir() if i != "users.txt" and i.endswith(".txt")]:
            temp = (i[:i.find(".txt")])
            self.refreshed[temp] = i

        #for i in self.buttons:
        #    self.lis.popitem(i)
            #self.button_grid.remove_widget(i)
        #print("lis: ", self.lis)
        self.button_grid.clear_widgets()
        self.buttons = []
        self.lis.clear()

        self.output_button = Button(text="Unselected", size_hint=(0.5, 0.5),
                                    font_size=20)  # , pos_hint = {"left":0.1, "top":0.2})

        self.cur_theme = "Unselected"
        self.cur = ""

        self.output_button.bind(on_press=self.change)
        self.output_button.bind(on_press=self.detect)
        self.button_grid.add_widget(self.output_button)

        self.d = Button(text="Next question", pos_hint={'center_x': 0.5, 'center_y': .2}, size_hint=(0.2, 0.1), font_size=25)
        self.d.bind(on_press=self.on_touch_up)
        self.d.bind(on_press=self.detect)
        self.button_grid.add_widget(self.d)

        for i, symbol in enumerate(self.refreshed):
            #print(symbol)
            self.buttons.append(Button(text=symbol, pos_hint={'center_x': 0.5, 'center_y': .2}, size_hint=(0.2, 0.1), font_size=25))
            self.buttons[i].bind(on_press=self.something)
            self.button_grid.add_widget(self.buttons[i])
            self.lis[self.buttons[i]] = symbol

        self.refreshing_btn = Button(text="Refresh", pos_hint={'center_x': 0.5, 'center_y': .2}, size_hint=(0.2, 0.1),
                                     font_size=25)
        self.refreshing_btn.bind(on_press=self.refresh)
        self.button_grid.add_widget(self.refreshing_btn)
        return self.button_grid


    def detect(self, ind):
        pass
        #print(ind)

    def on_touch_up(self, event):
        if self.cur_theme == "Unselected": #or len(self.buttons) != 0:
            self.cur = ""
            if self.refreshed:
                print(self.refreshed)
                for k, v in self.refreshed.items():
                    self.cur_theme = k
                    self.on_touch_up(1)
        elif os.path.exists(self.refreshed[self.cur_theme]):
            lines = list(open(self.refreshed[self.cur_theme]).read().split("\n"))
            tr = False
            for i in lines:
                if '— ' in i:
                    tr = True
                    break
            if len(lines) != 0 and tr:
                self.RandomChoice = dict(i.split('— ') for i in lines)
                if len(self.RandomChoice.keys()) != 0:
                    tmp = random.choice(list(self.RandomChoice.keys()))
                    self.cur = tmp
                    self.output_button.text = self.cur

    def change(self, *args):
        if len(self.RandomChoice) != 0 and self.cur != "":
            if self.cur == self.output_button.text:
                self.output_button.text = self.RandomChoice[self.cur]
            else:
                self.output_button.text = self.cur
        else:
            self.output_button.text = "Unselected"

    def __init__():
        self.output_button = Button(text = "Unselected", size_hint = (0.5, 0.5), font_size = 20)#, pos_hint = {"left":0.1, "top":0.2})
        self.cur_theme = "Unselected"
        self.cur = ""
        #self.cur = "Start"
        self.output_button.bind(on_press = self.change)
        self.output_button.bind(on_press = self.detect)
        self.button_grid.add_widget(self.output_button)
        #self.button_grid.add_widget(self.output_button)

        self.d = Button(text="Start", pos_hint={'center_x': 0.5, 'center_y': .2}, size_hint=(0.2,0.1), font_size = 25)
        self.d.bind(on_press = self.on_touch_up)
        self.d.bind(on_press=self.detect)
        self.button_grid.add_widget(self.d)
        #self.button_grid.add_widget(self.d)
        self.refresh(self)
        return self.button_grid

    def something(self, op):
        if self.cur_theme != self.lis[op]:
            self.cur_theme = self.lis[op]
            #print(self.lis[op])
            self.on_touch_up(op)

        
class Window(Screen):
    def build(self):
        Quiz().run()

class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    #current = ""

    def logOut(self):
        sm.clear_widgets()
        sm.cls()
        #sm.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created
        #sm.clear_widgets()
        #sm.current = "test"

class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("users.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), MainWindow(name="main"), (Window(name = "test"))]#, TestWindow(name="quiz")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
