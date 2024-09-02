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

# loop to add total of all values < 5.
total = 0
for i in range(5):
		if nums[i] < 5:
				total += nums[i]

# display total
print("Total:", total)