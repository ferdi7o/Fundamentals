list_of_cards = input().split(", ")
number_of_commands = int(input())

for number in range(1, number_of_commands + 1):
    commands = input().split(", ")
    command, command_1 = commands[0], commands[1]


    if command == "Add":
        if command_1 in list_of_cards:
            print("Card is already in the deck")
        else:
            list_of_cards.append(command_1)
            print("Card successfully added")

    elif command == "Remove":
        if command_1 not in list_of_cards:
            print("Card not found")
        else:
            list_of_cards.remove(command_1)
            print("Card successfully removed")

    elif command == "Remove At":
        index = int(command_1)
        if list_of_cards[index] not in list_of_cards:
            print("Index out of range")
        else:
            list_of_cards.remove(list_of_cards[index])
            print("Card successfully removed")

    elif command == "Insert":
        index = int(command_1)
        card_name = command[2]
        if 0 <= index < len(list_of_cards):
            if list_of_cards[index] not in list_of_cards:
                print("Index out of range")
            elif card_name in list_of_cards:
                print("Card is already added")
            else:
                list_of_cards.insert(index, card_name)
                print("Card successfully added")

print(", ".join(list_of_cards))
