activation_key = input()

while True:
    command = input()
    if command == "Generate":
        break
    parts = command.split(">>>")
    fonction = parts[0]

    if fonction == "Contains":
        pass
    elif fonction == "Flip":
        pass
    elif fonction == "Slice":
        pass