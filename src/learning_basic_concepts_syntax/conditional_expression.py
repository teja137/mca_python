# conditional expression (ternary operator)
# X if condition else Y

num = -5
print("Positive" if num > 0 else "Negative")

num = 1
result = "Even" if num%2 == 0 else "odd"
print(result)

a = 3
b = 7
max_num = b if b > a else a
min_num = b if b < a else a
print(max_num)
print(min_num)

age = 18
result = "Adult" if age >= 18 else "Minor"
print(result)

temperature = 20
weather = "Hot" if temperature > 20 else "Cold"
print(weather)

user_role = "guest"
access_level = "Full access" if user_role == "admin" else "Limited access"
print(access_level)