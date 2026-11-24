import sys 
try:
    first_number = float (input("Enter the first_number "))
    second_number = float(input("Enter the second_number "))
except ValueError:
    print("Please enter valid numbers")
    sys.exit()
operation = input("Enter an operation (+,-,*,/)")
if operation == "+":
    result = first_number + second_number
    print(result)
elif operation == "-":
    result = first_number - second_number
    print(result)
elif operation == "*":
    result = first_number * second_number 
    print(result)
elif operation == "/":
    if second_number == 0:
        print("you cannot divide by zero")
    else:
        result = first_number / second_number
        print(result)
else:
    print("Unknown operator")
