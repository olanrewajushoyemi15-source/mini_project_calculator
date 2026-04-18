

history = []

user = input("Enter your name : ")
print("you are welcome", user)


# Functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "cannot divide by zero"


def square(a):
    return a ** 2


def cube(a):
    return a ** 3


def square_root(a):
    if a < 0:
        return "Error! Navigate number"
    return a ** 0.5


# Load previous history from file
try:
    with open("history.txt", "r") as file:
        for line in file:
            history.append(line.strip())
except FileNotFoundError:
    pass
while True:
    print("\n_____Choose Operation_______:  ")
    print("1. add ")
    print("2. Subtract ")
    print("3. Multiply ")
    print("4. Divide ")
    print("5. Square ")
    print("6. Cube ")
    print("7. Square root ")
    print("8. View History ")
    print("9. Exit ")

    choice = input("Choose an option (1 - 9): ")

    if choice in ["1", "2", "3", "4"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            result = add(a, b)
            operation = f"{a} + {b} = {result}"

        elif choice == "2":
            result = subtract(a, b)
            operation = f"{a} - {b}= {result}"

        elif choice == "3":
            result = multiply(a, b)
            operation = f"{a} * {b} = {result}"

        elif choice == "4":
            result = divide(a, b)
            operation = f"{a} / {b} = {result}"

        print("Result:", result)
        history.append(operation)

    elif choice in ["5", "6", "7"]:

        a = float(input("Enter number:"))

        if choice == "5":
            result = square(a)
            operation = f"{a}^2 = {result}"

        elif choice == "6":
            result = cube(a)
            operation = f"{a}^3 = {result}"

        elif choice == "7":
            result = square_root(a)
            operation = f"sqrt({a}) = {result}"

            print("Result:", result)
        history.append(operation)

    elif choice == "8":
        print("\n----- History ------")
        for item in history:
            print(item)
    elif choice == "9":
        with open("history.txt", "w")as file:
            for item in history:
                file.write(item + "\n")
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try Again  ")
