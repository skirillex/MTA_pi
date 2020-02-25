import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window


from datetime import datetime

import mta_times

class TrainGui(BoxLayout):
    def __init__(self,**kwargs):
        super(TrainGui, self).__init__(**kwargs)
        self.count = 0

        self.train_directions_flag = False
        self.dir_options = ["72nd North", "72nd South"]

        self.directions = self.dir_options[0]

        self.trains_list, self.times_list, = self.get_trains()

        # Debug:
        #print(self.times_list)
        #print(self.trains_list)

        # create widgets to but into layouts:
        self.station_name = Label(text=f"[b]From 72nd St[/b]", markup=True, halign="left", font_size=40, size_hint=(.5, .5),
                             pos_hint={"center_x": .15, "center_y": .5})
        # debugging button
        #self.btn = Button(text="Refresh", background_color=[1,0,1,1], on_press=self.update)

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

        #self.add_widget(self.btn)
        Clock.schedule_interval(self.update, 30) # creates a clock that calls update function every 30 secs


    # this function is able to update the text and images in the widgets
    def update(self, event):
        new_train_num, new_dire, new_time_label = self.train_dir_time_list()

        # this counter is for the afternoon where the screen needs to alternate between uptown/downtown
        if self.count < 100:
            self.count += 1
        else:
            self.count = 1

        #updates the widget text and images to the new strings retrieved from train_dir_time_list()
        for i in range(0, len(new_train_num)):
            self.train_num[i].source = new_train_num[i].source
            self.dire[i].text = new_dire[i].text
            self.time_label[i].text = new_time_label[i].text




    def get_trains(self):
        # this function runs the mta_times.py functions and returns their result
        return mta_times.get_train(self.directions)

    def train_dir_time_list(self):
        # this function creates 3 lists in the same order to add to the main boxlayout


        # this conditonal statement has uptown trains only showing in the morning, but alternate betweeen uptown and downtown trains in the afternoon
        if 0 < int(str(datetime.now().time())[0:2]) <= 12:
            self.directions = self.dir_options[0]
        #else:
            #self.directions = self.dir_options[1] # this makes it static downtown in the afternoon
        elif self.count % 2 == 0:
            self.directions = self.dir_options[0]
        else:
            self.directions = self.dir_options[1]

        # a list of image objects, train_num / a list of direction label objects / a list of time label objects
        self.trains_list, self.times_list, = self.get_trains()
        train_num = []
        dir = []
        time_label = []

        # the for loop below creates the widgets in the proper order and applies the proper labels and image
        for i in range(0, len(self.trains_list)):

            if self.directions == self.dir_options[0]:

                direction = Label(text="Uptown", size_hint=(.5, .5), halign="left", font_size=20,
                              pos_hint={"center_x": .1, "center_y": .5})
                dir.append(direction)
            elif self.directions == self.dir_options[1]:
                direction = Label(text="Downtown", size_hint=(.5, .5), halign="left", font_size=20,
                              pos_hint={"center_x": .1, "center_y": .5})
                dir.append(direction)

            #conditional statements put the correct train number image object into list
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
    #Window.fullscreen = 'auto' # uncommend for fullscreen mode
    #Window.show_cursor = False
    gui().run()