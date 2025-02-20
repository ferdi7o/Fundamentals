factor = int(input())
count = int(input())
mylist = []

for number in range(1, count + 1):
    mylist.append(number * factor)

print(mylist)