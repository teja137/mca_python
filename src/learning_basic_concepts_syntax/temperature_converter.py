#Temperature converter

unit = input("Is the temperature in Celsius or Fahrenheit (C/F): ")
temperature = float(input("Enter the temperature: "))

if unit == 'C':
    print(f"The temperatire in Fahrenheit is: {round((9*temperature)/5+32,1)}°F")
elif unit == 'F':
    print(f"The temperature in Celsius is: {round((temperature-32)*5/9,1)}°C")
else:
    print(f"{unit} is an invalid unit of measurement.")