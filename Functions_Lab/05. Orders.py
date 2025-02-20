def calculate(product, piecce):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "coke":
        price = 1.40
    elif product == "water":
        price = 1
    elif product == "snacks":
        price = 2
    sum_cals = price * piecce
    return sum_cals

products = input()
quantity = int(input())
result_price = calculate(products, quantity)
print(f'{result_price:.2f}')