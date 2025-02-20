string_one = input()
string_two = input()
b = 1

for i in range(len(string_one)):
    checking = (string_two[0:i+1] + string_one[b:len(string_one)])
    b += 1