data = input()
dict = {}

while data != "statistics":
    comand = data.split(": ")

    key = comand[0]
    value = int(comand[1])
    if key in dict.keys():
        dict[key] += value
    else:
       dict[key] = value

    data = input()


print("Products in stock:")
for product, quantity in dict.items():
    print(f"- {product}: {quantity}")
# [print(f"- {product}: {quantity}") for (product, quantity) in dict]
print(f"Total Products: {len(dict.keys())}")
print(f"Total Quantity: {sum(dict.values())}")
