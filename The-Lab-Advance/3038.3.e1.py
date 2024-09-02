"""
Learning Objectives:
- Creating list of random numbers
- Familiarizing between index and value
- Checking through individual values
"""
import random

# Create list and display.
# Students may use any method.
nums = [random.randint(1, 10) for i in range(5)]
print(nums)

# loop to display value < 5
for i in range(5):
		if nums[i] < 5:
				print(i)