groups = int(input())
days = int(input())
coins = 0

for day in range(1, days +1):
    if day % 15 == 0:
        groups += 5
    if day % 10 == 0:
        groups -= 2
    if day % 5 == 0:
        coins += 20 * groups
        if day % 3 == 0:
            coins -= 2 * groups
    if day % 3 == 0:
        coins -= 3 * groups
    coins += 50
    coins -= 2 * groups

calculation = coins // groups
print(f"{groups} companions received {calculation} coins each.")