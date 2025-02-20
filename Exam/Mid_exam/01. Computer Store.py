command = input()
total_price , price_with_texes = 0 , 0
special_discount = 0

def special(price_before_discount):
    special_discount = (price_before_discount * 10) / 100  #10% discount
    return special_discount


while True:
    if command == "special" or command == "regular":
        taxes_price = (total_price * 20) / 100
        price_with_texes = total_price + taxes_price
        if command == "special":
            special_discount = special(price_with_texes)
        break

    price = float(command)
    if price < 0:
        print("Invalid price!")
    else:
        total_price += price

    command = input()

if total_price == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price:.2f}$\n"
          f"Taxes: {taxes_price:.2f}$\n"
          f"-----------\n"
          f"Total price: {price_with_texes - special_discount:.2f}$")