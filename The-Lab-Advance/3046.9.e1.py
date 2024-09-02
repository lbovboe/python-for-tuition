"""
Learning Objectives:
- Using Turtle graphics to visualise collision boundary
- If students are stuck, guide in steps to implement navigate()
"""
import turtle
import random


def navigate(pen):

		# students are allowed to hard code the boundary size in the solution

		# box size
		w = 400
		h = 200

		# draw boundary box
		pen.penup()
		pen.goto(-w//2, h//2)
		pen.pendown()
		pen.goto(-w//2, -h//2)
		pen.goto(w//2, -h//2)
		pen.goto(w//2, h//2)
		pen.goto(-w//2, h//2)

		# goto center
		pen.penup()
		pen.goto(0, 0)
		pen.pendown()

		# set pen speed and shape
		pen.speed(3)
		pen.shape("turtle")

		# wander
		while True:

				# move forward
				pen.forward(20)

				# check: pen.x exceeds left / pen.x exceeds right / pen.y below bottom / pen.y above ceiling
				penx, peny = pen.position()
				if (penx < -w//2 or penx > w//2) or (peny < -h//2 or peny > h//2):
						# out of bound: reverse and turn randomly
						pen.backward(20)
						pen.left(random.randint(-140, 140))


# main ###########################################

# create a screen and pen
screen = turtle.Screen()
pen = turtle.Turtle()

# call function
navigate(pen)