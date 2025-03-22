""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""





import turtle                           # Tell Python we want to work with the turtle
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

t = turtle.Turtle()

def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)
    

set_turtle_image(tina, "leaguebot_bolt.gif")
tina.turtlesize(stretch_wid=10, stretch_len=10)
for i in range(6):
    tina.forward(150)
    tina.left(60)


turtle.exitonclick()