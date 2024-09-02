"""
Learning Objectives:
- Project development
- Instructors can test but are not required to debug or guide
- If students are stuck, instructor can still choose to help (see comments in solution):
		1. Implement Field class with display
				__init__()
				display()
				main()
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
				field.display()


# main #############################################################
Field.main()