largest = None
smallest = None
while True :                    # loop
    num = input ('Enter a number: ')
    if num == 'done' :
        break                   #exit mechanism
    try:
        num = int(num)
        if smallest is None or num < smallest :
            smallest = num
        elif largest is None or num > largest :
            largest = num
    except:
        print('Invalid input')
        continue                #to loop back up
print ("Maximum is", largest)
print ("Minimum is", smallest)
