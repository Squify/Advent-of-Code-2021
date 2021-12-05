with open('input2.txt') as f:
    datas = f.readlines()

horizontal = depth = aim = 0
for data in datas:
    instruction = data.split()
    if instruction[0] == 'down':
        aim += int(instruction[1])

    if instruction[0] == 'up':
        aim -= int(instruction[1])

    if instruction[0] == 'forward':
        horizontal += int(instruction[1])
        depth += aim * int(instruction[1])

print("The horizontal position is", horizontal, "at", depth, "depth. The final result is", horizontal*depth)