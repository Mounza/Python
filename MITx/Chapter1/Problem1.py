s = 'abcbcd'
#create an empty string to hold alpha substrings
newString = ''
#even one more string to store longest substring
storedString = ''
prevChar = ''

# iterate over string
for char in s:                                                                                  #für buchstaben im text (s)
    # compare neighbors
    if prevChar <= char:                                                                        #wenn der vorherige buchstabe kleiner is als der aktuelle
        newString += char                                                                       #dann ist der neue string der neue string + aktueller buchstabe
        # if neighbor 1 <= neighbor 2
        if len(newString) > len(storedString):                                                  #wenn die länge des neuen strings länger ist als vom gespeicherten string
            # store that value
            storedString = newString                                                            #dann ist der gespeichterte string jetzt der neue string
    # is current substring longer than any previous one?
    else:                                                                                       #wenn er nicht kleiner ist als der aktuelle buchstabe
        # remember that
        newString = char                                                                        #dann is der neue string der nächste buchstabe
    # you dont have an alphabetical substring so get rid of your current alpha substring
    prevChar = char                                                                             #der vorherige buchstabe is der neue buchstabe
#report result
print('Longest substring in alphabetical order is: ' + storedString )                           







