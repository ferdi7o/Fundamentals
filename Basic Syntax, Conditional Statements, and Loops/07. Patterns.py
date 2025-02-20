# parrent = int(input())
#
# for i in range(1, parrent + 1, 1):
#     print(i * "*")
# for j in range(parrent - 1, 0, -1):
#     print(j * "*")

# Mario Github project Patterns


w = int(input())
h = int(input())

for i in range(h):
    if i == 0 or i == (h - 1):
        print("*" * w)
    else:
        print("*" + " " * (w - 2) + "*")