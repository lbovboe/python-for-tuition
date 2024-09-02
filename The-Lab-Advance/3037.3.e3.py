"""
Learning Objectives:
- Running date and resetting
- Proper sequencing of updating, resetting and display
- If students are stuck, guide to do in order:
		1. increment of day and display
		2. reset at end of Jan
		3. break at 2 Feb
"""
import time


# input date
d = input("Input a day in Jan (1-31): ")
d = int(d)

# loop to run date till 2 Feb
m = "Jan"
while True:
		# increase day
		d += 1

		# check if end of Jan is reached
		if d == 32:
				d = 1
				m = "Feb"

		# display date
		print(d, m)
		time.sleep(1)

		# break if reach 2 Feb
		if d == 2 and m == "Feb":
				break