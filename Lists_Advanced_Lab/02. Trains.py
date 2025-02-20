wagon_number = int(input())
wagons = [0] * wagon_number
command = input()

while command != "End":
    action = command.split()[0]
    if action == "add":
        peoples = int(command.split()[1])
        wagons[-1] += peoples
    elif action == "insert":
        index = int(command.split()[1])
        peoples = int(command.split()[2])
        wagons[index] += peoples

    elif action == "leave":
        index = int(command.split()[1])
        peoples = int(command.split()[2])
        wagons[index] -= peoples

    command = input()


print(wagons)
