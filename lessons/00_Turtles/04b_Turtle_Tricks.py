"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast.

tina.pencolor('purple')                  # Set the pen color to blue
tina.forward(20)                       # Move tina forward by the forward distance
tina.left (70)

tina.forward(20)                       # Move tina forward by the forward distance
tina.left(70)

tina.forward(20)                       # Move tina forward by the forward distance
tina.left (70)

tina.forward(20)                       # Move tina forward by the forward distance
tina.left(70)

tina.forward(20)                      # Move tina forward by the forward distance

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()


... # Your code here

turtle.exitonclick()                    # Close the window when we click on it
