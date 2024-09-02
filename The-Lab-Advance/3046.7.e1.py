"""
Learning Objectives:
- drawing center lines with respect to window size for positioning
"""
import turtle


def draw(screen, pen):

		# Note that in replit, the default screen size is 2000 x 2000 pixels.
		# The viewable size is about quarter of it.
		# Hence, the cursor will move out of screen when going towards the edge.
		# It will take some time for the cursor to travel at the default speed.
		# (this can be rectified by setting pen speed to 0 or set to smaller window size)

		# determine screen size
		w = screen.window_width()
		h = screen.window_height()

		# draw vertical line.
		# it will still work with float division h/2 but good to use whole number for pixels
		pen.penup()
		pen.goto(0, h//2)
		pen.pendown()
		pen.goto(0, -h//2)

		# draw horizontal line.
		# it will still work with float division w/2 but good to use whole number for pixels
		pen.penup()
		pen.goto(-w//2, 0)
		pen.pendown()
		pen.goto(w//2, 0)

		# draw circle center
		pen.penup()
		pen.goto(0, -120)
		pen.pendown()
		pen.circle(120)


# main ###########################################

# create a screen and pen
screen = turtle.Screen()
pen = turtle.Turtle()

# call function
draw(screen, pen)
