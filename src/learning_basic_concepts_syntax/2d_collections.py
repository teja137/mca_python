#2d lists

fruits     =    ["apple", "banana", "citrus"]
vegetables =    ["tomato", "green chilli", "egg plant"]
meat       =    ["mutton", "chicken", "fish"]

groceries = [fruits,vegetables,meat]
print(groceries)
print(groceries[0])
print(groceries[1])
print(groceries[2])
print(groceries[0][0])
print(groceries[0][1])
print(groceries[0][2])

for collection in groceries:
    print(collection)

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()