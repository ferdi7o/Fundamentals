receive_liters = int(input())

capacity_of_water_tank = 255
use_water = 0

for receive in range(receive_liters):
    liter_receive = int(input())

    if capacity_of_water_tank < liter_receive:
        print("Insufficient capacity!")
    else:
        capacity_of_water_tank -= liter_receive
        use_water += liter_receive

print(use_water)