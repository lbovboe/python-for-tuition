"""
Learning Objectives:
- for-loop: specifying range with variables to count down and up
"""
# enter numbers
nums = input("Input 2 integers: ")
num1, num2 = nums.split()
num1 = int(num1)
num2 = int(num2)

# swap if num1 < num2
if num1 < num2:
		temp = num1
		num1 = num2
		num2 = temp

# count down
for i in range(num1, num2, -1):
		print(i)
# count up
for i in range(num2, num1 + 1, 1):
		print(i)