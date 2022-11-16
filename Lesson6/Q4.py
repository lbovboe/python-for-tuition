
names_list = ['Paul','Ethan','Jolie']

while True:
    name = input('Enter a name: ').capitalize()
    
    for i in range(len(names_list)):
        if names_list[i] == name:
            print(i)
    if name not in names_list:
        print('Not found key in again')