"""
Learning Objectives:
- placing text
"""
import turtle


# main ###########################################

# create screen
screen = turtle.Screen()

# create pen
pen = turtle.Turtle()

# Top text
pen.penup()
pen.goto(0, 50)
pen.pendown()
pen.color("magenta")
style = ("Comic Sans MS", 30, "bold")
pen.write("Awesome Turtle!", font=style , align="center")

# Middle text
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.color("DarkTurquoise")
style = ("Monoton", 30, "bold")
pen.write("Awesome Turtle!", font=style , align="center")

# Bottom text
pen.penup()
pen.goto(0, -50)
pen.pendown()
pen.color("YellowGreen")
style = ("Calligraphr", 30, "bold")
pen.write("Awesome Turtle!", font=style , align="center")