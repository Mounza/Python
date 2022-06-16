low = 0
high = 100
print('Please think of a number between 0 and 100!')
while True:
    guess = (low + high) // 2
    print('Is your secret number ', guess)
    guessInput = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
    if guessInput == 'h':
        high = guess
    elif guessInput == 'l':
        low = guess
    elif guessInput == 'c':
        print('Game over. Your secret number was: ',guess)
        break
    else:
        print('Sorry, I did not understand your input.')
        continue

