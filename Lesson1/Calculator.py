while True:
    print("Select operation from below :")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice = int(input("Enter choice(1/2/3/4): "))
    l = [1,2,3,4]
    ans = -1
    if choice not in l:
        continue
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == 1:
        print(num1,"+",num2,"=",num1+num2)
    elif choice == 2:
        print(num1,"-",num2,"=",num1-num2)
    elif choice == 3:
        print(num1,"*",num2,"=",num1*num2)
    elif choice == 4:
        print(num1,"/",num2,"=",num1/num2)

    
    while True :
        check = input("Let's do next calculation? (yes/no):").lower()
        if check == "no" or check == "yes":
            break
    if check == "no":
        break
