han = open('mbox-short.txt')                     # open the file
lines = 0
for line in han:                                 # look through the file
    line = line.rstrip()                         # remove the whitespace
    wds = line.split()                           # break the string into words
    #Guardian Pattern a bit stronger
    #if len(wds) < 3 :                           # if length of words is less than 1
        #continue                                # continue/skip it
    #Guardian in a compound statement
    if len(wds) < 3 or wds[0] != 'From' :        # check if there are less than 3 words or first word is not from (guardian must come first/right order else it will fail)
        continue                                 # if its not skip the line
    if line.startswith('From'):
        lines = lines + 1
    print(wds[1])                                # if we find a line that starts with From then print the 3rd word

print('There were', lines, 'lines in the file with From as the first word')
