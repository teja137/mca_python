# compund interest
# formula - total = principle *pow((1+rate/100), time)

rate = 0
principle = 0
time = 0
total = 0

while True:
    rate = float(input("Enter the rate amount: "))
    if rate < 0:
        print("Enter a valid rate, less than 0 is invalid. {rate} INVALID.")
    else:
        break

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Enter a valid principle, less than 0 is invalid. {principle} INVALID.")
    else:
        break

while True:
    time = int(input("Enter the time amount: "))
    if time < 0:
        print("Enter a valid time, less than 0 is invalid. {time} INVALID.")
    else:
        break

total = principle *pow((1+rate/100), time)

print(f"Balance after {time} year's: ₹{total:.2f}")