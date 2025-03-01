number = int(input())
dic = {}

for _ in range(number):
    word = input()
    synonym = input()

    if word not in dic.keys():
        dic[word] = []

    dic[word].append(synonym)


for key in dic:
    print(f"{key} - {', '.join(dic[key])}")
