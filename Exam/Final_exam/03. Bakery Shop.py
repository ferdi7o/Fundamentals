def receive(piece, food):
    if piece <= 0:
        return
    if food not in foods:
        foods[food] = piece
    else:
        foods[food] += piece

def sell(piece, food, sells):
    if food not in foods:
        print(f"You do not have any {food}.")
    elif foods[food] < piece:
        print(f"There aren't enough {food}. You sold the last {foods[food]} of them.")
        sells += foods[food]
        del foods[food]
    else:
        print(f"You sold {piece} {food}.")
        foods[food] -= piece
        sells += piece
        if foods[food] == 0:
            del foods[food]
    return sells

sell_quantity = 0
foods = {}
while True:
    command = input()
    if command == "Complete":
        break
    process, quantity, food = command.split()
    quantity = int(quantity)
    if process == "Receive":
        receive(quantity, food)
    elif process == "Sell":
        sell_quantity = sell(quantity, food, sell_quantity)

for key, value in foods.items():
    print(f"{key}: {value}")
print(f"All sold: {sell_quantity} goods")