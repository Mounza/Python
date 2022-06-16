name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)

di = dict()                     #directory
for line in handle:             #read through the file
    if line.startswith("From "):
    #line = line.rstrip()        # to remove the white space to the right
        linelist = line.split()         # to split them into words
        sender = linelist[1]
        if sender in di:
            di[sender] = di[sender] + 1
        else:
            di[sender] = 1


largest = -1
theword = None
for key,value in di.items():                     # give me the key value pairs/ assignment statement for key and value/ key and value take on the successive values
    if value > largest :
        largest = value
        theword = key                            # capture/remember the word that was largest

print(theword,largest)