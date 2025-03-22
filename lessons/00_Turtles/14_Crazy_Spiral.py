"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""

import random
import turtle


# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["red", "blue", "green", "yellow", "orange"]


def getNextColor(i):
    return colors[i % len(colors)]

turtle.setup (width=600, height=600) 
window = turtle.Screen()

baseSize = 200  # the size of the black part of the star
flameSize = 130  # the length of the flaming arms

t = turtle.Turtle() 

t.shape("turtle") 

t.width(2) 

t.speed(0) 

for i in range(40):
    t.pencolor(getRandomColor())

    t.fillcolor(getRandomColor()) 
   
    t.begin_fill()

    t.forward(30) 

    t.left(30) 

    t.forward(flameSize) 

    t.right(30) 

    t.forward(flameSize) 

    t.right(170) 

    t.forward(baseSize) 

    t.end_fill()

t.hideturtle() 

turtle.done() 
