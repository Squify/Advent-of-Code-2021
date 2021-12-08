with open('input7.txt') as f:
    crabs_positions = f.readline().strip().split(',')
map_object = map(int, crabs_positions)
crabs_positions = list(map_object)

def compute_fuel_p2(mouvments):
    result = 0
    for i in range(1, mouvments + 1):
        result = result + i
    return result


horizontal_positions = {}
for i in range(min(crabs_positions), max(crabs_positions) + 1):
    filtered_positions = filter(lambda position: position == i, crabs_positions)
    how_many_in_this_position = len(list(filtered_positions))
    if how_many_in_this_position > 0:
        horizontal_positions[i] = how_many_in_this_position

fuel_minimum = 0
#for position_to_go in horizontal_positions:
for position_to_go in range(min(horizontal_positions.keys()), max(horizontal_positions.keys()) + 1):
    fuel = 0
    for position in horizontal_positions:
        calcul = 0
        if position == position_to_go:
            continue
        if position < position_to_go:
            #print("calcul", position_to_go, "-", position, "is", position_to_go - position, "*", horizontal_positions[position], "=", (position_to_go - position) * horizontal_positions[position])
            calcul = (position_to_go - position)
            result = 0
            for i in range(1, calcul+1):
                result = result + i
            fuel += compute_fuel_p2(calcul) * horizontal_positions[position]
        elif position > position_to_go:
            #print("calcul", position, "-", position_to_go, "is", position - position_to_go, "*", horizontal_positions[position], "=", (position_to_go - position) * horizontal_positions[position])
            calcul = (position - position_to_go)
            result = 0
            for i in range(1, calcul+1):
                result = result + i
            fuel += compute_fuel_p2(calcul) * horizontal_positions[position]
        #print("Trying to go", position_to_go, "with", position, "equal:", calcul)
    if fuel > fuel_minimum:
        fuel_minimum = fuel

#for position_to_go in horizontal_positions:
for position_to_go in range(min(horizontal_positions.keys()), max(horizontal_positions.keys()) + 1):
    fuel = 0
    for position in horizontal_positions:
        calcul = 0
        if position == position_to_go:
            continue
        if position < position_to_go:
            #print("calcul", position_to_go, "-", position, "is", position_to_go - position, "*", horizontal_positions[position], "=", (position_to_go - position) * horizontal_positions[position])
            calcul = (position_to_go - position)
            result = 0
            for i in range(1, calcul+1):
                result = result + i
            fuel += compute_fuel_p2(calcul) * horizontal_positions[position]
        elif position > position_to_go:
            #print("calcul", position, "-", position_to_go, "is", position - position_to_go, "*", horizontal_positions[position], "=", (position_to_go - position) * horizontal_positions[position])
            calcul = (position - position_to_go)
            result = 0
            for i in range(1, calcul+1):
                result = result + i
            fuel += compute_fuel_p2(calcul) * horizontal_positions[position]
            #fuel += compute_fuel_p2(calcul) * horizontal_positions[position]
        #print("Trying to go", position_to_go, "with", position, "equal:", compute_fuel_p2(calcul))
        #print(calcul)
    print("result", fuel)
    if fuel < fuel_minimum:
        fuel_minimum = fuel

print("final",fuel_minimum)
