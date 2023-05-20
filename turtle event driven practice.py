# Welcome to the event-driven practice
# File: turtle event driven practice.py
# Author: Darling
#
'''
Summary:
    Short and simple event driven programming with turtle focusing on key bindings.
'''

import turtle
import random

turtle.setup(400,500) # Determine the window size
wn = turtle.Screen() # Get a reference to the window
wn.title("Handling keypresses!") # Change the window title
wn.bgcolor("lightgreen") # Set the background color
tess = turtle.Turtle() # Create our favorite turtle

# The next four functions are our "event handlers for navigation.
def h1():
    tess.forward(30)

def h2():
    tess.left(45)

def h3():
    tess.right(45)

def h4():
    wn.bye() # Close down the turtle window

#setting colors red,bude,green
def red():#setting colors
    tess.color("Red")
def blue():
    tess.color("Blue")
def green():
    tess.color("Green")

#setting customization for increasing or decreasing pen width between sizes 0-20 inclusive
def increase():
    num = tess.width()
    if tess.width()<= 20:
        tess.width(num+1)

def decrease():
    num = tess.width()
    if tess.width() >= 0:
        tess.width(num-1)

#setting customization for random pen shapes
def shape():
    shapes = ["turtle","square","triangle","circle","arrow"]
    tess.shape(random.choice(shapes))

def message():
    tess.write("PYTHON ROCKS!!!")

# These lines "wire up" keypresses to the handlers we’ve defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(red,"r")
wn.onkey(blue,"b")
wn.onkey(green,"g")
wn.onkey(increase, "+")
wn.onkey(decrease, "-")
wn.onkey(shape,"s")
wn.onkey(message,"m")

# Now we need to tell the window to start listening for events,
# If any of the keys that we’re monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()
