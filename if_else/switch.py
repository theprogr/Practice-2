operation = input("Enter operation (+, -, *, /): ")
a = 10
b = 5

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    result = a / b
else:
    result = "Invalid operation"

print("Result:", result)
