# Smart Security System

# Ask user for input
has_keycard = True
knows_password = True
is_admin = True

has_keycard = input("Do you have a keycard?,(yes/no):").lower() == "yes"
knows_password = input(
    "Do you know the password?, (yes/no): ").lower() == "yes"
is_admin = input("Are you the admin?, (yes/no): ").lower() == "yes"
# Check Access

if has_keycard and knows_password:
    print("Access Granted")
elif is_admin:
    print("Acess Granted")
else:
    print("Access Denied")

 # Online Shopping Checking
items_in_cart = True
payment_successful = True

items_in_cart = input(
    "Do you have items in cart?, (yes/no):").lower() == "yes"
payment_successful = input(
    "Was your payment successful?, (yes/ no ):").lower() == "yes"

# Check Conditions
if items_in_cart and payment_successful:
    print("Check out successful, Order placed!: ")
elif not items_in_cart:
    print("Your cart is Empty, Add something before you check out: ")
elif not payment_successful:
    print("Payment failed, Please try again:")

# Traffic Simulator

light_color = True

light_color = input(
    "What colour is displayed on the Traffic light? (red, yellow, green)").lower()

# Check conditions

if light_color == ("red"):
    print("stop:")
elif light_color == ("yellow"):
    print("Ready to go")
elif light_color == ("green"):
    print("Go")

  # Exam Eligibility

eligibility = input("Enter attendance percentage")
fees = input("Have you paid your fees? (Yes / no)").lower()

if eligibility >= "75%":
    print("Your are eligible to sit for the exam: ")
elif fees == "yes":
    print("You are eligible")
else:
    print("you are not eligible")

# Weather Decision Maker

is_raining = input("is it raining today?(yes/no):").lower() == "yes"
is_sunny = input("is it sunny today? (yes/no)").lower() == "yes"
is_windy = input("is it windy? (yes/no)").lower() == "yes"

# Decision Making
if is_raining:
    print("take an unbrella:")
elif is_sunny and not is_windy:
    print("Great Weather! you can go out:")
elif is_windy:
    print("It's windy be careful when going out:")
else:
    print("Weather is unclear, please stay safe:")

# Exclusive Barbing Saloon
print("Hello, you are welcome to Exclusive Barbing Saloon")
print("You may have your seat:")
print("/n --- Choose Category")
category = input("Choose Category  (Adult / Children): ").lower()
if category == "adult":
    print("\n---choose Hairstyle!")
    print("1,  low cut(with dye) - #2000")
    print("2, Low cut (without dye) - #1500 ")
    print("3, Last Skin - #1000")
    print("4, Shave - #1000 ")
    choice = input("Enter your choice(1-4): ")
    if choice == "1":
        price = 2000
        Style = "Low cut with dye"
    elif choice == "2":
        price = 1500
        style = "low cut without dye"
    elif choice == "3":
        price = 1000
        style = "last skin"
    elif choice == "4":
        price = 1000
        style = "shave"
    else:
        print("invalid choice")
        exit()
elif category == "children":
    print("\n---choose Hairstyle!")
    print("1,  low cut -#1500")
    print("2 Last Skin - #1000")
    print("3, Shave - #500 ")
    choice = input("Enter your choice(1-3): ")
    if choice == "1":
        price = 1500
        Style = "Low cut"
    elif choice == "2":
        price = 1000
        style = "Last skin"
    elif choice == "3":
        price = 500
        style = "shave"
    else:
        print("Invalid choice!")
        exit()

# Final output
    print("\nBooking Confirmed!")
    print("Category:", category.capitalize())
    print("Hairstyle:", style)
    print("Price: #", price)
