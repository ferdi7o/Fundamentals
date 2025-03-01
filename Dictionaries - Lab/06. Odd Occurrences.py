data = input().lower().split()
dic = {}

for el in data:
    if el not in dic.keys():
        dic[el] = 1
    else:
        dic[el] += 1

for key, value in dic.items():
    if value % 2 != 0:
        print(key, end=" ")