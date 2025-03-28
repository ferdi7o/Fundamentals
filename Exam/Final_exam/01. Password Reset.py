password = input()


while True:
    command = input()
    if command == "Done":
        break
    parts = command.split()
    mod = parts[0]
    if mod == "TakeOdd":
        new_password = ""
        for odd in range(len(password)):
            if odd % 2 == 0:
                continue
            else:
                new_password += password[odd]
        print(new_password)
        password = new_password
    elif mod == "Cut":
        index = int(parts[1])
        lenght = int(parts[2])
        password = password[:index] + password[(index+lenght):]
        print(password)
    elif mod == "Substitute":
        substring = parts[1]
        substitute = parts[2]
        if substring not in password:
            print("Nothing to replace!")
        else:
            password = password.replace(substring, substitute)
            print(password)

print(f"Your password is: {password}")