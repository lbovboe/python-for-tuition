import random

# method 1
num_list = []
for i in range(5):
    num_list.append(random.randint(0, 10))
print(*num_list)

# method 2

num_list = [ random.randint(0, 10) for i in range(5)]
print(*num_list)