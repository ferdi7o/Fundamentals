list_one = input().split(", ")
list_two = input().split(", ")

land_and_city = dict(zip(list_one, list_two))

for country, capital in land_and_city.items():
    print(f"{country} -> {capital}")