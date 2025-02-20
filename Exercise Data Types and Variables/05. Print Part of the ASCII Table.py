char_from = int(input())
char_to = int(input())

for charakter in range(char_from, char_to + 1):
    if charakter == char_to:
        print(chr(charakter))
    else:
        print(chr(charakter), end=" ")