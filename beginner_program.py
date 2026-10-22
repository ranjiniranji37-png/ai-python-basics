# Beginner program: Student Grade Calculator

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    return "F"


def main():
    students = {"Arun": 92, "Priya": 78, "Karthik": 65, "Divya": 48}
    print("Student Grade Report")
    print("-" * 30)
    for name, marks in students.items():
        print(f"{name:10} {marks:3}  Grade: {calculate_grade(marks)}")

    average = sum(students.values()) / len(students)
    print("-" * 30)
    print(f"Class average: {average:.2f}")


if __name__ == "__main__":
    main()
