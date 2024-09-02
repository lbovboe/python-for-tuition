"""
Learning Objectives:
- using loop to draw shape
"""
import turtle

# create a screen
screen = turtle.Screen()

# create pen
pen = turtle.Turtle()

# draw triangle
for i in range(3):
		pen.forward(100)
		pen.left(120)