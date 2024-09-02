"""
Learning Objectives:
- Learn how to develop running time sequence using running number to trigger reset
- If student is stuck:
		1. Implement input and casting
		2. Implement loop to keep increasing second
		3. Implement reset triggered by second, then minute
"""
import time

# input
mm, ss = input('Enter the start time (MM:SS): ').split(':')
mm = int(mm)
ss = int(ss)

while True:
		# output in MM:SS format and wait 1 sec
		print(str(mm).zfill(2) + ':' + str(ss).zfill(2))
		time.sleep(1)

		# increase sec
		ss += 1

		# below trigger also works without nesting the if statements
		# but reduces redundant checking with nested ifs

		# if sec hits 60, reset sec and increase min
		if ss == 60:
				ss = 0
				mm += 1
				# if min hits 60, reset min and increase hr
				if mm == 60:
						mm = 0


