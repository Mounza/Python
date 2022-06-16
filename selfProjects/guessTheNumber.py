import random
print('Hello, Welcome to Guess the Number')
print('Do you want to play? ')
userInput = input()

if userInput != 'yes':
    quit()

numberInput = input('Thats great to hear! First enter a number for as high as you want it to go ')

if numberInput.isdigit():
    numberInput = int(numberInput)

    if numberInput <= 0:
        print('Please type a number larger than 0 next time.')
    elif numberInput > 0:
        print('Great! You have 10 tries to find the random number between 0 and ' + str(numberInput) + ' Good Luck!')
    else:
        print('Please type a number next time.')
        quit()

randomNumber = random.randrange(0, numberInput)
count = 0

while True:
    count += 1
    guessInput = input()
    if guessInput.isdigit():
        guessInput = int(guessInput)
    else:
        print('Please type in a number ')
        continue
    if guessInput == randomNumber:
        print('Wow! you got the number in ' + str(count) + ' tries')
        break
    elif count == 10:
        print('You failed to find the Number, the number was ' + str(randomNumber))
        break
    else:
        if guessInput > randomNumber:
            print('You were above the number! ')
        else:
            print('You were below the number! ')




