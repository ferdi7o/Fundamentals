command = input()
product_and_price = {}

while command != "buy":
    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if product not in product_and_price.keys():
        product_and_price[product] = [quantity, price]
    else:
        product_and_price[product][0] += quantity
        product_and_price[product][1] = price

    command = input()

for key, value in product_and_price.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")