# this program says hello and asks for the name
print('Hello world!')

print('What is your name?') # ask user for their name
myName = input()                                             # input from user
print('It is good to meet you, ' + myName)                   # answer + output of what user typed in
print('The length of your name is: ')
print(len(myName))                                           # len takes a string argument and evaluates the number of characters

print('What is your age?')                                   # ask user for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')

