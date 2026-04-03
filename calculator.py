user = input("Enter your name : ")
print("you are welcome", user)


history = []

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

    choice = input("Enter choice (1 - 9): ")
    if choice == "9":
        print("Goodbye! ")
        break
    elif choice == "8":
        if history:
            print("\n ---- History -----")
            for item in history:
                print(item)
if choice in ["1", "2", "3", "4"]:
    try:
        a = float(input("Enter first number"))
        b = float(input("Enter second number "))
    except ValueError:
        print("Please Enter valid number")
        continue
    if choice == "1":
        result = add(a, b)
        print("Result:", result)
        history.append(f"{a} + {b} = {result}")
        with open("history.txt", "a")as file:
            file.write(f"{a} + {b} = {result}\n ")
            print("\nPress Enter to continue....")

    elif choice == "2":
        result = subtract(a, b)
        print("Result:", result)
        history.append(f"{a} - {b} = {result}")
        with open("history.txt", "a")as file:
            file.write(f"{a} - {b} = {result}\n ")
            print("\nPress Enter to continue....")
