"""
Learning Objectives:
- filling shapes
"""
import turtle


def fill_circle(pen):

		# set pen colour and size
		pen.pensize(6)

		# draw and fill circle
		pen.color("green", "yellow")
		pen.begin_fill()
		pen.circle(120)
		pen.end_fill()

		# draw and fill square
		pen.penup()
		pen.goto(100,-100)
		pen.pendown()
		pen.color("purple", "pink")
		pen.begin_fill()
		for i in range(4):
				pen.forward(120)
				pen.left(90)
		pen.end_fill()


# main ###########################################

# create a screen and pen
screen = turtle.Screen()
pen = turtle.Turtle()

# call function
fill_circle(pen)
