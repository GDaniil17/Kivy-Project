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

class MyApp(App, Widget):
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
        print("lis: ", self.lis)
        self.button_grid.clear_widgets()
        self.buttons = []
        self.lis.clear()
        print("re: ", self.refreshed)

        self.output_button = Button(text="Unselected", size_hint=(0.5, 0.5),
                                    font_size=20)  # , pos_hint = {"left":0.1, "top":0.2})
        # self.direct = {'Сражения': 'Battles.txt', 'Мировая история': 'Global History.txt', 'Правители': 'Princes.txt','Реформы': 'Reformations.txt', 'Войны и Восстания': 'Wars and Rebellions.txt'}

        # self.button_symbols = ['Сражения', 'Мировая история', 'Правители', 'Реформы', "Войны и Восстания"]
        # self.cur_theme = "Сражения"
        self.cur_theme = "Unselected"
        self.cur = ""
        # self.cur = "Start"
        self.output_button.bind(on_press=self.change)
        self.output_button.bind(on_press=self.detect)
        self.button_grid.add_widget(self.output_button)
        # self.button_grid.add_widget(self.output_button)

        self.d = Button(text="Next question", pos_hint={'center_x': 0.5, 'center_y': .2}, size_hint=(0.2, 0.1), font_size=25)
        self.d.bind(on_press=self.on_touch_up)
        self.d.bind(on_press=self.detect)
        self.button_grid.add_widget(self.d)
        # self.button_grid.add_widget(self.d)
        #self.refresh(self)


        for i, symbol in enumerate(self.refreshed):
            print(symbol)
            self.buttons.append(Button(text=symbol, pos_hint={'center_x': 0.5, 'center_y': .2}, size_hint=(0.2, 0.1), font_size=25))
            self.buttons[i].bind(on_press=self.something)  # = self.change_theme(symbol))
            self.button_grid.add_widget(self.buttons[i])
            self.lis[self.buttons[i]] = symbol


        # for i, symbol in enumerate(self.refreshed):
        #    print(symbol)
        #    self.buttons.append(Button(text=symbol, pos_hint={'center_x': 0.5, 'center_y': .2}, size_hint=(0.2, 0.1), font_size=25))
        #    self.buttons[i].bind(on_press=self.something)  # = self.change_theme(symbol))
        #    self.button_grid.add_widget(self.buttons[i])
        #    self.lis[self.buttons[i]] = symbol
        # print(self.buttons[i])
        # tex = self.buttons[i].text
        # self.buttons[i].bind(on_release = self.change_theme(tex))
        # self.button_grid.add_widget(self.buttons)

        self.refreshing_btn = Button(text="Refresh", pos_hint={'center_x': 0.5, 'center_y': .2}, size_hint=(0.2, 0.1),
                                     font_size=25)
        self.refreshing_btn.bind(on_press=self.refresh)
        self.button_grid.add_widget(self.refreshing_btn)
        return self.button_grid
        """
        for i, symbol in enumerate(self.refreshed):
            self.buttons.append(
                Button(text=symbol, pos_hint={'center_x': 0.5, 'center_y': .2}, size_hint=(0.2, 0.1), font_size=25))
            self.button_grid.add_widget(self.buttons[i])
            self.lis[self.buttons[i]] = symbol
            # print(self.buttons[i])
            # tex = self.buttons[i].text
            # self.buttons[i].bind(on_release = self.change_theme(tex))
            self.buttons[i].bind(on_press=self.something)  # = self.change_theme(symbol))
        self.button_grid.add_widget(self.buttons)
        return self.button_grid
        """
        # self.button_grid.add_widget(Button(id = str(i), text=symbol, pos_hint={'center_x': 0.5, 'center_y': .2}, size_hint=(0.2,0.1), font_size = 25))
        # print(self.button_grid.id)


    def detect(self, ind):
        print(ind)
        #self.lis[ind] = self.__name__()
        #self.lis[ind] = self.cur_theme
        #print(self.lis)
        """
                Словарь:
                Идекс - Значение
                self.cur_theme = direct[Значение]
        """
       # lis[ind] = #путь

    def on_touch_up(self, event):
        if self.cur_theme == "Unselected":
            self.cur = ""
            if self.refreshed:
                print(self.refreshed)
                for k, v in self.refreshed.items():
                    self.cur_theme = k
                    break
            self.on_touch_up(1)

        if os.path.exists(self.refreshed[self.cur_theme]):
            lines = list(open(self.refreshed[self.cur_theme]).read().split("\n"))
            self.RandomChoice = dict(i.split('— ') for i in lines)
            # direct[]
            #self.change_next()
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
        #self.direct = {'Сражения': 'Battles.txt', 'Мировая история': 'Global History.txt', 'Правители': 'Princes.txt','Реформы': 'Reformations.txt', 'Войны и Восстания': 'Wars and Rebellions.txt'}

        #self.button_symbols = ['Сражения', 'Мировая история', 'Правители', 'Реформы', "Войны и Восстания"]
        #self.cur_theme = "Сражения"
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

        #for i, symbol in enumerate(self.refreshed):
        #    print(symbol)
        #    self.buttons.append(Button(text=symbol, pos_hint={'center_x': 0.5, 'center_y': .2}, size_hint=(0.2, 0.1), font_size=25))
        #    self.buttons[i].bind(on_press=self.something)  # = self.change_theme(symbol))
        #    self.button_grid.add_widget(self.buttons[i])
        #    self.lis[self.buttons[i]] = symbol
            # print(self.buttons[i])
            # tex = self.buttons[i].text
            # self.buttons[i].bind(on_release = self.change_theme(tex))
        #self.button_grid.add_widget(self.buttons)


        #self.refreshing_btn = Button(text="Refresh", pos_hint={'center_x': 0.5, 'center_y': .2}, size_hint=(0.2, 0.1), font_size=25)
        #self.refreshing_btn.bind(on_press = self.refresh)
        #self.button_grid.add_widget(self.refreshing_btn)
        return self.button_grid
    def something(self, op):
        if self.cur_theme != self.lis[op]:
            self.cur_theme = self.lis[op]
            print(self.lis[op])
            self.on_touch_up(op)

if __name__ == "__main__":
  MyApp().run()