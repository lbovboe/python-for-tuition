import random
number_list = [random.randint(1,10) for i in range(10)]
unique_list = []
duplicate_list = []

for i in number_list:
    if i not in unique_list:
        unique_list.append(i)
    else:
        duplicate_list.append(i)

print(number_list)
print(unique_list)
print(duplicate_list)
print(list(set(duplicate_list)))
