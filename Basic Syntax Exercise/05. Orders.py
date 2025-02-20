n = int(input())
allprice = 0

for i in range(n):
    price_per_capsul = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 1 > days or 1 > capsules_per_day or 0.01 > price_per_capsul or \
            days > 31 or capsules_per_day > 2000 or price_per_capsul > 100.00:
        continue

    calculasion = (capsules_per_day * days) * price_per_capsul
    allprice += calculasion
    print(f"The price for the coffee is: ${calculasion:.2f}")

print(f"Total: ${allprice:.2f}")