#exercise02 - shopping cart program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?:  "))
quantity = int(input("How many items would you like?: "))
total = price*quantity
print(f"You have bought {quantity} x {item}")
print(f"Your total is: ₹{total}")