all_cars = {}

cars = int(input())
for _ in range(cars):
    car, mileage, fuel = input().split("|")
    all_cars[car] = [int(mileage), int(fuel)]

while True:
    comand = input()
    if comand == "Stop":
        break
    parts = comand.split(" : ")
    options = parts[0]
    car = parts[1]
    if options == "Drive":
        distance = int(parts[2])
        fuel = int(parts[3])
        if all_cars[car][1] >= fuel:
            all_cars[car][1] = all_cars[car][1] - fuel
            all_cars[car][0] = all_cars[car][0] + distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if all_cars[car][0] > 100000:
                print(f"Time to sell the {car}!")
                del all_cars[car]
        else:
            print("Not enough fuel to make that ride")
    elif options == "Refuel":
        fuel = int(parts[2])
        before_refuel = all_cars[car][1]
        all_cars[car][1] += fuel
        if all_cars[car][1] > 75: #max 75 lt.
            need_liters = 75 - before_refuel
            print(f"{car} refueled with {need_liters} liters")
            all_cars[car][1] = 75

        else:
            print(f"{car} refueled with {fuel} liters")
    elif options == "Revert":
        kilometers = int(parts[2])
        all_cars[car][0] -= kilometers
        if all_cars[car][0] < 10000:
            all_cars[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car in all_cars:
    print(f"{car} -> Mileage: {all_cars[car][0]} kms, Fuel in the tank: {all_cars[car][1]} lt.")