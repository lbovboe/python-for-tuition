"""
Learning Objectives:
- drawing grid with respect to window size for positioning
- guide students on calculations and implement the function in parts if they are stuck
"""
import turtle


def draw_grid(screen, pen):

		# the function will draw in parts:
		#   left half and right half in a loop
		#   top half and bottom half in a loop
		#   center lines (do last or it may be covered by the light gray grid lines

		# determine screen size
		w = screen.window_width()
		h = screen.window_height()

		# draw vertical grid lines ######################
		pen.color("LightGray")
		interval = 35
		# half the width div by interval = num of lines needed on one side
		num_of_lines = round((w/2)/interval)
		for x in range(num_of_lines):
				# draw right side
				pen.penup()
				pen.goto(x*interval, h//2)
				pen.pendown()
				pen.goto(x*interval, -h//2)
				# draw left side
				pen.penup()
				pen.goto(-x*interval, h//2)
				pen.pendown()
				pen.goto(-x*interval, -h//2)

		# draw horizontal grid lines ######################
		# half the height div by interval = num of lines needed on top/bottom
		num_of_lines = round((h/2)/interval)
		for y in range(num_of_lines):
				# draw top side
				pen.penup()
				pen.goto(w//2, y*interval)
				pen.pendown()
				pen.goto(-w//2, y*interval)
				# draw bottom
				pen.penup()
				pen.goto(w//2, -y*interval)
				pen.pendown()
				pen.goto(-w//2, -y*interval)

		# draw center lines ######################
		pen.color("gray")
		# draw center vertical line
		pen.penup()
		pen.goto(0, h/2)
		pen.pendown()
		pen.goto(0, -h/2)

		# draw center vertical line
		pen.penup()
		pen.goto(-w/2, 0)
		pen.pendown()
		pen.goto(w/2, 0)

# main ###########################################

# create screen
screen = turtle.Screen()

# create pen
pen = turtle.Turtle()
pen.speed(0)

# call function
draw_grid(screen, pen)