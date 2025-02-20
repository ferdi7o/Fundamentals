my_list = list(map(int, input().split()))
command = input()

while command != "end":
    if command == "decrease":
        my_list = [num - 1 for num in my_list ]

    else:
        comand_parts = command.split()
        comands , index1 , index2 = comand_parts[0], int(comand_parts[1]), int(comand_parts[2])

        if comands == "swap":
            my_list[index1] , my_list[index2] = my_list[index2], my_list[index1]
        else:
            multiply = my_list[index1] * my_list[index2]
            my_list[index1] = multiply


    command = input()

print(", ".join(map(str, my_list)))