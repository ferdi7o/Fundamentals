# number = input()
# mylist = []
# bigger = []
#
# for num in range(len(number)):
#     mylist.append(int(number[num]))
#
# for big in range(len(mylist)):
#     bigger.append(max(mylist))
#     mylist.remove(max(mylist))
#
# print("".join(map(str,bigger)))

number = input()

bigger = sorted(number, reverse=True)
print("".join(bigger))