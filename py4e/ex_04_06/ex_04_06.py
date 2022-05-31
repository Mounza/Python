def computepay(hours, rate) :
    #print("In computepay", hours, rate)
    if hours > 40 :
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate       #rate = floating hour * floating rate
    #print("Returning", pay)
    return pay

sh = input("Enter Hours: ")     # sh = string hours
sr = input("Enter Rate: ")      # sr = string rate
fh = float(sh)                  #floating hours
fr = float(sr)                  #floating point rate

xp = computepay(fh, fr)

print ("Pay:", xp)
