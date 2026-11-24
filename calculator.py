first_number = float (input("Enter the first_number "))
second_number = float(input("Enter the second_number "))
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
    result = first_number / second_number
    print(result)
else:
    print("Unknown operator")
