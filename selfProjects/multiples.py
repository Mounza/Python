#3 or 5 below 1000

a = [i for i in range(3, 1000, 3)]   # for numbers taht are lower than 1000 and multiples of 3
b = [i for i in range(5, 1000,5)]    #for numbers that are lower than 1000 and multiples of 5
in_a = set(a)
in_b = set(b)

x = in_b - in_a

result = a + list(x)
print(result)
c = sum(result)

print(c)

