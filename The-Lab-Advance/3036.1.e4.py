"""
Learning Objectives:
- this step is leading towards use of boolean in the next step
"""
# enter number
num = input("Input positive integer: ")
num = int(num)

# loop and display num div by 3 and not by 5
for i in range(0, num+1, 1):
		if i % 3 == 0 and i % 5 != 0:
				print(i)
