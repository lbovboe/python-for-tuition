"""
Learning Objectives:
- using loop to draw shape
"""
import turtle

# create a screen
screen = turtle.Screen()

# create pen
pen = turtle.Turtle()

# draw square
for i in range(4):
		pen.forward(100)
		pen.left(90)