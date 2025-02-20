team_a = []
team_b = []
for num in range(1, 12):
    team_a.append(f'A-{num}')
    team_b.append(f"B-{num}")

comand = input().split()

for check in range(len(comand)):
    if len(team_a) < 7 or len(team_b) < 7:
        break
    if comand[check] not in team_a and comand[check] not in team_b:
        continue
    if comand[check] in team_a:
        team_a.remove(comand[check])
    if comand[check] in team_b:
        team_b.remove(comand[check])

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if len(team_a) < 7 or len(team_b) < 7:
    print("Game was terminated")
