exam_result = {}
launguage_count = {}
while True:
    command = input()
    if command == "exam finished":
        break

    info = command.split("-")
    name = info[0]
    language = info[1] # maybe banned
    if language == "banned":
        for language in exam_result.keys():
            if name in exam_result[language]:
                del exam_result[language][name]
        continue
    points = int(info[2]) # points from exam
    if language not in exam_result.keys():
        exam_result[language] = {name:points}
        launguage_count[language] = 0
    elif name in exam_result[language]:
        if exam_result[language][name] < points:
            exam_result[language][name] = points
        else:
            launguage_count[language] += 1
            continue
    else:
        exam_result[language][name] = points
    launguage_count[language] += 1


print("Results:")
for cours in exam_result.keys():
    for student, points in exam_result[cours].items():
        print(f'{student} | {points}')
print("Submissions:")
for cours, coursist in launguage_count.items():
    print(f"{cours} - {coursist}")