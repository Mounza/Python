fh = open("romeo.txt")               #what file to open
data=[]                              #for the list of words
for each in fh:
    words=each.split()               # split each line into words
    for word in words:               #word iteration iterates through each word in the line
        if word not in data:
            data.append(word)        #updates the list
print(sorted(data))                  #order
