rooms = int(input())
game_on = True
free_chairs = 0

for room in range(rooms):
    chars, visitor = input().split()

    if len(chars) < int(visitor):
        print(f"{int(visitor) - len(chars)} more chairs needed in room {room + 1}")
        game_on = False
    else:
        free_chairs += (len(chars) - int(visitor))

if game_on:
    print(f"Game On, {free_chairs} free chairs left")