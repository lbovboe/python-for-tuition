"""
Learning Objectives:
- Learn about mutating adjacent cells in 2D list.
	This step will start with 1D list.
- When students are stuck, follow the steps in the solution in the order
		main
		display()
		spread()
"""


# function to display in the format:
# Day N: X X X X X
def display(space, day):
		print("Day " + str(day) + ":", *space)


# function to spread to neighbour
def spread(space, day):

		# it is acceptable that student use loops to search instead
		# below shows a simpler method

		# check for valid index of a left neighbour
		if (position-day) >= 0:
				# set to 1 if it is a 0
				space[position-day] = 1

		# check for valid index of a right neighbour
		if (position+day) < size:
				# set to 1 if it is a 0
				space[position + day] = 1


# main #######################################

# enter size and position
size = input("Enter space size: ")
size = int(size)
position = input("Enter cell position: ")
position = int(position)

# create space list and set position to 1
space = [0 for i in range(size)]
space[position] = 1

# starts from Day 0
day = 0
display(space, day)

# loop until both ends are 1
while space[0] == 0 or space[size-1] == 0:
		day = day + 1
		spread(space, day)
		display(space, day)

# display days
print("Total", day, "days")