fh = open('mbox-short.txt') #to take a look at the file

for lx in fh:
    ly = lx.rstrip()    #to strip the character from the right side
    print(ly.upper())   #to make them all upper case
