list_of_string = input().split(" ")
smalles_numbers = int(input())
new_list = []

for number in list_of_string:
    new_list.append(int(number))

for _ in range(smalles_numbers):
    new_list.remove(min(new_list))

print(", ".join(map(str,new_list)))