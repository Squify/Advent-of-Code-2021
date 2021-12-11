numbers = []
numbers_truth = []


def check_if_low_point(number, up=None, right=None, down=None, left=None):
    if up is not None and number >= up:
        return False
    elif right is not None and number >= right:
        return False
    elif down is not None and number >= down:
        return False
    elif left is not None and number >= left:
        return False
    else:
        return True


def basin_size(x, y, numbers):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in numbers]))
    size = 0
    print(x, y)

    for i in range(1, len(numbers[0]) + 1):
        print(x + 1, len(numbers[0]))
        if x + i >= len(numbers[0]):
            continue
        if numbers[y][x + i] < 9:
            size += numbers[y][x + i]
    print(size)
    return size


with open('example.txt') as f:
    for data in f:
        line = []
        line_truth = []
        for i in data:
            if i != '\n':
                line.append(i)
                line_truth.append(False)
        numbers.append(line)
        numbers_truth.append(line_truth)

print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in numbers_truth]))

for index, line in enumerate(numbers):
    map_object = map(int, line)
    numbers[index] = list(map_object)

# print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in numbers]))
risk_level = 0
largest_basins = [1, 1, 1]

for y, line in enumerate(numbers):
    for x, number in enumerate(line):
        up = numbers[y - 1][x] if y > 0 else None
        right = numbers[y][x + 1] if x < len(line) - 1 else None
        down = numbers[y + 1][x] if y < len(numbers) - 1 else None
        left = numbers[y][x - 1] if x > 0 else None
        if check_if_low_point(number, up, right, down, left):
            risk_level = risk_level + 1 + number
            basin_size(x, y, numbers)
            if min(largest_basins) < basin_size(x, y, numbers):
                index_lower = largest_basins.index(min(largest_basins))
                largest_basins[index_lower] = basin_size(x, y, numbers)

print(risk_level)
