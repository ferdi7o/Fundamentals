name = input()

while name != "Voldemort":
    haus = ""
    if len(name) < 5:
        haus = "Gryffindor"
    elif len(name) == 5:
        haus = "Slytherin"
    elif len(name) == 6:
        haus = "Ravenclaw"
    else:
        haus = "Hufflepuff"
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    else:
        print(f"{name} goes to {haus}.")
    name = input()

if name == "Voldemort":
    print("You must not speak of that name!")