"""
Learning Objectives:
- Familiarise with moving cursor to different positions fom input to draw line
"""

import turtle

# Create a graphical window
myscreen = turtle.Screen()

# Create a pen
mypen = turtle.Turtle()

# enter pointA
pointA = input("Point A: ")
pointAx, pointAy = pointA.split(",")
pointAx = int(pointAx)
pointAy = int(pointAy)

# enter pointB
pointB = input("Point B: ")
pointBx, pointBy = pointB.split(",")
pointBx = int(pointBx)
pointBy = int(pointBy)

# Draw a line from (-150,-100) to (150,100)
mypen.penup()
mypen.goto(pointAx, pointAy)
mypen.pendown()
mypen.goto(pointBx, pointBy)