fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        colpos = line.find(':')
        number = line[colpos + 1:].strip()
        total = total + float(number)
    print(line)
average = total / count
print('There were', count, 'subject lines in', fname)
print('Average spam confidence: ', average)
