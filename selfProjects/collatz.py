# function named collatz() that has one parameter named number
def collatz(number):
    # if number is even collatz() should print number // 2 and return this value
    if (number % 2) == 0:
        value1 = number // 2
        print(value1)
        return value1
    # if number is odd, then collatz() should print and return 3 * number + 1
    else:
        value2 = 3 * number + 1
        print(value2)
        return (value2)


# write program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value1.
ask = input('type in a integer ')

try:
    while ask != 1:
        # remember to convert the return value from input() to an integer with the int() function otherwise, it will be a string value
        ask = collatz(int(ask))
except ValueError:
    print('You did not enter a number.')
