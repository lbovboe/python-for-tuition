"""
Learning Objectives:
- Swapping list items in loop based on condition
- Students who can't do this usually didn't visualise that nums[i] and nums[i+1] are neighbours.
	Guide them to visualise the relation (like printing out nums[i] and nums[i+1]) before guiding them
	the solution.
- The inner loop is done in previous step
"""
import random

# create a list of random numbers and display
nums = [random.randint(1, 10) for i in range(5)]
print(nums)

for j in range(2):
		# loop till second last value so that i+1 is within range
		for i in range(0, 4, 1):
				# swap if value is more than neighbour
				if nums[i] > nums[i+1]:
						temp = nums[i]
						nums[i] = nums[i+1]
						nums[i+1] = temp

				# display result
				print(nums)

		# display blank line
		print()