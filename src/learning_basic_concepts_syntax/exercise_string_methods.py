# validate user input exercise
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits   

user_name = input("Enter a username: ")
input_length = len(user_name)
find_space = user_name.find(" ")
find_alphabets = user_name.isalpha()

if input_length > 12:
    print("Your username can't be more than 12 characters.")
elif not find_space == -1:
    print("username must not contain spaces")
elif not find_alphabets:
    print("username must not contain digits")
else:
    print(f"Welcome {user_name}")