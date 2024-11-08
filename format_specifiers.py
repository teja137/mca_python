# formats the value

price1 = 3000.14159
price2 = -9870.659
price3 = 1370.731

#decimal point
print(f"Price 1 is: ₹{price1:.2f}")
print(f"Price 2 is: ₹{price2:.2f}")
print(f"Price 3 is: ₹{price3:.2f}")

#adding spaces
print(f"Price 1 is: ₹{price1:10}")
print(f"Price 2 is: ₹{price2:10}")
print(f"Price 3 is: ₹{price3:10}")

#zero paddded
print(f"Price 1 is: ₹{price1:010}")
print(f"Price 2 is: ₹{price2:010}")
print(f"Price 3 is: ₹{price3:010}")

#left justifying
print(f"Price 1 is: ₹{price1:<10}")
print(f"Price 2 is: ₹{price2:<10}")
print(f"Price 3 is: ₹{price3:<10}")

#right justifying/default
print(f"Price 1 is: ₹{price1:>10}")
print(f"Price 2 is: ₹{price2:>10}")
print(f"Price 3 is: ₹{price3:>10}")

#center align justifying
print(f"Price 1 is: ₹{price1:^10}")
print(f"Price 2 is: ₹{price2:^10}")
print(f"Price 3 is: ₹{price3:^10}")

#displaying positive values
print(f"Price 1 is: ₹{price1:+}")
print(f"Price 2 is: ₹{price2:+}")
print(f"Price 3 is: ₹{price3:+}")

print(f"Price 1 is: ₹{price1: }")
print(f"Price 2 is: ₹{price2: }")
print(f"Price 3 is: ₹{price3: }")

#displaying negative values
print(f"Price 1 is: ₹{price1:-}")
print(f"Price 2 is: ₹{price2:-}")
print(f"Price 3 is: ₹{price3:-}")

#thousand seperator
print(f"Price 1 is: ₹{price1:,}")
print(f"Price 2 is: ₹{price2:,}")
print(f"Price 3 is: ₹{price3:,}")

print(f"Price 1 is: ₹{price1:+,.2f}")
print(f"Price 2 is: ₹{price2:+,.2f}")
print(f"Price 3 is: ₹{price3:+,.2f}")