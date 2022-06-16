playing = input('Do you want to play?' )

if playing.lower() != 'yes':
    quit()

print('Welcome to my Quiz! Lets Play')

count = 0

answer1 = input('What does "www" stand for in a website browser?' )
if answer1 == 'world wide web' or 'World Wide Web':
    print('Correct!')
    count = count + 1
else:
    print('Incorrect')

answer2 = input('How long is an Olympic swimming pool (in meters)?')
if answer2 == '50' or '50 meters' or '50m':
    print('Correct!')
    count = count + 1
else:
    print('Incorrect')

answer3 = input('What is the name of the biggest technology company in South Korea?')
if answer3 == 'Samsung' or 'samsung':
    print('Correct!')
    count = count + 1
else:
    print('Incorrect')

answer4 = input('Who was the first woman to win a Nobel Prize (in 1903)?')
if answer4 == 'Marie Curie' or 'marie curie':
    print('Correct!')
    count = count + 1
else:
    print('Incorrect')

answer5 = input('What is the name of the largest ocean on earth?')
if answer5 == 'Pacific Ocean' or 'pacific ocean':
    print('Correct!')
    count = count + 1
else:
    print('Incorrect')

print('These were all the Questions! you got', count, 'Questions correct')
