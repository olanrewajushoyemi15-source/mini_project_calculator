name = input("what is your name?")
age = int(input("what is your age?"))


with open("u.txt", "w") as file:
    information = file.write("Hello World"
                             "you can as well do well ")
    print(information)
