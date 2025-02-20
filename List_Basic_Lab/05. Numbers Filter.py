number = int(input())
number_list = []
filtered_list = []

for _ in range(number):
    new_number = int(input())
    number_list.append(new_number)

comand = input()

if comand == "even":
    for check in number_list:
        if check % 2 == 0:
            filtered_list.append(check)
elif comand == "odd":
    for check in number_list:
        if check % 2 != 0:
            filtered_list.append(check)
elif comand == "negative":
    for check in number_list:
        if check < 0:
            filtered_list.append(check)
elif comand == "positive":
    for check in number_list:
        if check >= 0:
            filtered_list.append(check)

print(filtered_list)