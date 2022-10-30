word_list = input("Enter ur scores for EL,CH,Math,Science respectively : ")
word_list = word_list.split()

# convert scores to float
for i in range(len(word_list)):
    word_list[i] = float(word_list[i])


total_AL_points = 0
AL_list =[]
for i in range(len(word_list)):
    if word_list[i] >= 90:
        total_AL_points += 1
        AL_list.append(1)
    elif word_list[i] >= 85:
        total_AL_points += 2
        AL_list.append(2)
    elif word_list[i] >= 80:
        total_AL_points += 3
        AL_list.append(3)
    elif word_list[i] >= 75:
        total_AL_points += 4
        AL_list.append(4)
    elif word_list[i] >= 65:
        total_AL_points += 5
        AL_list.append(5)
    elif word_list[i] >= 45:
        total_AL_points += 6
        AL_list.append(6)
    elif word_list[i] >= 20:
        total_AL_points += 7
        AL_list.append(7)
    else:
        total_AL_points += 8
        AL_list.append(8)
    
print("Your English is", AL_list[0])
print("Your Chinese is", AL_list[1])
print("Your Math is", AL_list[2])
print("Your Science is", AL_list[3])
print("Your total PSLE scores is",total_AL_points)