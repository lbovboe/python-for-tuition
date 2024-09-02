"""
Learning Objectives:
- Creating list with random values
- Access specific item in list
"""
import random

# students may use other methods to create the list but must use the random generator.
nums = [random.randint(1, 100) for i in range(10)]

# display list
print(nums)

# enter index adn display value
idx = input("Input index 0 to 9: ")
idx = int(idx)
print(nums[idx])