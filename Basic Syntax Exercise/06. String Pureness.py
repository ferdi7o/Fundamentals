n = int(input())

for _ in range(n):
    check = input()

    if "," in check or "." in check or "_" in check:
        print(f"{check} is not pure!")
    else:
        print(f"{check} is pure.")