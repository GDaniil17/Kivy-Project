import glob
import os
import random
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class Quiz(App, Widget):
    RandomChoice = {}
    lis = {}
    #avaliable_lis = {}
    refreshed = {}
    button_grid = GridLayout(cols=1)  # , size_hint_x=0.5)
    #dictionary = {}
    buttons = []
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

    def build(self):
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

if __name__ == "__main__":
    Quiz().run()