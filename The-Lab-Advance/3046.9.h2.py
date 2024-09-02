"""
Learning Objectives:
- Using Turtle graphics to visualise collision boundary
- If students are stuck, guide in steps to implement navigate()
"""
import turtle
import random


def navigate(pen):

		# draw outer boundary box
		pen.color("white", "yellow")
		pen.penup()
		pen.goto(-200, 100)
		pen.pendown()
		pen.begin_fill()
		pen.goto(-200, -100)
		pen.goto(200, -100)
		pen.goto(200, 100)
		pen.goto(-200, 100)
		pen.end_fill()

		# set outer box boundary limits
		outer_left = -200 + 20
		outer_right = 200 - 20
		outer_top = 100 - 20
		outer_bottom = -100 + 20

		# enter box
		inner_box = input("Enter center of a box (x,y) with value between 0 to 200: ")
		x, y = inner_box.split(",")
		x = int(x)
		y = int(y)

		# draw inner boundary box
		pen.color("white", "white")
		pen.penup()
		pen.goto(x-25, y-25)
		pen.pendown()
		pen.begin_fill()
		for i in range(4):
				pen.forward(50)
				pen.left(90)
		pen.end_fill()

		# set inner box boundary limits
		inner_left = (x - 25) - 20
		inner_right = (x + 25) + 20
		inner_top = (y + 25) + 20
		inner_bottom = (y - 25) - 20

		# goto start position (-150,0)
		pen.penup()
		pen.goto(-150, 0)
		pen.pendown()

		# set pen speed and shape
		pen.speed(3)
		pen.shape("turtle")
		pen.color("green")

		# wander
		while True:

				# move forward
				pen.forward(20)

				# get new position
				penx, peny = pen.position()

				# students may combine all the conditions into a single if statement
				# but be aware of the use of brackets
				collided = False
				# check collision with outer boundary
				if (penx < outer_left or penx > outer_right) or (peny > outer_top or peny < outer_bottom):
						collided = True
				# check collision with inner boundary
				if (penx >= inner_left and penx <= inner_right and peny <= inner_top and peny >= inner_bottom):
						collided = True

				# reverse if collided
				if collided == True:
						# out of bound: reverse and turn randomly
						pen.backward(20)
						pen.left(random.randint(-140, 140))


# main ###########################################

# create a screen and pen
screen = turtle.Screen()
pen = turtle.Turtle()

# call function
navigate(pen)