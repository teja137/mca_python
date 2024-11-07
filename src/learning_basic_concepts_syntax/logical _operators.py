# logical operators

'''
or - atleast one condition must be true 
and - both conditions must be true
not - intverts the condition
'''

temp = 30
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The out door event is cancelled")
else:
    print("the out door event is still scheduled")

temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is hot outside 🥵")
    print("It is SUNNY 🌞")
elif temp <= 0 and is_sunny:
    print("Tt is cold outside ☃️")
    print("It is SUNNY 🌞")
elif temp < 28 and temp < 0 and not is_sunny:
    print("Tt is warn outside 😎")
    print("It is CLOUDY ☁️")
elif temp >= 28 and not is_sunny:
    print("It is hot outside 🥵")
    print("It is CLOUDY ☁️")
elif temp <= 0 and not is_sunny:
    print("Tt is cold outside ☃️")
    print("It is CLOUDY ☁️")
elif temp < 28 and temp > 0 and not is_sunny:
    print("Tt is warn outside 😎")
    print("It is CLOUDY ☁️")
