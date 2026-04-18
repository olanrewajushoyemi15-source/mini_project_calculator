# Student Result System
name = input("\nEnter name of student: ")
school = input("\nEnter name of school: ")
class_room = input("\nEnter your class / level: ")


score1 = float(input("\nEnter score of subject 1: "))
score2 = float(input("\nEnter score of subject 2: "))
score3 = float(input("\nEnter score of subject 3: "))
score4 = float(input("\nEnter score of subject 4: "))

total = score1 + score2 + score3 + score4
percentage = total/4


print("\nStudent name: ", name)
print("\nName of school: ", school)
print("\nClassroom / level: ", class_room)
print("\ntotal", total)
print("\npercentage", percentage)

if percentage >= 80:
    print("Grade A")
elif percentage >= 70:
    print("Grade B ")
elif percentage >= 60:
    print("Grade C")
elif percentage >= 50:
    print("Grade D")
elif percentage >= 40:
    print("Grade E")
else:
    print("Advice To Withdraw")
