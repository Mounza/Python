import math
import numpy_financial as npf
b = 0

while True:

    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print('5.Square')
    print('6.Root')
    print('7.Pythagorean')
    print('8.Income')
    print('9.Profit')
    print('10.Debt')
    print('11.Loan')
    a = input('Enter choice(1/2/3/4/..): ')
    if a == '1':
        ask = input('Enter a number: ')
        askP = input('Enter another number: ')
        b = int(askP) + int(ask)
        print(ask, '+', askP, 'ist:', b)
    elif a == '3':
        ask = input('Enter a number ')
        askM = input('Enter another number ')
        c = int(ask) * int(askM)
        print(ask, '*', askM, 'ist:', c)
    elif a == '2':
        ask = input('Enter a number ')
        askM = input('Enter another number: ')
        c = int(ask) - int(askM)
        print(ask, '-', askM, 'ist:', c)
    elif a == '4':
        ask = input('Enter a number ')
        askM = input('Enter another number: ')
        c = int(ask) / int(askM)
        print(ask, '/', askM, 'ist:', c)
    elif a == '5':
        ask = input('Enter a number ')
        askM = input('Enter another number: ')
        c = int(ask) ** int(askM)
        print(ask, 'hoch', askM, 'ist:', c)
    elif a == '6':
        ask = input('Enter a number ')
        c = math.sqrt(ask)
        print('Wurzel aus', ask, 'ist:', c)
    elif a == '7':
        ask = input('Enter a number ')
        askM = input('Enter another number: ')
        c = math.sqrt(ask ** 2 + askM ** 2)
        print(c)
    elif a == '8':
        ask = input('Hourly Wage:')
        askM = input('Hours Worked: ')
        c = float(ask) * float(askM)
        print('You earned :', c)
    elif a == '11':
        int_Rate = input('Interest Rate: ')
        years = input('Years: ')
        payment_year = input('Number of Payments each year: ')
        amt_borrowed = input('Amount you borrowed: ')
        interest = float(int_Rate) / float(100)
        payment = npf.pmt(float(interest) / float(payment_year), float(years) * float(payment_year), float(amt_borrowed)) *- float(1)
        total_payments = float(payment) * float(years) * float(payment_year)
        total_interest = float(total_payments) - float(amt_borrowed)
        print("Your monthly payment is: ${:,.2f}.".format(payment))
        print("Assuming all payments are made on time, at the agreed upon amount.")
        print("------------------------------------------------------------------")
        print("Total principal paid: ${:,.2f}.".format(float(amt_borrowed)))
        print("Total interest paid:  ${:,.2f}.".format(float(total_interest)))
        print("Total payments made:  ${:,.2f}.".format(float(total_payments)))
    else:
        quit()


