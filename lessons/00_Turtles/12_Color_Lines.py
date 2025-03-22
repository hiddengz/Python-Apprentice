"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle
tina = turtle.Turtle()
tina.shape("turtle")

forward = 50
left = 90
colors = [ 'red', 'blue', 'black', 'orange']

for color in colors:
    tina.color(color)
    tina.forward(forward)
    tina.left(left)


# 2) Make another square, but put the colors in reverse order, using a negative index. 

import turtle
t = turtle.Turtle()
t.shape("turtle")

forward = 50
left = 90
colors = [ 'orange', 'black', 'blue', 'red']
t.penup
t.forward(60)
t.pendown
for color in colors:
    t.color(color)
    t.forward(forward)
    t.left(left) # Your code here

turtle.exitonclick()                     # Close the window when we click on it