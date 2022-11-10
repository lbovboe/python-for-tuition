import random
print('Select Mode 1 to play against AI')
print('Select Mode 2 to play against Player')
mode = int(input('Enter Game Mode 1/2: '))

AI_options = ['scissors','paper','stone']
AI_score = 0
Player_score = 0  
Player2_score = 0
if mode == 1:
    while True:
        AI_option = random.randint(0,2)
        AI_value = AI_options[AI_option]
        Player_value = input('Enter your option : ').lower()
        if Player_value == 'end':
            break
        if AI_value == 'scissors' and Player_value == 'paper':
            AI_score +=1
            print('AI wins ')
        elif AI_value == 'paper' and Player_value == 'stone':
            AI_score +=1
            print('AI wins ')
        elif AI_value == 'stone' and Player_value == 'scissors':
            AI_score +=1
            print('AI wins ')
        elif AI_value == Player_value:
            print('Draw')
        else:
            Player_score += 1
            print('Player wins ')
    print('AI Score :',AI_score,'Player Score : ',Player_score)
elif mode == 2:
    while True:
        Player_value = input('Enter Player1 option : ').lower()
        if Player_value =='end':
            break
        Player_value2 = input('Enter Player2 option : ').lower()
        if Player_value2 == 'end':
            break
        if Player_value2 == 'scissors' and Player_value == 'paper':
            Player2_score +=1
            print('Player 2  wins ')
        elif Player_value2 == 'paper' and Player_value == 'stone':
            Player2_score +=1
            print('Player 2 wins ')
        elif Player_value2 == 'stone' and Player_value == 'scissors':
            Player2_score +=1
            print('Player 2 wins ')
        elif Player_value2 == Player_value:
            print('Draw')
        else:
            Player_score += 1
            print('Player 1 wins ')
    print('Player 1 Score :',Player_score,'Player 2 Score : ',Player2_score)