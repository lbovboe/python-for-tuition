"""
Learning Objectives:
- Using an existing sample, explore how turtle is setup for drawing
"""
import turtle

# Create a graphical window
myscreen = turtle.Screen()
myscreen.bgcolor("blanched almond")

# Create a pen
mypen = turtle.Turtle()

# Draw something
mypen.forward(150)
mypen.left(90)
mypen.forward(100)
mypen.right(90)
mypen.backward(200)
mypen.circle(50)