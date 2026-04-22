# _______Contact Manager _____-

contacts = {
    "Ahmed": "09013550274",
    "Olanrewaju": "08165169640"
}
# Name = key
# number = value

contacts = {}

while True:
    print("\n ------ CONTACT MANAGER -------")
    print("1. Add contact")
    print("2. View Contact")
    print("3. Search contact")
    print("4. Delete Contact")
    print("5. Exit ")

    choice = input("Enter your choice(1 - 5):   ")

    # Add contact
    if choice == "1":
        phone_number = input("Enter number: ")
        name = input("Enter your name ")

        contacts[phone_number] = name
        print("Contact added successfully ")

        # View Contact
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found")
        else:
            print("\n---- Contact List---")
            for name, phone_number in contacts.items():
                print(name, ":", phone_number)

       # Search Contacts
    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("Contact Not Found: ")

            # Delete Contact
    elif choice == "4":
        name = input("Enter Name to Delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact Deleted")
        else:
            print("Contact not found")
            # Exit
    elif choice == "5":
        print("Goodbye: ")
        break
    else:
        print("Inavalid choice: ")
