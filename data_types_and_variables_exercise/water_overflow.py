number_of_fill = int(input())
water_tank_capacity = 255
added_liters_in_tank = 0
for fill in range(number_of_fill):
    amount_of_water = int(input())
    added_liters_in_tank += amount_of_water
    if added_liters_in_tank > water_tank_capacity:
        added_liters_in_tank -= amount_of_water
        print("Insufficient capacity!")
print(added_liters_in_tank)
