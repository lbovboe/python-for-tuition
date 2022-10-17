loop = int(input("Enter Number: "))
store ='' #--> for storing different words
for i in range(loop):
    word = input("Enter Input "+str(i+1)+" :")
    store += word + " " #--> same as store = store + word + " "

print("Ans: ",store)