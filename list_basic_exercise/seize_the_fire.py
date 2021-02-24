HIGH_FIRE = range(81, 125 + 1)
MEDIUM_FIRE = range(51, 80 + 1)
LOW_FIRE = range(1, 50 + 1)

fires_with_cells = input().split("#")
water_amount = int(input())
cell_value_list = []

for fires in fires_with_cells:
    fire_type, cell_value = fires.split(" = ")
    cell_value = int(cell_value)
    if fire_type == "High" and cell_value not in HIGH_FIRE:
        continue
    elif fire_type == "Medium" and cell_value not in MEDIUM_FIRE:
        continue
    elif fire_type == "Low" and cell_value not in LOW_FIRE:
        continue
    if water_amount - cell_value >= 0:
        water_amount -= cell_value
        cell_value_list.append(cell_value)
print("Cells:")
for values in cell_value_list:
    print(f" - {values}")
print(f"Effort: {(sum(cell_value_list) * 0.25):.2f}")
print(f"Total Fire: {sum(cell_value_list)}")

