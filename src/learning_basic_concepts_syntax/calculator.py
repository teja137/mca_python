#calculator app

operator = input("Enter an operator ('+', '-', '*', '/', '%'): ")
input1 = float(input("Enter your first number: "))
input2 = float(input("Enter your second number: "))

if operator == '+':
    print(f"Result = {round(input1 + input2, 3)}.")
elif operator == '-':
    print(f"Result = {round(input1 - input2, 3)}.")
elif operator == '*':
    print(f"Result = {round(input1 * input2, 3)}.")
elif operator == '/':
    print(f"Result = {round(input1 / input2, 3)}.")
elif operator == '%':
    print(f"Result = {round(input1 % input2, 3)}.")
else:
    print(f"{operator} is not valid. Please enter a valid operator")
