command = input()
phonebook = {}

while "-"  in command:
    name, number = command.split("-")
    phonebook[name] = number

    command = input()

numbers = int(command)

for contact in range(numbers):
    find_contact = input()
    if find_contact in phonebook.keys():
        print(f"{find_contact} -> {phonebook[find_contact]}")
    else:
        print(f"Contact {find_contact} does not exist.")