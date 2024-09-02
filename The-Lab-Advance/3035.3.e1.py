"""
Learning Objectives:
- for-loop: using loop to repeat certain number of times
"""
# enter integer
num = input("Input integer: ")
num = int(num)

# student may use other range, e.g. with start, end step
# but can remind them if it is only to repeat a number of
# times without the need to use the i, then a simpler way
# is as shown
for i in range(num):
		print("#")