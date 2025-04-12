activation_key = input()

while True:
    command = input()
    if command == "Generate":
        break
    parts = command.split(">>>")
    fonction = parts[0]

    if fonction == "Contains":
        substring = parts[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif fonction == "Flip":
        up_or_low = parts[1]
        start_index = int(parts[2])
        end_index = int(parts[3]) # inclusive end index
        before = activation_key[:start_index]
        target = activation_key[start_index:end_index]
        after = activation_key[end_index:]

        if up_or_low == "Upper":
            target = target.upper()
        elif up_or_low == "Lower":
            target = target.lower()

        activation_key = (before + target + after)
        print(activation_key)

    elif fonction == "Slice":
        start_index = int(parts[1])
        end_index = int(parts[2])
        before = activation_key[:start_index]
        target = activation_key[start_index:end_index]
        after = activation_key[end_index:]

        activation_key = before + after
        print(activation_key)

print(f"Your activation key is: {activation_key}")