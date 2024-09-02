"""
Learning Objectives:
- How to use loops to display running time
- If student is stuck:
		1. Implement loop to keep increasing second
		2. Implement reset after every 60 seconds
"""
import time

# start second at 0
sec = 0

# loop forever
while True:

		# display in 2-digit format and wait a second
		print(str(sec).zfill(2))
		time.sleep(1)

		# increase sec
		sec = sec + 1

		# reset when hit 60
		if sec == 60:
				sec = 0


