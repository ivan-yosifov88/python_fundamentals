worker_produce_biscuits_for_day = int(input())
count_of_workers = int(input())
competing_factory_month_production = int(input())

total_production = 0
production_for_day = worker_produce_biscuits_for_day * count_of_workers
month = 1

while month < 31:
    if month % 3 == 0:
        total_production += int(production_for_day * 0.75)
    else:
        total_production += production_for_day
    month += 1

print(f"You have produced {total_production} biscuits for the past month.")

difference = abs(total_production - competing_factory_month_production)
difference /= competing_factory_month_production
difference *= 100

if total_production > competing_factory_month_production:
    print(f"You produce {difference:.2f} percent more biscuits.")
else:
    print(f"You produce {difference:.2f} percent less biscuits.")

