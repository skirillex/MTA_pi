import kivy
kivy.require('1.11.1')

import random

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Ellipse
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.core.window import Window

import mta_times

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]


###need to figure out way for times to update


class TrainGui(BoxLayout):
    def __init__(self,**kwargs):
        super(TrainGui, self).__init__(**kwargs)

        self.dir_options = ["72nd North", "72nd South"]

        self.directions = self.dir_options[0]

        self.colors = [red, green, blue, purple]
        self.trains_list, self.times_list, = self.get_trains()

        #Debug:
        print(self.times_list)
        print(self.trains_list)

        # create widgets to but into layouts:
        self.station_name = Label(text=f"[b]From 72nd St[/b]", markup=True, halign="left", font_size=40, size_hint=(.5, .5),
                             pos_hint={"center_x": .15, "center_y": .5})
            # debugging button
        self.btn = Button(text="Refresh", background_color=random.choice(self.colors), on_press=self.update)
            # this below creates three lists of widgets
        self.train_num, self.dire, self.time_label = self.train_dir_time_list()

        # add all widgets to layouts
        self.add_widget(self.station_name)

        for i in range(0, len(self.train_num)):
            h_layout = BoxLayout(padding=1)
            h_layout.add_widget(self.train_num[i])
            h_layout.add_widget(self.dire[i])
            h_layout.add_widget(self.time_label[i])
            self.add_widget(h_layout)

        self.add_widget(self.btn)
        Clock.schedule_interval(self.update, 10)



    def update(self, event):
        new_train_num, new_dire, new_time_label = self.train_dir_time_list()

        for i in range(0, len(new_train_num)):
            self.train_num[i].source = new_train_num[i].source
            self.dire[i].text = new_dire[i].text
            self.time_label[i].text = new_time_label[i].text




    def get_trains(self):
        return mta_times.get_train(self.directions)

    def train_dir_time_list(self):
        #this method creates 3 lists in the same order to add to the main boxlayout
        #a list of image objects, train_num / a list of direction label objects / a list of time label objects

        self.trains_list, self.times_list, = self.get_trains()
        train_num = []
        dir = []
        time_label = []

        for i in range(0, len(self.trains_list)):

            if self.directions == self.dir_options[0]:

                direction = Label(text="Uptown", size_hint=(.5, .5), halign="left", font_size=20,
                              pos_hint={"center_x": .1, "center_y": .5})
                dir.append(direction)
            elif self.directions == self.dir_options[1]:
                direction = Label(text="Downtown", size_hint=(.5, .5), halign="left", font_size=20,
                              pos_hint={"center_x": .1, "center_y": .5})
                dir.append(direction)

            #conditional statements put the train image object into list
            if self.trains_list[i] == '1':
                img = Image(source = 'C:/Users/Kiril/PycharmProjects/MTA_pi/1_train.png', size_hint=(.7, .7), pos_hint={"center_x":.5, "center_y": .5})
                train_num.append(img)
            elif self.trains_list[i] == '2':
                img = Image(source='C:/Users/Kiril/PycharmProjects/MTA_pi/2_train.png', size_hint=(.7, .7),
                            pos_hint={"center_x": .5, "center_y": .5})
                train_num.append(img)
            else:
                img = Image(source='C:/Users/Kiril/PycharmProjects/MTA_pi/3_train.png', size_hint=(.7, .7),
                            pos_hint={"center_x": .5, "center_y": .5})
                train_num.append(img)

            train_time = self.times_list[i]
            time = Label(text=f"{train_time} Mins", halign="right", font_size=40, size_hint=(.5, .5),
                         pos_hint={"center_x": .9, "center_y": .5})
            time_label.append(time)

        return train_num, dir, time_label




class gui(App):
    def build(self):
        return TrainGui()

if __name__ == '__main__':
    gui().run()