"""
Learning Objectives:
- using variable as a boolean flag
- understanding how to use flag to determine something not done/found in a loop
"""
# enter number
num = input("Input 2 positive integers: ")
n1, n2 = num.split()
n1 = int(n1)
n2 = int(n2)

# loop and display num div by 3 and not by 5
found = False
for i in range(0, 101, 1):
		if i % n1 == 0 and i % n2 != 0:
				print(i)
				found = True

# if none is found, display "None"
if found == False:
		print("None")