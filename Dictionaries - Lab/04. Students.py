data = input()
student_dic = {}

while ":" in data:
    name, number, cours = data.split(":")

    if cours not in student_dic.keys():
        student_dic[cours] = {number: name}
    else:
        student_dic[cours][number] = name


    data = input()

data = data.replace("_", " ")
for stutent, id in student_dic[data].items():
    print(f"{id} - {stutent}")