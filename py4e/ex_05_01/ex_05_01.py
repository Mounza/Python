num = 0
tot = 0.0
while True :                    # loop
    sval = input ('Enter a number: ')
    if sval == 'done' :
        break                   #exit mechanism
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue                #to loop back up
    #print(fval)
    num = num + 1
    tot = tot + fval

#print('ALL DONE')
print(tot,num,tot/num)
