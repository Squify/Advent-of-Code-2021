with open('example.txt') as f:
    crabs_positions = f.readline().strip().split(',')
map_object = map(int, crabs_positions)
crabs_positions = list(map_object)

# print(crabs_positions)
# print(max(crabs_positions))

horizontal_positions = {}
for i in range(min(crabs_positions), max(crabs_positions) + 1):
    filtered_positions = filter(lambda position: position == i, crabs_positions)
    how_many_in_this_position = len(list(filtered_positions))
    if how_many_in_this_position > 0:
        horizontal_positions[i] = how_many_in_this_position

print(horizontal_positions)
print(horizontal_positions.items())

average_of_position = sum(horizontal_positions.keys()) / len(horizontal_positions)
print(sum(horizontal_positions.keys()))
print(len(horizontal_positions))
print(average_of_position)
nearest_index_with_this_position = min(horizontal_positions, key=lambda x: abs(x - average_of_position))
positions = {}




positions[a] = horizontal_positions[a]
positions[nearest_index_with_this_position] = horizontal_positions[nearest_index_with_this_position]
positions[b] = horizontal_positions[b]







print(positions)

# print(positions)
ideal_position = max(positions, key=positions.get)

fuel = 0
for position in horizontal_positions:
    # print(position)
    # difference index ideal * values
    consumption = abs(position - ideal_position) * horizontal_positions[position]
    # print(consumption)
    fuel += consumption
print(fuel)
