sh = input("Enter Hours: ")     # sh = string hours
sr = input("Enter Rate: ")      # sr = string rate
try:
    fh = float(sh)                  #floating hours
    fr = float(sr)                  #floating point rate
except:
    print("Error, please enter numeric input")
    quit()                          # do not continue

print(fh, fr)
if fh > 40 :
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr                 #rate = floating hour * floating rate
print ("Pay:", xp)
