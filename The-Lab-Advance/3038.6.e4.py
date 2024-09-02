"""
Learning Objectives:
- Learning a sorting algorithm
- The solution is similar to previous step.
	Only additions are repeating len-1 times and setting inner end range to 4-j.
"""
import random

# create a list of random numbers and display
nums = [random.randint(1, 100) for i in range(5)]
print(nums)

# loop len(nums)-1 times
for j in range(4):
		# Loop till second last value so that i+1 is within range.
		# Note that the end range is 4-j because as the biggest numbers get in position
		# each round, you do not need to check it anymore.
		# This significantly reduces the number of computations in large lists
		for i in range(0, 4-j, 1):
				# swap if value is more than neighbour
				if nums[i] > nums[i+1]:
						temp = nums[i]
						nums[i] = nums[i+1]
						nums[i+1] = temp

				# display result
				print(nums)

		# display blank line
		# this is optional, just to separate each round of sorting
		# to let student see the iterations are reduced each round
		# due to "4-j" in the inner range
		print()