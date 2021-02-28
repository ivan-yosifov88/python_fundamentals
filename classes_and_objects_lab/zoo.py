class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.zoo_name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
number_of_animals = int(input())
for animals in range(number_of_animals):
    animals, specie = input().split()
    zoo.add_animal(animals, specie)

species = input()

print(zoo.get_info(species))