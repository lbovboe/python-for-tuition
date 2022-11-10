while True:
    value = input("Enter a value : ")
    check_is_num = value.isdigit()
    if check_is_num == True:
        value = int(value)
        if value >= 10 :
            print('win')
        else:
            print('lost')
    else:
        if value == "end":
            break

