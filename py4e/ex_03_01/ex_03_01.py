sh = input("Enter Hours: ")     # sh = string hours
sr = input("Enter Rate: ")      # sr = string rate
fh = float(sh)                  #floating hours
fr = float(sr)                  #floating point rate
#print(fh, fr)
if fh > 40 :
    #print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    #print(reg,otp)
    xp = reg + otp
else:
    #print("Regular")
    xp = fh * fr                 #rate = floating hour * floating rate
print ("Pay:", xp)
