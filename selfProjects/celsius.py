askInput = input('Type in "c" for °C to °F or "f" for °F to °C: ')
if askInput == 'c':
    celsius = input('Enter Celsius: ')
    fahrenheit = (float(celsius) * 1.8) + 32
    print(float(fahrenheit))
elif askInput == 'f':
    fahrenheit = input('Enter Fahrenheit: ')
    celsius = (float(fahrenheit) - 32) / 1.8
    print(float(celsius))