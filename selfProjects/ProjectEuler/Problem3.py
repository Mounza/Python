sumNumber = 0
squareSum = 0
for x in range(1, 101):
    sumNumber = sumNumber + x
    squareSum = sumNumber ** 2

range1 = range(1,101)
result = [number ** 2 for number in range1]
sum1 = sum(result)

finalResult = squareSum - sum1
print(finalResult)