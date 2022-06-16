weight = input('kg: ')
height = input('cm: ')

bmi = float(weight) / (float(height) * float(height)) * 10000

print(round(bmi, 2))

if bmi < 18.5:
    print('You are Underweight!')
elif bmi > 18.5 and bmi < 24.9:
    print('You are Normal Weight')
elif bmi > 25 and bmi < 29.9:
    print('You are Overweight')
else:
    print('You are Obese')