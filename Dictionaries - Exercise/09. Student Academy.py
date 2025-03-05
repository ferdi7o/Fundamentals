students = int(input())
students_info = {}

for _ in range(students):
    student = input()
    grade = float(input())

    if student not in students_info.keys():
        students_info[student] = [grade, 1]
    else:
        students_info[student][0] += grade
        students_info[student][1] += 1

for student, grade in students_info.items():
    avarage_grade = grade[0] / grade[1]
    if avarage_grade < 4.50:
        continue
    print(f"{student} -> {avarage_grade:.2f}")