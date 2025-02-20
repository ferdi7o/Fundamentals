waiting_peoples = int(input())
wagons = list(map(int, input().split()))

for index in range(len(wagons)):
    while wagons[index] != 4:
        if waiting_peoples == 0:
            break
        wagons[index] += 1
        waiting_peoples -= 1

if wagons[-1] < 4:
    print('The lift has empty spots!')
    print(" ".join(map(str, wagons)))
elif wagons[-1] == 4 and waiting_peoples > 0:
    print(f"There isn't enough space! {waiting_peoples} people in a queue!")
    print(" ".join(map(str, wagons)))
else:
    print(" ".join(map(str, wagons)))