"""
Learning Objectives:
- Creating list with random values
"""
import random

# students may use other methods to create the list but must use the random generator.
nums = [random.randint(1, 100) for i in range(10)]
print(nums)