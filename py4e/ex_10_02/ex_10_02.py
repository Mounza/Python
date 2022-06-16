fname = input('Enter File: ')
if len(fname) < 1: fname = 'mbox-short.txt'
hand = open(fname)                               # open the file

di = dict()                                      # di = variable for dictionary
for line in hand:                                # read through the file
    if line.startswith("From "):
         line = line.rstrip()
    #print(line)
         wds = line.split()                           # split them into words
    #print(wds)
         time = wds[5]                    #to pull the hour from the From line
         timesplit = time.split(':')                #splitting it again using a colon to only get the hours
         hour = timesplit[0]
        #print('**',words,di.get(words,-99))     #.get says in its first parameters the key to look up which is word like the or fall or clown and 99 is the default value if the key doesnt exist

        #idiom: retrieve/create/update counter
         di[hour] = di.get(hour,0) + 1          # get old value from this key or zero and then add 1 to it

#print(di)

tmp = list()
for key, value in di.items():
    #print(k,v)
    newtuple = (key, value)                                   # make new tuple
    tmp.append(newtuple)                               # list of tuples

#print('Flipped',tmp)
result = sorted(tmp)
#print(result)
for count in result:
    print(count[0], count[1])
#for value, key in tmp[5]:
   # print(key, value)