"""
Learning Objectives:
- Deleting from list
"""
import random

# create a list of random numbers and display
nums = [random.randint(20, 30) for i in range(6)]
print(nums)

# enter index
idx = input("Remove index: ")
idx = int(idx)

# delete value at index from list and display results
removed = nums.pop(idx)
print(removed)
print(nums)