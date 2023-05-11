# Dict example
student_scores = {
    "Student1": 81,
    "Student2": 78,
    "Student3": 99,
    "Student4": 74,
    "Student5": 62,
}
student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)