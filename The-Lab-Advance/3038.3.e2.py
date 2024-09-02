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

# loop to add total
total = 0
for i in range(5):
		total += nums[i]

# display total
print("Total:", total)