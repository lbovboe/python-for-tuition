"""
Learning Objectives:
- Running date and resetting
- Proper sequencing of updating, resetting and display
- If students are stuck, guide to do in order:
		1. increment of day and display
		2. reset at end of Feb
		3. break at 2 Mar
"""
import time


# input date
y = input("Input a year: ")
y = int(y)
d = input("Input a day in Feb (1-25): ")
d = int(d)

# loop to run date till 2 Feb
m = "Feb"
while True:
		# increase day
		d += 1

		# check if end of Feb is reached
		# leap year
		if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
				if d == 30:
						d = 1
						m = "Mar"
		# non-leap year
		else:
				if d == 29:
						d = 1
						m = "Mar"

		# display date
		print(d, m)
		time.sleep(1)

		# break if reach 2 Mar
		if d == 2 and m == "Mar":
				break