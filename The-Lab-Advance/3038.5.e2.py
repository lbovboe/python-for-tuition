"""
Learning Objectives:
- Deleting from list using loop
"""
import random

# create a list of random numbers and display
nums = [random.randint(-5, 5) for i in range(8)]
print(nums)

# Use loop to remove both values.
# If students hardcode, ask them to use loop instead
for i in range(4):
		# pop the first and last value
		nums.pop(0)
		nums.pop(len(nums)-1)

		# display result
		print(nums)