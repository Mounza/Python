play = input ('Do you want to play? ')

if play != 'yes':
    quit()

print('Welcome! Lets play a Random number Guessing Game ')

guess = input ('Write a number you want to guess between ')
if guess.isdigit():
    guess = int(guess)

    if guess <= 0:
        print('Please type a number larger than 0 next time.')
    elif guess > 0:
        print('Guess a Number between 0 and',guess,'Good Luck!')
    else:
        print('Please type a number next time.')
        quit()

import random
r = random.randrange(0, guess)
guesses = 0

while True:
    guesses += 1
    answer = input('Guess a number ')
    if answer.isdigit():
        answer = int(answer)
    else:
        print('Please type in a number ')
        continue

    if answer == r:
        print('You got it! ')
        break
    else:
        if answer > r:
            print('You were above the number! ')
        else:
            print('You were below the number! ')

print('You got it in',guesses, "guesses")
