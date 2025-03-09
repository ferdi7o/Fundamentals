text_1, text_2 = input().split()
all_sum = 0

if len(text_1) > len(text_2):
    for index in range(len(text_2)):
        char1 = text_1[index]
        char2 = text_2[index]
        calculate = ord(char1) * ord(char2)
        all_sum += calculate
    for add in range(len(text_2), len(text_1)):
        all_sum += ord(text_1[add])

elif len(text_1) < len(text_2):
    for index in range(len(text_1)):
        calculate = ord(text_1[index]) * ord(text_2[index])
        all_sum += calculate
    for add in range(len(text_1), len(text_2)):
        all_sum += ord(text_2[add])
else:
    for index in range(len(text_1)):
        calculate = ord(text_1[index]) * ord(text_2[index])
        all_sum += calculate

print(all_sum)