"""
Learning Objectives:
- How to use loops to display running time from a start
- If student is stuck:
		1. Implement input and casting
		2. Implement loop to keep increasing second for 10 seconds
		3. Implement reset after every 60 seconds
"""
import time

# enter start second
sec = input('Enter the start second: ')
sec = int(sec)

# loop for 10 seconds
for i in range(10):

		# display in 2-digit format and wait a second
		print(str(sec).zfill(2))
		time.sleep(1)

		# increase sec
		sec = sec + 1

		# reset when hit 60
		if sec == 60:
				sec = 0


