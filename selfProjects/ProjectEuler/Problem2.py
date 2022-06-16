x = 1
y = 1
sum = 0
maxNumber = 0

while maxNumber <= 4000000:
    if maxNumber % 2 == 0:
        sum += maxNumber
    x = y
    y = maxNumber
    maxNumber = x + y

print(sum)