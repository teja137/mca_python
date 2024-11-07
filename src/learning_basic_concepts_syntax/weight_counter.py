#weight convertor

weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pounds? (K or P): ")

if unit == 'K':
    print(f"Weight in kilograms is: {round(weight*2.205,2)}kgs")
elif unit == 'P':
    print(f"Weight in pounds isL {round(weight/2.205, 2)}pounds")
else:
    print(f"{(unit)} was not valid.")