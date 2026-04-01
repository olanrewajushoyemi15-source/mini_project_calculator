# Larry exclusive shawarma spot
customers_name = input("Enter your name")

print("Welcome to Larry exclusive shawarma spot", customers_name)
print("\n -- You may have your seat: ")

cravings = (input(
    "What is your cravings today?, (1= standard chicken wrap,2=premium chicken wrap, 3=combo chicken wrap)"))
if cravings == "1":
    print("Recommended: standard chicken wrap with single sausage")
elif cravings == "2":
    print("Recommended:premium chicken wrap with double sausage",)
elif cravings == "3":
    print("Recommended: combo chicken wrap comes with chicken,beef and double sausage")
else:
    print("invalid order!")
