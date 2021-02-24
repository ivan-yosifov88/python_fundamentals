population_wealth = [int(number) for number in input().split(", ")]
minimum_wealth = int(input())
average_wealth = sum(population_wealth) // len(population_wealth)
total_wealth = sum(population_wealth)
if average_wealth >= minimum_wealth:
    difference = 0
    for index in range(len(population_wealth)):
        if population_wealth[index] < minimum_wealth:
            difference = minimum_wealth - population_wealth[index]
            population_wealth[population_wealth.index(max(population_wealth))] -= difference
            population_wealth[index] += difference
    print(population_wealth)
else:
    print("No equal distribution possible")
