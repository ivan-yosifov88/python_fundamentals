string_particles = input().split("|")

data = input()

while not data == "Done":
    command = data.split()[0]
    if command == "Move":
        new_command = data.split()[1]
        index = data.split()[2]
        index = int(index)
        if new_command == "Left":
            if 0 <= index < len(string_particles) and index - 1 >= 0:
                string_particles[index], string_particles[index - 1] = string_particles[index - 1], string_particles[index]
        elif new_command == "Right":
            if 0 <= index < len(string_particles) and index + 1 < len(string_particles):
                string_particles[index] , string_particles[index + 1] = string_particles[index + 1], string_particles[index]
    elif command == "Check":
        new_command = data.split()[1]
        if new_command == "Even":
            even_elements = [string_particles[i] for i in range(len(string_particles)) if i % 2 == 0]
            print(*even_elements)
        elif new_command == "Odd":
            odd_elements = [string_particles[i] for i in range(len(string_particles)) if not i % 2 == 0]
            print(*odd_elements)
    data = input()

print(f"You crafted {''.join(string_particles)}!")