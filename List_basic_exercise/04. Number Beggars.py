money_list = input().split(", ")
beggars = int(input())

money_as_string = []
for money in money_list:
    money_as_string.append(int(money))

begarsums = []
start_index = 0
for current_beggar in range(beggars):
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_as_string), beggars):
        current_beggar_sum += money_as_string[current_index]
    begarsums.append(current_beggar_sum)
    start_index += 1

print(begarsums)