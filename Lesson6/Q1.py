# Checking for duplications

# generate 4 random number using short way

import random 

random_list = [ random.randint(0,10) for i in range(4)]
print(random_list)
for i in range(4):
    c = 0
    for j in range(4):
        if random_list[i] == random_list[j]:
            c +=1
    if c>1:
        print('duplicate is found')
        break
 
if c <= 1:
    print('No duplicate found')

