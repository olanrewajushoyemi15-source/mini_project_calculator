# Import Math

def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if num2 == 0:
            print("Error! Cannot divide by zero")
        else:
            return a / b
    else:
        print("invalid operation")


# User input
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
operation = input("choose operation(-,+,*,/)")

result = calculate(num1, num2, operation)

print("Result is", result)
