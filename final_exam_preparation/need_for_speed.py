def drive_command(cars, cars_info):
    car, distance_to_go,  needed_fuel = cars_info
    distance_to_go = int(distance_to_go)
    needed_fuel = int(needed_fuel)
    if cars[car]['fuel'] >= needed_fuel:
        cars[car]['fuel'] -= needed_fuel
        cars[car]["mileage"] += distance_to_go
        print(f"{car} driven for {distance_to_go} kilometers. {needed_fuel} liters of fuel consumed.")
    else:
        print("Not enough fuel to make that ride")
    if cars[car]["mileage"] >= 100000:
        print(f"Time to sell the {car}!")
        cars.pop(car)
    return cars


def refuel_command(cars, cars_info):
    car, fuel_to_refuel = cars_info
    fuel_to_refuel = int(fuel_to_refuel)
    if cars[car]['fuel'] + fuel_to_refuel > 75:
        fuel_to_refuel = 75 - cars[car]['fuel']
        cars[car]['fuel'] = 75
    else:
        cars[car]['fuel'] += fuel_to_refuel
    print(f"{car} refueled with {fuel_to_refuel} liters")
    return cars


def revert(cars, cars_info):
    car, kilometers = cars_info
    kilometers = int(kilometers)
    if cars[car]['mileage'] - kilometers < 10000:
        cars[car]['mileage'] = 10000
    else:
        cars[car]['mileage'] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")
    return cars


number_of_cars = int(input())

cars_available = {}
for _ in range(number_of_cars):
    car_model, car_mileage, car_fuel = input().split("|")

    cars_available[car_model] = {'mileage': int(car_mileage), 'fuel': int(car_fuel)}

data = input()

while not data == "Stop":
    command = data.split(" : ")[0]
    # info = data.split(" : ")[1:] judge don't like it this way!

    if command == "Drive":
        info = data.split(" : ")[1:]
        drive_command(cars_available, info)
    elif command == "Refuel":
        info = data.split(" : ")[1:]
        refuel_command(cars_available, info)
    elif command == "Revert":
        info = data.split(" : ")[1:]
        revert(cars_available, info)
    data = input()
if cars_available:
    sorted_cars_available = dict(sorted(cars_available.items(), key=lambda x: (-x[1]['mileage'], x[0])))
    for car in sorted_cars_available:
        print(f"{car} -> Mileage: {sorted_cars_available[car]['mileage']} kms, Fuel in the tank: {sorted_cars_available[car]['fuel']} lt.")

