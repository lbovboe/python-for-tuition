"""
Learning Objectives:
- for-loop: specifying range with variables (start, end, step)
- swapping to count up from small to big numbers
"""
# enter numbers
nums = input("Input 3 positive integers: ")
start, end, step = nums.split()
start = int(start)
end = int(end)
step = int(step)

# If student uses 2 loops, ask them to practise swapping instead
# as it will shorten subsequent steps.
# swap if start > end
if start > end:
		temp = start
		start = end
		end = temp

# run loop
for i in range(start, end + 1, step):
		print(i)