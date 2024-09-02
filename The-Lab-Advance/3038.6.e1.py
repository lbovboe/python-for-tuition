"""
Learning Objectives:
- Swapping list items in loop
- Students who can't do this usually didn't visualise that nums[i] and nums[i+1] are neighbours.
	Guide them to visualise the relation (like printing out nums[i] and nums[i+1]) before guiding them
	the solution.
"""
# create a list of random numbers and display
nums = [i for i in range(10)]
print(nums)

# loop till second last value so that i+1 is within range
for i in range(0, 9, 1):
		# swap
		temp = nums[i]
		nums[i] = nums[i+1]
		nums[i+1] = temp

		# display result
		print(nums)