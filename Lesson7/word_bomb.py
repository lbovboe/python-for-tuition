import random 

number_players = int(input('Enter the number of players : '))
player_list = [ i+1 for i in range(number_players)]
print(player_list)
guess_list = []

for i in range(len(player_list)):
    guess_number = input('Player '+str(player_list[i])+' enter a number : ')
    if guess_number not in guess_list:
        guess_list.append(guess_number)
    else:
        print('BOOMMM! You Lost !')
        print('This number already exists.')
        print('Player',player_list[i],'is out')
    
