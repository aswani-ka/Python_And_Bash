stud_grades = {
    "Catherine": "B",
    "Alex": "A",
    "Maya": "C",
    "Lisa": "D",
    "Rohan": "B"
}


new_student = input("Enter new student name: ")
new_grade = input("Enter the student grade: ")
if new_student in stud_grades:
    print("Student already exists.")
else:
    stud_grades[new_student] = new_grade


update_student = input("Enter the student name to update: ")
update_grade = input("Enter the new student grade: ")

if update_student in stud_grades:
    stud_grades[update_student] = update_grade
else:
    print("Student not found!")


print("\nStudent Grades:")
for name, grade in stud_grades.items():
    print(f"{name}: {grade}")


