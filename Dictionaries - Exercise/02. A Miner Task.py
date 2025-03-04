command = input()
jewels = {}

while command != "stop":
    quantity = int(input())
    if command not in jewels.keys():
        jewels[command] = quantity
    else:
        jewels[command] += quantity

    command = input()

for resource, quantity in jewels.items():
    print(f"{resource} -> {quantity}")