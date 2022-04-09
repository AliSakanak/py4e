import random

options = ['rock', 'paper', 'scissors']
gamemodes = {'1': 'First to 3', '2': 'First to 10', '3': 'Endless!'}
user_score = 0
computer_score = 0
while True:
    game_selection = input('Choose game type! (Type number):(1)First to 3, (2)First to 10, (3)Endless!')
    if game_selection not in gamemodes.keys():
        print('Please correctly type the number of the game type you want to play!')
        continue
    else:
        print('Starting gamemode ', gamemodes[game_selection])
        break
while True:
    if game_selection == '2':
        if user_score == 10 or computer_score == 10:
            break
    if game_selection == '1':
        if user_score == 3 or computer_score == 3:
            break
    user_choice = input('Type rock/paper/scissors or Q to quit: ').lower()
    if user_choice == 'q':
        break
    if user_choice not in options:
        print('Please choose from rock/paper/scissors (check spelling!)')
        continue
    rand_pick = random.randint(0, 2)
    computer_pick = options[rand_pick]
    print("Computer's choice: {}".format(computer_pick))

    if user_choice == 'rock' and computer_pick == 'scissors':
        user_score += 1
        print('You won!')
    elif user_choice == 'paper' and computer_pick == 'rock':
        user_score += 1
        print('You won!')
    elif user_choice == 'scissors' and computer_pick == 'paper':
        user_score += 1
        print('You won!')
    elif user_choice == computer_pick:
        print("It's a draw!")
    else:
        computer_score += 1
        print('Computer won!')
print('You scored {} and computer scored {}.'.format(user_score, computer_score))
if user_score > computer_score:
    print('You won by {} points! Well done!'.format(user_score - computer_score))
elif computer_score > user_score:
    print('You lost by {} points! Unlucky!'.format(computer_score - user_score))
elif computer_score == user_score:
    print('Wow! It was a draw!')
