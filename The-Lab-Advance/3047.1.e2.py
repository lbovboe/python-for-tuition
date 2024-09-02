"""
Learning Objectives:
- Project development
- Instructors can test but are not required to debug or guide
- If students are stuck, instructor can still choose to help (see comments in solution):
		1. main()
				create board variable
				loop to play
"""
import turtle


# draw board
def draw_board(pen):
		# draw board
		pen.color("BlanchedAlmond")
		pen.pensize(1)
		pen.penup()
		pen.goto(-120, 140)
		pen.pendown()
		pen.begin_fill()
		pen.goto(120, 140)
		pen.goto(120, -100)
		pen.goto(-120, -100)
		pen.goto(-120, 140)
		pen.end_fill()

		# draw grid
		pen.pensize(4)
		pen.color("white")
		# horizontal lines
		pen.penup()
		pen.goto(-120, 60)
		pen.pendown()
		pen.goto(120, 60)
		pen.penup()
		pen.goto(-120, -20)
		pen.pendown()
		pen.goto(120, -20)
		# vertical lines
		pen.penup()
		pen.goto(-40, 140)
		pen.pendown()
		pen.goto(-40, -100)
		pen.penup()
		pen.goto(40, 140)
		pen.pendown()
		pen.goto(40, -100)

		# draw cell numbers
		pen.penup()
		pen.color("grey")
		style = ('Courier', 12, 'bold')
		# students can use manual method to label the cell.
		# below shows quick method using % and //
		for i in range(9):
			pen.goto(-100+(i%3*80), 120-(i//3*80))
			pen.write(str(i+1), font=style, align='center')

		# draw legend
		pen.penup()
		pen.goto(0, -130)
		pen.color("black")
		style = ('Courier', 12, 'bold')
		pen.write("Player-1: X  Player-2: O", font=style, align='center')


# draw symbol at position
def draw_symbol(pen, position, symbol):
		# student can manually calculate the positions.
		# below shows quick method using % and //
		position = int(position) - 1
		row = -80 + (position%3 * 80)
		col = 80 - (position//3 * 80)

		pen.penup()
		pen.goto(row, col)
		pen.color("black")
		style = ('Arial', 40, 'bold')
		pen.write(symbol, font=style, align='center')


##########################################################
#                main program                            #
##########################################################
# set screen
screen = turtle.Screen()
screen.setup(400, 400)
screen.bgcolor("white")

# set turtle
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# draw empty board
draw_board(pen)

# create board to store symbols.
# suggested to use 1D or 2D list.
# if students use 9 variables,
# may accept but tell him/her will get very low score
# as there will be a lot of manual steps
board = ["" for i in range(9)]

# Alternate player to fill the board
for i in range(9):

		# set player and symbol (alternate even/odd)
		if i%2 == 0:
				player = 1
				symbol = "X"
		else:
				player = 2
				symbol = "O"

		# loop until valid position is entered
		while True:
				try:
						# enter position 1-9
						position = input("Player-"+str(player)+" (1-9): ")
						position = int(position)
						# check range
						if position >= 1 and position <= 9:
								# update board if emtpy
								if board[position-1] == "":
										board[position-1] = symbol
										break
						# out of range or position occupied
						print("invalid entry")
				except:
						# non integer entered
						print("invalid entry")

		# draw symbol
		draw_symbol(pen, position, symbol)
