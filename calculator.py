a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ").strip()
b = float(input("Enter second number: "))

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    result = "Cannot divide by zero" if b == 0 else a / b
else:
    result = "Invalid operator"

print(result)
