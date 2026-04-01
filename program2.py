# float
total_package = 200.00
print(total_package)

# Input/Output
company_name = input("Enter name of company:")
print(f"you are welcome to {company_name}")
agent_name = input("Enter agent name:")
print(f"I'm agent {agent_name}")
full_name = input("Enter your full name")
print(
    f"How can we be of help to achieve your dream home Mr {full_name} what type of home are you looking for")

home_type = input("Enter type of house:")
print(home_type, "will be perfectly okay for your family")

age = int(input("Enter your age"))
if age >= 18:
    print("you are old enough get a home with us")
else:
    print("you are still a minor :")


r = 0
while True:
    i = int(("Enter number to add"))
    if i != 0:
        r += 1
        print(f"the total numbernow is{r}")
