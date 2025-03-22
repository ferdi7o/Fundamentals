validname = input()

while True:
    command = input()
    if command == "Registration":
        break

    parts = command.split()
    procces = parts[0]
    chars = parts[1]

    if procces == "Letters":
        if chars == "Lower":
            validname = validname.lower()
            print(validname)
        else:
            validname = validname.upper()
            print(validname)
    elif procces == "Reverse":
        start_index = int(parts[1])
        end_index = int(parts[2])
        if start_index >= 0 and len(validname) >= end_index:
            new_name = validname[start_index:end_index + 1]
            print(new_name[::-1])
        else:
            continue
    elif procces == "Substring":
        if chars in validname:
            validname = validname.replace(chars, "")
            print(validname)
        else:
            print(f"The username {validname} doesn't contain {chars}.")
    elif procces == "Replace":
        for _ in range(len(validname)):
            if chars in validname:
                validname = validname.replace(chars, "-")
        print(validname)
    elif procces == "IsValid":
        if chars in validname:
            print("Valid username.")
        else:
            print(f"{chars} must be contained in your username.")
    else:
        print("ERROR!")