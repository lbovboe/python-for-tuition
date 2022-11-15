while True:
    values = input("Enter a word and a number: ").split()
    if values[0] == 'happy':
        if int(values[1]) == 8:
            print('match')
        else:
            print('Close match')
    else:
        if values[0] == 'end':
            break

