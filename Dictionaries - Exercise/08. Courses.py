info = input()
courses_and_students = {}

while info != "end":
    course, student = info.split(" : ")
    if course not in courses_and_students.keys():
        courses_and_students[course] = [student]
    else:
        courses_and_students[course].append(student)

    info = input()

for element in courses_and_students.keys():
    print(f"{element}: {len(courses_and_students[element])}")
    for students in courses_and_students[element]:
        print(f"-- {students}")