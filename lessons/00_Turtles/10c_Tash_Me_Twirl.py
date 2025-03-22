
""" Tash Me with a Twirl
 
Update your Tash Me Click program ( copy your old program here )
so the moustache will twirl when you click on it. 

Hint: See 08a_More Turtle Programs, section 'Click on the Turtle'
"""

... # Your code here

import turtle
def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle and set its shape to the custom GIF
t = turtle.Turtle()
t.penup
set_turtle_image(t, "moustache2.gif")

def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""

    from pathlib import Path
    from PIL import Image


    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

# Set up the screen


turtle.setup(width=600, height=600)     # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina
tina.penup
screen = turtle.Screen()                # Get the screen that tina is on
set_background_image(screen, "emoji.png") # Set the background image of the screen

def screen_clicked(x, y):
    """Print the x and y coordinates of the screen when clicked.
    and make the turtle move to the clicked location."""

    print('You pressed: x=' + str(x) + ', y=' + str(y))

    t.goto(x, y)
  
screen.onclick(screen_clicked) # Important! Tell Python which function to use when the screen is clicked

turtle.done() # Important! Use `done` not `exitonclick` to keep the window open
