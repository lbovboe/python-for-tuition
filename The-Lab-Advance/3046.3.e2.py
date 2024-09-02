"""
Learning Objectives:
- how to check a current screen size
- draw center lines to visualise the coordinates
"""
import turtle

# create a screen
screen = turtle.Screen()

# determine screen size
w = screen.window_width()
h = screen.window_height()

# create pen
pen = turtle.Turtle()

# vertical center line
# note that coordinates can be floats
pen.penup()
pen.goto(0, h / 2)
pen.pendown()
pen.goto(0, -h / 2)

# horizontal center line
# note that coordinates can be floats
pen.penup()
pen.goto(-w / 2, 0)
pen.pendown()
pen.goto(w / 2, 0)