def changeall(message, old, new):
    message = message.replace(old, new)
    return message

def insert(message, char, index):
    message = (message[:index] + char + message[index:])
    return message

def move(message, chars):
    moved_chars = message[:chars]
    message = message.replace(moved_chars, "")
    message = message + moved_chars
    return message

message = input()

while True:
    command = input()
    if command == "Decode":
        break
    parts = command.split("|")
    process = parts[0]
    if process == "ChangeAll":
        char = parts[1]
        new = parts[2]
        message = changeall(message,char, new)
    elif process == "Insert":
        index = int(parts[1])
        char = parts[2]
        message = insert(message, char, index)
    elif process == "Move":
        chars = int(parts[1])
        message = move(message, chars)

print(f"The decrypted message is: {message}")