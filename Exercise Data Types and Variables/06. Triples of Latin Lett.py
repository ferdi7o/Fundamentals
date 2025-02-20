number = int(input())

for i in range(97, 97 + number):
    for j in range(97, 97 + number):
        for k in range(97, 97 + number):

            print(chr(i) + chr(j) + chr(k))
