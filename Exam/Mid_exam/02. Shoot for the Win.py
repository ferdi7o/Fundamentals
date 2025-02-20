targets = list(map(int, input().split()))
command = input()
count = 0

while command != "End":
    index = int(command)

    if 0 <= index < len(targets) and targets[index] != -1:
        shot_value = targets[index]
        targets[index] = -1
        count += 1

        for target in range(len(targets)):
            if targets[target] != -1:
                if targets[target] > shot_value:
                    targets[target] -= shot_value
                else:
                    targets[target] += shot_value

    command = input()

print(f"Shot targets: {count} -> {' '.join(map(str, targets))}")