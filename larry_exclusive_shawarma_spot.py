# customer's order
name = input("Enter your name")
print("Welcome to Exclusive Shawarma Spot", name)

# Exclusive shawarma spot menu list

while True:

    print("\n Choose category:")
    print("1. Chicken wrap shawarma (no sausage) - #2000:")
    print("2. Regular chicken wrap shawarma (single sausage) - #2500: ")
    print("3. Standard chicken wrap shawarma(double sausage) -#3000: ")
    print("4. Premium chicken wrap shawarma(double sausage with more chicken) - #3500: ")
    print("5. Combo chicken wrap shawarma(Double sausage with chicken and beef) - #4000")
    print("6. Order cancelled")
    print("7. Exit")

    category = input("Enter category(1 - 7): ")

    if category == "6":
        print("Oder cancelled")

    elif category == "7":
        print("Thank you for visiting Exclusive shawarma spot")
        break

    elif category == "1":
        qty = int(input("How many do you want?: "))
        total = qty * 2000
        print("Total bill is # ", total)
    elif category == "2":
        qty = int(input("How many do you want?: "))
        total = qty * 2500
        print("Your bill is #", total)
    elif category == "3":
        qty = int(input("How many do you want?: "))
        total = qty * 3000
        print("Your bill is #", total)
    elif category == "4":
        qty = int(input("How many do you want?: "))
        total = qty * 3500
        print("Your bill is #", total)
    elif category == "5":
        qty = int(input("How many do you want?: "))
        total = qty * 4000
        print("Your bill is #", total)
    else:
        print("Invalid Category:")
