"""
Learning Objectives:
- Creating list of random numbers
- Familiarizing between index and value
- Checking through individual values and perform comparison
"""
import random

# Create list and display.
# Students may use any method.
nums = [random.randint(1, 10) for i in range(5)]
print(nums)

# set variables to first value
smallest = nums[0]
biggest = nums[0]
# loop to add total of all values < 5.
for i in range(1, 5):
		# save the smaller number
		if smallest > nums[i]:
				smallest = nums[i]
		# save the bigger number
		if biggest < nums[i]:
				biggest = nums[i]

# display total
print("Smallest:", smallest)
print("Biggest:", biggest)