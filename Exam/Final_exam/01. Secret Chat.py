message = input()

while True:
    command = input()
    if command == "Reveal":
        break
    parts = command.split(":|:")
    instruction = parts[0]
    if instruction == "InsertSpace":
        index = int(parts[1])
        message = (message[:index] + " " + message[index:])
    elif instruction == "Reverse":
        substring = parts[1]
        if substring not in message:
            print("error")
            continue
        else:
            message = message.replace(substring, "")
            message = message + (substring[::-1])
    elif instruction == "ChangeAll":
        substring = parts[1]
        replacement = parts[2]
        message = message.replace(substring, replacement)
    print(message)

print(f"You have a new text message: {message}")