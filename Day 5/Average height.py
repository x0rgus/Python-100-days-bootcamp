# Simulates len() and sum()


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

student_count = 0
allheights = 0
for height in student_heights:
    allheights += height
    student_count += 1

average = round(allheights/student_count)
print(average)
