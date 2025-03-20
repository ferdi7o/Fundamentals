import re

command = input()
pattern = r">>([A-Za-z]+)<<(\d+(\.\d+)?)!(\d+)"
total_price = 0
items = []

while command != "Purchase":
    matches = re.search(pattern, command)
    if matches:
        price = float(matches[2])
        piece = int(matches[4])
        item = matches[1]

        items.append(item)
        total_price += (price * piece)

    command = input()

print("Bought furniture:")
for item in items:
    print(f"{item}")
print(f"Total money spend: {total_price:.2f}")