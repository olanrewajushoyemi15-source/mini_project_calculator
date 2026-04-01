# Mini project calculator that work with decimal and whole number
name = input("Enter your name")
print("Welcome", name)
print("Mini calculator:")
print("Operation:")

# Choose operation
op = input("choose operation(+, -, *, /)")

# Calculation
num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number:"))

if op == "+":
    result = num1 + num2
    print(f"\n{num1} + {num2} = {result}")
elif op == "-":
    result = num1 - num2
    print(f"\n{num1} - {num2} = {result}")

    # Handle possible error division by zero
elif op == "/":
    if num2 == 0:
        print("Error: Cannot divide by Zero")
    else:
        result = num1 / num2
    print(f"\n{num1} / {num2} = {result}")
elif op == "*":
    result = num1 * num2
    print(f"\n{num1} * {num2} = {result}")
else:
    print = ("Invalid operation")


# Percentage App that works with decimal
num = float(input("Enter the number: "))
perc = float(input("Enter the percentage: "))

result = (perc / 100) * num

print("The percentage of", num, "is", result)
