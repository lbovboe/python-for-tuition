"""
Learning Objectives:
- Appending list across different loops
- If students are stuck, guide to implement in order:
		inner loop to append students in one group
		add on outer loop to incorporate different groups
"""
# input qty
groups = input("Total groups: ")
groups = int(groups)

names = []
# repeat for each group
for i in range(groups):

		# loop for number of students in the next group
		students = input("Total students in group " + str(i+1) + ": ")
		students = int(students)
		for j in range(students):
				# get name and append name to list if coins >= 50
				name = input("Input name " + str(j+1) + ": ")
				coin = input("Input coins: ")
				coin = int(coin)
				if coin >= 50:
						names.append(name)

# display list
print(names)