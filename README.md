# Introduction

This is a program, written in python, that reads the NYC MTA realtime feed API for subway data and displays that information graphically, utilizing the Kivy Python Framework.

Kivy was chosen due to its portability amongst different operating systems without changing it's code.

It was created as an exercise to learn and get familiar with APIs as well as learning a gui framework. While also being a very helpful tool for me when I'm getting ready to leave the apartment. This is the reason it is hardcoded to show data from a specific train station and trains.


![Screenshot of program](https://raw.githubusercontent.com/skirillex/MTA_pi/master/screenshot_of_program.jpg?token=AHQWLHUUPJ7N7XKSUTMZGWC6LXLUM)

![Running on Raspberry Pi](https://raw.githubusercontent.com/skirillex/MTA_pi/master/running_on_raspberry_pi.jpg?token=AHQWLHWW26ETN5Z3YM4QAR26LXLLU)

# Requirements

This program relies on the following packages:
* Python3
* Python language bindings for GTFS
* protobuf3-to-dict
* Kivy 1.11.1

here's some common ways to install the dependencies:

```
python3 -m pip install --upgrade gtfs-realtime-bindings
python3 -m pip install protobuf3_to_dict
```
for Kivy:
```
python3 -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*
python3 -m pip install kivy==1.11.1
```

More detailed Kivy instructions based on operating system:
* [Kivy for windows](https://kivy.org/doc/stable/installation/installation-windows.html#kivy-dependencies)
* [Kivy on Raspberry Pi / Rasbian](https://kivy.org/doc/stable/installation/installation-rpi.html)
* [Kivy on Linux](https://kivy.org/doc/stable/installation/installation-linux.html)

This also requires access to the MTA live Feed via an API: [https://datamine.mta.info/user/register]



# Program Behavior

This program obtains data from the MTA API in the form of a dictionary with nested lists and dictionaries.
the feed contains downtown and uptown trains predicted arrival times at their respective stops. This feed corresponds to the 1,2,3,4 and 5 trains.

in mta_times.py the get_train() function takes an argument of which station it will return the next 4 trains for. That argument is set by guiAPP.py

After mta_times.py is run, it's get_train() function will return two lists. one for trains, and the other for times. The index of the trains list corresponds to the same index of the times list.


the guiAPP.py is where Kivy works and controls the logic to make the program run as desired. 
in the class TrainGUi, a BoxLayout is set vertically and each box within it has another box layout set horizontally.
each section in each horizontal box layout contains the image for the train departing the station, the direction that train is going, and in how many minutes will it depart.

there is a clock object that calls the update() every 30 seconds, which in turn calls the mta_times.py function get_train() and gets a new list of trains and times. It does this by way of trains_dir_times_list().

trains_dir_times_list() contains addtional logic to create the functionality of displaying uptown trains in the morning and alternating between uptown and downtown trains in the afternoon

