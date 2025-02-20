budget = int(input())
shopping = 0

while budget >= shopping:
    shop = input()
    if shop == "End":
        break
    shopping += int(shop)

if budget >= shopping:
    print("You bought everything needed.")
else:
    print("You went in overdraft!")