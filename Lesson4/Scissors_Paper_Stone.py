import random
print('Select 1 to play with AI')
print('Select 2 to player to another player')

choice = ['scissors', 'paper','stone']
AI_score =0
Player1_score =0
Player2_score =0


game_mode = int(input('Input the game mode you want to play: '))

if game_mode == 1:
    while True:
        AI_choice = random.randint(0,2)
        AI_choice_value = choice[AI_choice]
        play_choice_value = input('Enter your choice scissors/paper/stone : ').lower()

        if play_choice_value not in choice:
            print('Please enter a valid choice!')
        else:
            if play_choice_value == 'scissors' and AI_choice_value == 'paper':
                print('You won!')
            elif play_choice_value == 'paper' and AI_choice_value == 'stone':
                print('You won!')
            elif play_choice_value == 'stone' and AI_choice_value == 'scissors':
                print('you won!')
            else:
                print('You Lost!')

        decision = input('Do you wanna continue? (y/n):')
        if decision == 'n':
            print('The final score AI :',AI_score)
            print('The final score Player:',Player1_score)
            if AI_score > Player1_score:
                print('The final winner is AI !')
            elif AI_score < Player1_score:
                print('The final winner is Player!')
            else:
                print('It is a draw!')
            break

    






