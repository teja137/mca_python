# collections = single "variable" used to store multiple values

# list = [] ordered and changeable. Duplicates ok

fruits = ["blue berry", "straw berry", "black berry"]

print(fruits)
print(fruits[0])
print(fruits[1])
# print(fruits[3])
print(fruits[:3:2])
print(fruits[-1])
print(fruits[::-1])

for fruit in fruits:
    print(fruit)

# print(dir(fruits))
# print(help(fruits))

print(len(fruits))
print("apple" in fruits)
print("black berry" in fruits)

fruits[0] = "red berry"

for fruit in fruits:
    print(fruit)

fruits.append("orange berry")
print(fruits)

fruits.remove("black berry")
print(fruits)

fruits.insert(0, "apple")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

# fruits.clear()
# print(fruits)

print(fruits.index("apple"))


print(fruits.count("apple"))
print(fruits.count("mango"))

# Set = {} unordered and immutable, but Add/Remove OK. No duplicated

places = {"Swiss", "England","USA","India", "India"}
print(places)
print(len(places))
print("paris" in places)
print("Swiss" in places)

places.add("Alaska")
print(places)

places.remove("India")
print(places)

places.pop()
print(places)

places.clear()
print()

# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

minds = ("Einstein", "Osho", "Alan watts", "Osho")

print(len(minds))
print("Osho" in minds)
print(minds.index("Alan watts"))
print(minds.count("Osho"))