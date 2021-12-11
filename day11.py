from useful_methods import print_matrice, import_truth_matrice_from_file, reset_truth

with open('input11.txt') as f:
    octopuses, octopuses_truth = import_truth_matrice_from_file(f)
print_matrice(octopuses)
width = len(octopuses[0])
height = len(octopuses)
octopus_number = width * height
flashes = 0


def increase_energy(y, x, octopuses):
    octopuses[y][x] += 1
    if octopuses[y][x] == 10:
        octopuses[y][x] = 0
        if octopuses_truth[y][x] == 0:
            increment_adjacent(y, x, octopuses)
            octopuses_truth[y][x] += 1


def increment_adjacent(y, x, octopuses):
    for i in range(-1, 2):
        for j in range(-1, 2):
            y_i = y + i
            x_j = x + j
            if 0 <= y_i < height and 0 <= x_j < width:
                if i != 0 or j != 0:
                    increase_energy(y_i, x_j, octopuses)


#steps = int(input("How many steps:"))
#for i in range(0, steps):
for i in range(0, 99999999999999):
    step_flashes = 0
    for y, line in enumerate(octopuses):
        for x, value in enumerate(line):
            increase_energy(y, x, octopuses)
    for y, line in enumerate(octopuses_truth):
        for x, value in enumerate(line):
            if value != 0:
                flashes += 1
                step_flashes += 1
                octopuses[y][x] = 0
    if step_flashes == octopus_number:
        print("All the octopus flashes as the same time step", i + 1)
        exit()
    reset_truth(octopuses_truth, 0)

print("Octopuses flashs", flashes, "times.")
