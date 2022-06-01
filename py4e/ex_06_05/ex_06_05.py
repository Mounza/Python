str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(':')
#print(ipos)
piece = str[ipos+2:]        # so it starts past the : and the blank space
#print(piece)
value = float(piece)
print(value)
#print(value+42.0)
