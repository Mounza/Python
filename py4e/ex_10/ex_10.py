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

tmp = list()
for k,v in di.items():
    #print(k,v)
    newt = (v,k)                                   # make new tuple
    tmp.append(newt)                               # list of tuples

#print('Flipped',tmp)

tmp = sorted(tmp, reverse=True)
#print('Sorted',tmp[:5])

for v,k in tmp[:5]:
    print(k,v)