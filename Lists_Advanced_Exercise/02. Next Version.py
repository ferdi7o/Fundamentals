version = list(map(int, input().split(".")))
version[-1] += 1

for index in range(len(version) -1, -1, -1):
    if version[index] > 9:
        version[index] = 0
        version[index-1] += 1

print(".".join([str(digit) for digit in version]))








# number1, number2, number3 = [int(digit) for digit in input().split(".")]
# number3 += 1
#
# if number3 > 9:
#     number3 = 0
#     number2 += 1
# if number2 > 9:
#     number2 = 0
#     number1 += 1
# if number1 > 9:
#     number1 = 0
#
# print(f"{number1}.{number2}.{number3}")
