import random
number_list = [ random.randint(1,100) for i in range(10)]
length = len(set(number_list))
if length != 10:
    print(' There is duplicate')
else:
    print(' There is no duplicate')