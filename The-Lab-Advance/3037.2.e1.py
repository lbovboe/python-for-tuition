"""
Learning Objectives:
- How to use sleep function to wait
- If student is stuck, guide step by step and
	watch him try different values to see if he understands
	what the function means
"""

import time

# note that need to cast input to float instead of integer
sec = input("Input seconds: ")
sec = float(sec)

print("wait")
time.sleep(sec)
print("done")