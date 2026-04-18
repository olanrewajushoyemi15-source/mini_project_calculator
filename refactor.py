cart = []


def add_item():
    item = input("Enter item name: ")
    cart.append(item)
    print(item, "added successfully! ")


def view_cart():
    if not cart:
        print("cart is empty ")
        return

    print("\nYour Cart: ")
    for item in cart:
        print("-", item)


def remove_item():
    item = input("Enter item to remove: ")

    if item in cart:
        cart.remove(item)
        print(item, "removed")
    else:
        print("Item not found")


def menu():
    while True:
        print("\n1. Add item ")
        print("\n2. View cart ")
        print("\n3. Remove item ")
        print("\n4. Exit ")

        choice = input("Choose menu ")
        if choice == "1":
            add_item()

        elif choice == "2":
            view_cart()

        elif choice == "3":
            remove_item()

        elif choice == "4":
            print("Goodbye! ")
            break
        else:
            print("Invalid Choice ")


menu()
