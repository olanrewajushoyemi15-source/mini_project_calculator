file_one = open("student_note.txt", "w")
Sholey = [
    "i'm olanrewaju Ahmed Shoyemi \n"
    "A student of University of Ibadan \n"
    "Currently learning a python langauage programming \n"
    "Passionate About Learning \n"
    "A 400 level student.... \n"

]

file_one.write("The story of my life...\n")
file_one.writelines(Sholey)
file_one.close()

# Reading

file_one = open("student_note.txt", "r")
print("This is the content of the student_note file \n")
print(file_one.read())

note = input("Enter Your name: ")
with open("student_note.txt", "a") as file:
    file.write(note + "\n")

    with open("student_note.txt", "a") as file:
        file.write("A new line is added.. \n"
                   "And this too.. \n"
                   "All together can become one... \n")

# file_one = open("student_note.txt", "r")
# for line in file_one:
# print(line, end="")

# A program that counts the number of lines in a text file
