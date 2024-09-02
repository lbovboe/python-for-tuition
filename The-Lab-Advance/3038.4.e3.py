"""
Learning Objectives:
- Appending list with condition from other values
"""
# input qty
num = input("Total students: ")
num = int(num)

# loop to append text to string list
names = []
for i in range(num):
		name = input("Input name " + str(i+1) + ": ")
		coin = input("Input coins: ")
		coin = int(coin)
		if coin >= 50:
				names.append(name)

# display list
print(names)