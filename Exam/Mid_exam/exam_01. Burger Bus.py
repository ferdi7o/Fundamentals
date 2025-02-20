cities = int(input())
total_income = 0

for city in range(1, cities + 1):
    city_name = input()
    income = float(input())
    expenses = float(input())
    special_event, losses_money = 0 , 0

    if city % 3 == 0 and city % 5 != 0:
        special_event = expenses / 2

    if city % 5 == 0:
        losses_money = (income * 10) / 100

    calculasion = income - (expenses + special_event + losses_money)
    total_income += calculasion
    print(f"In {city_name} Burger Bus earned {calculasion:.2f} leva.")


print(f"Burger Bus total profit: {total_income:.2f} leva.")