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


class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        #self.add_widget(Ellipse(text = "hi")) #size_hint=(.5,.5),pos_hint={'center_x':.5, 'center_y':.5}))

###need to figure out way for times to update

class gui(App):

    def build(self):

        colors = [red, green, blue, purple]
        trains_list, times_list, = self.get_trains()
        print(times_list)
        print(trains_list)
        #direction = Label(text = "Uptown", size_hint=(.5,.5),halign = "left", font_size=30,pos_hint={"center_x": .1, "center_y": .5})

        #img = Image(source = 'C:/Users/Kiril/PycharmProjects/MTA_pi/1_train.png', size_hint=(.5, .5), pos_hint={"center_x":.5, "center_y": .5})

        #time = Label(text="X Mins",halign = "right", font_size = 40, size_hint=(.5, .5), pos_hint={"center_x": .9, "center_y": .5})


        #this creates the overall gui layout, which is a vertical box (meaning boxes are inserted horizontally stacked vertically)
        main_layout = BoxLayout(padding = 10, orientation = "vertical")

        station_name = Label(text=f"[b]From 72nd St[/b]", markup=True, halign="left", font_size=40, size_hint=(.5, .5), pos_hint={"center_x": .15, "center_y": .5})
        main_layout.add_widget(station_name)
        #debugging button
        btn = Button(text = "Refresh", background_color= random.choice(colors))

        for i in range(0, len(trains_list)):
            h_layout = BoxLayout(padding=1)

            direction = Label(text="Uptown", size_hint=(.5, .5), halign="left", font_size=20,
                              pos_hint={"center_x": .1, "center_y": .5})
            #conditional statements put the train label picture onto
            if trains_list[i] == '1':
                img = Image(source = 'C:/Users/Kiril/PycharmProjects/MTA_pi/1_train.png', size_hint=(.7, .7), pos_hint={"center_x":.5, "center_y": .5})
                h_layout.add_widget(img)
            elif trains_list[i] == '2':
                img = Image(source='C:/Users/Kiril/PycharmProjects/MTA_pi/2_train.png', size_hint=(.7, .7),
                            pos_hint={"center_x": .5, "center_y": .5})
                h_layout.add_widget(img)
            else:
                img = Image(source='C:/Users/Kiril/PycharmProjects/MTA_pi/3_train.png', size_hint=(.7, .7),
                            pos_hint={"center_x": .5, "center_y": .5})
                h_layout.add_widget(img)

            h_layout.add_widget(direction)

            train_time = times_list[i]
            time = Label(text=f"{train_time} Mins", halign="right", font_size=40, size_hint=(.5, .5),
                         pos_hint={"center_x": .9, "center_y": .5})
            h_layout.add_widget(time)

            main_layout.add_widget(h_layout)

        #h_layout.add_widget(img)
        #h_layout.add_widget(direction)
        #h_layout.add_widget(time)


        btn.bind(on_press=self.on_button_press)
        main_layout.add_widget(btn)
        #Clock.schedule_interval(self.update,1)




        return main_layout

    def on_button_press(self, instance):
        #current = self.solution.text
        button_text = instance.text


        if button_text == "Refresh":
            print("Button Pressed")
            self.build()


    def _update_rect(self, instance, value):
        self.circle.pos = instance.pos
        self.circle.size = instance.size

    def get_trains(self):
        return mta_times.get_train("72nd North")





if __name__ == '__main__':
    gui().run()