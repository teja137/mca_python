name = input("Enter your full name: ")

length = len(name)
print(length)

space = name.find(" ")
find_b = name.find("b")
print(space)
print(find_b)

space = name.rfind(" ")
find_b = name.rfind("b")
print(space)
print(find_b)

upper_case_first_letter = name.capitalize()
print(upper_case_first_letter)

upper_case = name.upper()
print(upper_case)

lower_case = name.lower()
print(lower_case)

contains_digits = name.isdigit()
print(contains_digits)

contains_alphabets = name.isalpha()
print(contains_alphabets)

phone_number = input("Enter your phone number: ")
count_character = phone_number.count("1")
print(count_character)

replace = phone_number.replace("-", "")
print(replace)

print(help(str))