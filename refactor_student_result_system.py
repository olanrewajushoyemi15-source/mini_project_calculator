def get_score():
    return float(input("Enter Your Score: "))


def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F9"


def display_result(score, grade):
    print("Score: ", score)
    print("Grade: ", grade)


def main():
    while True:
        score = get_score()
        grade = calculate_grade(score)
        display_result(score, grade)

        again = input("Check another result?(yes/no): ")
        if again.lower() != "yes":
            print("Goodbye!")
            break


main()
