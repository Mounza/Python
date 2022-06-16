import random


user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors']

ask = input ('Do you want to play? ')
if ask.lower() != 'yes':
    quit()

print('Hello! Welcome to Rock, Paper, Scissors')

while True:
    random_number = random.randint(0, 2)
    user_input = input('Rock, Paper or Scissors? or q if you want to quit ').lower()
    computer_pick = options[random_number]
    if user_input == 'q':
        print('Your score is',user_wins,'W', computer_wins, 'L')
        quit()
    elif user_input not in options:
        print('Please enter a correct option')
        continue
    elif user_input == 'rock' and computer_pick == 'scissors':
        user_wins += 1
        print('You Won')
    elif user_input == 'scissors' and computer_pick == 'paper':
        user_wins += 1
        print('You Won')
    elif user_input == 'paper' and computer_pick == 'rock':
        user_wins += 1
        print('You Won')
    else:
        computer_wins += 1
        print('You Lost')

