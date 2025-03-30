my_string = str(input())

while True:
    part_command = input()
    if part_command == "End":
        break
    parts = part_command.split()
    command = parts[0]
    if command == "Translate":
        char = str(parts[1])
        replacement = parts[2]
        my_string = my_string.replace(char, replacement)
        print(my_string)
    elif command == "Includes":
        substring = parts[1]
        if substring in my_string:
            print(True)
        else: print(False)
    elif command == "Start":
        substring = parts[1]
        if substring == my_string[:len(substring)]:
            print(True)
        else: print(False)
    elif command == "Lowercase":
        my_string = my_string.lower()
        print(my_string)
    elif command == "FindIndex":
        char = parts[1]
        index = my_string.rfind(char)
        print(index)
    elif command == "Remove":
        startindex = int(parts[1])
        count = int(parts[2])
        my_string = my_string.replace(my_string[startindex:startindex+count], "")
        print(my_string)