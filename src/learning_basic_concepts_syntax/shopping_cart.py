# shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to by (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of {food}: "))
        foods.append(food)
        prices.append(price)


print("----- Your shopping cart -----")

for food, price in zip(foods, prices):
    print(f"{food} : {price}")
    total+=price

print(f"Your total is: {total}$")