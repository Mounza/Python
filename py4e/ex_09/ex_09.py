fname = input('Enter File: ')
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)                               # open the file

di = dict()                                      # di = variable for dictionary
for line in hand:                                # read through the file
    line = line.rstrip()
    #print(line)
    wds = line.split()                           # split them into words
    #print(wds)
    for words in wds:
        #print('**',words,di.get(words,-99))     #.get says in its first parameters the key to look up which is word like the or fall or clown and 99 is the default value if the key doesnt exist

        #idiom: retrieve/create/update counter
        di[words] = di.get(words,0) + 1          # get old value from this key or zero and then add 1 to it

#print(di)

#find most common word
largest = -1                                     # Using -1 as a flag in this case is acceptable because we are only dealing with positive values in finding the highest frequency email sender
theword = None
for key,value in di.items():                     # give me the key value pairs/ assignment statement for key and value/ key and value take on the successive values
    if value > largest :
        largest = value
        theword = key                            # capture/remember the word that was largest

print(theword,largest)

        #if words in di:
            #di[words] = di[words] + 1           # to add +1 to the count of words in the dictionary*
       # else:
            #di[words] = 1                       # to add the new word to the dictionary
        #print(words, di[words])                 # to make sure that words is going through all the words in the file

