number = int(input())
registered = {}

for num in range(number):
    command = input().split()
    process = command[0]
    name = command[1]

    if process == "register":
        plate_number = command[2]
        if name not in registered.keys():
            registered[name] = plate_number
            print(f"{name} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {registered[name]}")
    elif process == "unregister":
        if name not in registered.keys():
            print(f"ERROR: user {name} not found")
        else:
            del registered[name]
            print(f"{name} unregistered successfully")

for username, license_plate_number in registered.items():
    print(f"{username} => {license_plate_number}")