"""
Learning Objectives:
- learn how to develop running time sequence using running number to trigger reset
- If student is stuck:
		1. implement input and casting
		2. implement loop to keep increasing second
		3. implement reset triggered by second, then minute, then hour
"""
import time

# input
hh, mm, ss = input('Enter the start time (HH:MM:SS): ').split(':')
hh = int(hh)
mm = int(mm)
ss = int(ss)

while True:
		# output in HH:MM:SS format and wait 1 sec
		print(str(hh).zfill(2) + ':' + str(mm).zfill(2) + ':' + str(ss).zfill(2))
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
						hh += 1
						# if hr hits 24, reset hr
						if hh == 24:
								hh = 0

