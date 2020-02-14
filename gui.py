import kivy
kivy.require('1.11.1')

import random

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class gui(App):

    def build(self):
        #return Label(text = "hello world",size_hint=(.5,.5),pos_hint={"center_x": .6, "center_y": .5})

        #img = Image(source = 'C:/Users/Kiril/PycharmProjects/MTA_pi/1.svg.png', size_hint=(.5, .5), pos_hint={"center_x":.5, "center_y": .5})
        #return img

        layout = BoxLayout(padding = 10, orientation = "vertical")
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(text = "Button #%s" % (i+1),
            background_color= random.choice(colors))
            layout.add_widget(btn)
        return layout




if __name__ == '__main__':
    gui().run()