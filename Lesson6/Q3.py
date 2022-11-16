
string_number = input('Enter a 3 digit number : ')

# convert to list of digits
number_list = list(string_number) # note now they are still string inside the list

# convert each individual value to integer
number_list = list(map(int, number_list))
print(number_list)

total = sum(number_list)
print('The total is :',total)
