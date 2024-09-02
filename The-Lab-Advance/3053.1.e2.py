"""
Learning Objectives:
- Project development
- Instructors can test but are not required to debug or guide
- If students are stuck, instructor can still choose to help (see comments in solution):
		1. Implement Roamer class
				__init__()
				navigate()
		2. Modify Field class
				__init__(): set field[0][0] to R
				main(): add Roamer and navigate

"""
import replit, random, time


class Field:

		def __init__(self):

				# create field with default "."
				self.field = [["." for c in range(20)] for r in range(10)]

				# counter to keep track of the number of X on the field.
				# this variable is not specified in the question to allow
				# student an option to do otherwise.
				self.x_counter = 0

				# place 40 random "X"
				while self.x_counter < 40:
						# index range to to avoid the edges
						r = random.randint(1, 8)
						c = random.randint(1, 18)
						# check that it is not already an X
						if self.field[r][c] != "X":
								self.field[r][c] = "X"
								self.x_counter += 1

				# place R starting points
				self.field[0][0] = "R"

		def display(self):
				# clear screen on replit
				replit.clear()

				# display the field
				for r in range(10):
						print(*self.field[r], end='')
						print()

				# delay
				time.sleep(0.5)

		@ staticmethod
		def main():
				field = Field()
				roamer = Roamer(0, 0)
				field.display()

				while True:

						# roamer updates move
						roamer.navigate(field)

						# display field
						field.display()


class Roamer:

		def __init__(self, r, c):
				# initialise variables
				self.row = r
				self.col = c
				self.direction = 1

		def navigate(self, field):

				# repeat until a move is made
				while True:

						# 20% (2 out of 10) chance to regenerate new direction
						# 1 - up / 2 - down / 3 - left / 4 -right
						if random.randint(1, 10) <= 2:
								# loop until new direction is set.
								# it should not be the same as last direction.
								while True:
										new_direction = random.randint(1, 4)
										if new_direction != self.direction:
												self.direction = new_direction
												break

						# UP: check that move is within range
						if self.direction == 1 and (self.row-1) >= 0:
								# check that it is not occupied by X
								if field.field[self.row-1][self.col] == ".":
										# update field
										field.field[self.row][self.col] = "."
										field.field[self.row-1][self.col] = "R"
										# update position
										self.row -= 1
										break

						# DOWN: check that move is within range
						elif self.direction == 2 and (self.row+1) <= 9:
								# check that it is not occupied by X
								if field.field[self.row+1][self.col] == ".":
										# update field
										field.field[self.row][self.col] = "."
										field.field[self.row+1][self.col] = "R"
										# update position
										self.row += 1
										break

						# LEFT: check that move is within range
						elif self.direction == 3 and (self.col-1) >= 0:
								# check that it is not occupied by X
								if field.field[self.row][self.col-1] == ".":
										# update field
										field.field[self.row][self.col] = "."
										field.field[self.row][self.col-1] = "R"
										# update position
										self.col -= 1
										break

						# RIGHT: check that move is within range
						elif (self.direction == 4) and ((self.col+1) <= 19):
								# update move
								if field.field[self.row][self.col+1] == ".":
										# update field
										field.field[self.row][self.col] = "."
										field.field[self.row][self.col+1] = "R"
										# update position
										self.col += 1
										break


# main #############################################################
Field.main()
