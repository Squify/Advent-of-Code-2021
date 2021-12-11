with open('input7.txt') as f:
    crabs_positions = f.readline().strip().split(',')
map_object = map(int, crabs_positions)
crabs_positions = list(map_object)

horizontal_positions = {}
for i in range(min(crabs_positions), max(crabs_positions) + 1):
    filtered_positions = filter(lambda position: position == i, crabs_positions)
    how_many_in_this_position = len(list(filtered_positions))
    if how_many_in_this_position > 0:
        horizontal_positions[i] = how_many_in_this_position

fuel_minimum = 0
for position_to_go in range(min(horizontal_positions.keys()), max(horizontal_positions.keys()) + 1):
    fuel = 0
    for position in horizontal_positions:
        calcul = 0
        if position == position_to_go:
            continue
        if position < position_to_go:
            fuel += (position_to_go - position) * horizontal_positions[position]
        elif position > position_to_go:
            fuel += (position - position_to_go) * horizontal_positions[position]
    if fuel > fuel_minimum:
        fuel_minimum = fuel

for position_to_go in range(min(horizontal_positions.keys()), max(horizontal_positions.keys()) + 1):
    fuel = 0
    for position in horizontal_positions:
        calcul = 0
        if position == position_to_go:
            continue
        if position < position_to_go:
            fuel += (position_to_go - position) * horizontal_positions[position]
        elif position > position_to_go:
            fuel += (position - position_to_go) * horizontal_positions[position]
    if fuel < fuel_minimum:
        fuel_minimum = fuel

print("To align to that position, they spend", fuel_minimum, "fuel.")
