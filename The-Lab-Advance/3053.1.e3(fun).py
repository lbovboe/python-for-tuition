"""
Learning Objectives:
- Project development
- Instructors can test but are not required to debug or guide
- If students are stuck, instructor can still choose to help (see comments in solution):
		1. Modify Field class:
				display()
"""
import replit, random, time


class Field:

		def __init__(self):

				# added for easy checking of Hunter meet Roamer
				self.H_meets_R = False

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

				# place R and H starting points
				self.field[0][0] = "R"
				self.field[9][19] = "H"

		def display(self):
				# clear screen on replit
				replit.clear()

				# display the field
				for r in range(10):
						for c in range(20):
								if self.field[r][c] == "R":
										print("🌞", end=' ')
								elif self.field[r][c] == "H":
										print("🌛", end=' ')
								elif self.field[r][c] == "X":
										print("🪐", end=' ')
								else:
										print("🌚", end=' ')
						print()

				# delay
				time.sleep(0.5)

		@ staticmethod
		def main():
				field = Field()
				roamer = Roamer(0, 0)
				hunter = Hunter(9, 19)
				field.display()

				while True:

						# roamer updates move
						roamer.navigate(field)

						# hunter updates move
						hunter.navigate(field)

						# display field
						field.display()

						# end if H meets R
						if field.H_meets_R:
								break


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


class Hunter(Roamer):

		def __init__(self, r, c):
				Roamer.__init__(self, r, c)

		# find neighbouring X or R and return position, else return -1,-1
		def neighbour(self, field):
				# UP: check if in range
				if self.row-1 >= 0:
						# instead of finding "X" or "R", check that it is not "."
						if field.field[self.row-1][self.col] != ".":
								return self.row-1, self.col

				# DOWN: check if in range
				if self.row+1 <= 9:
						# instead of finding "X" or "R", check that it is not "."
						if field.field[self.row+1][self.col] != ".":
								return self.row+1, self.col

				# LEFT: check if in range
				if self.col-1 >= 0:
						# instead of finding "X" or "R", check that it is not "."
						if field.field[self.row][self.col-1] != ".":
								return self.row, self.col-1

				# RIGHT: check if in range
				if self.col+1 <= 19:
						# instead of finding "X" or "R", check that it is not "."
						if field.field[self.row][self.col+1] != ".":
								return self.row, self.col+1

				# No neighbouring X or R
				return -1, -1

		# overrides navigate
		def navigate(self, field):

				# check if there is X or R, step on it
				r, c = self.neighbour(field)
				if r != -1:
						# if the neighbour is R, set flag to true
						if  field.field[r][c] == "R":
								field.H_meets_R = True

						# update field and poistion
						field.field[self.row][self.col] = "."
						field.field[r][c] = "H"
						self.row = r
						self.col = c

				# else navigate as per normal (like R)
				else:
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
												field.field[self.row-1][self.col] = "H"
												# update position
												self.row -= 1
												break

								# DOWN: check that move is within range
								elif self.direction == 2 and (self.row+1) <= 9:
										# check that it is not occupied by X
										if field.field[self.row+1][self.col] == ".":
												# update field
												field.field[self.row][self.col] = "."
												field.field[self.row+1][self.col] = "H"
												# update position
												self.row += 1
												break

								# LEFT: check that move is within range
								elif self.direction == 3 and (self.col-1) >= 0:
										# check that it is not occupied by X
										if field.field[self.row][self.col-1] == ".":
												# update field
												field.field[self.row][self.col] = "."
												field.field[self.row][self.col-1] = "H"
												# update position
												self.col -= 1
												break

								# RIGHT: check that move is within range
								elif (self.direction == 4) and ((self.col+1) <= 19):
										# update move
										if field.field[self.row][self.col+1] == ".":
												# update field
												field.field[self.row][self.col] = "."
												field.field[self.row][self.col+1] = "H"
												# update position
												self.col += 1
												break


# main #############################################################
Field.main()