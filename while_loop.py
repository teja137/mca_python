name = input("Enter your name: ")
age = int(input("Enter your age: "))
while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")

while age < 0:
    print("You did not enter your age")
    age = int(input("Enter your age: "))
print(f"your {age} years old")

food = input("Enter the food you like (q to quit): ")

while not food == 'q':
    print(f"your fav food is: {food}")
    food = input("Enter the food you like (q to quit): ")
print("bye 👋🏼")

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Please enter a number between 1 - 10: "))
print(f"The number you've entered is {num}")
