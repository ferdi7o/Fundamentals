energy = int(input())
distance = input()
win_counter = 0


while distance != "End of battle":
    distance = int(distance)
    if energy >= distance:
        energy -= distance
        win_counter += 1
        if win_counter % 3 == 0:
            energy += win_counter
    else:
        print(f"Not enough energy! Game ends with {win_counter} won battles and {energy} energy")
        break

    distance = input()

if distance == "End of battle":
    print(f"Won battles: {win_counter}. Energy left: {energy}")