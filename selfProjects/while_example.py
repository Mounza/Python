#will be printed 5 times because spam is 0 and while spam is less than 5 it will keep looping and always adds +1 to spam until spam reaches 5
spam = 0
while spam < 5:
    print('Hello world!')
    spam = spam + 1