number_list = list(map(int, input().split()))
command = input()

while command != "Finish":
    commands = command.split()
    read_comand , read_value = commands[0], int(commands[1])

    if read_comand == "Add":
        number_list.append(read_value)
    elif read_comand == "Remove":
        if read_value in number_list:
            number_list.remove(read_value)
    elif read_comand == "Replace":
        replace = int(commands[2])
        if read_value in number_list:
            index = number_list.index(read_value)
            number_list[index] = replace
    elif read_comand == "Collapse":
        number_list = [num for num in number_list if num >= read_value]

    command = input()

print(" ".join(map(str, number_list)))