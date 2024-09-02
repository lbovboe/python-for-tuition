"""
Learning Objectives:
- Deleting from list using loop
"""
import random

# create a list of random numbers and display
nums = [random.randint(1, 10) for i in range(10)]
print(nums)

# Use loop to remove both values. Pop from the end to avoid index out of range.
# If students hardcode, ask them to use loop instead
for i in range(9, -1, -1):
		if nums[i] % 2 == 0:
				nums.pop(i)

# display result
print(nums)