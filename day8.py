digits = {
    0: 0, #0 : abcefg / 6
    1: 0, #1 : cf // 2
    2: 0, #2 : acdeg / 5
    3: 0, #3 : acdfg / 5
    4: 0, #4 : bcdf // 4
    5: 0, #5 : abdfg / 5
    6: 0, #6 : abdefg / 6
    7: 0, #7 : acf // 3
    8: 0, #8 : abcdefg // 7
    9: 0  #9 : abcdfg / 6
}

signal_patterns = []
outputs = []

with open('example.txt') as f:
    lines = f.readlines()
    for line in lines:
        datas = line.strip().split('|')
        signal_patterns.append(datas[0].split())
        outputs.append(datas[1].split())

for output in outputs:
    for value in output:
        if len(value) == 2:
            digits[1] = digits[1] + 1
        elif len(value) == 4:
            digits[4] += 1
        elif len(value) == 3:
            digits[7] += 1
        elif len(value) == 7:
            digits[8] += 1
        else:
            continue

print("Part 1:")
print("There's", digits[1] + digits[4] + digits[7] + digits[8], "simple digits")

# ------------------

digits_correspondances = {
    'a': '',
    'b': '',
    'c': '',
    'd': '',
    'e': '',
    'f': '',
    'g': ''
}

numbers = {
    'a': '',
    'b': '',
    'c': '',
    'd': '',
    'e': '',
    'f': '',
    'g': ''
}


def set_correspondances(datas):
    for data in datas:
        if len(data) == 2:
            digits_correspondances['c'] = data[0]
            digits_correspondances['f'] = data[1]
        if len(data) == 4:
            digits_correspondances['b'] = data[0]
            digits_correspondances['c'] = data[1]
            digits_correspondances['d'] = data[2]
            digits_correspondances['f'] = data[3]
        if len(data) == 3:
            digits_correspondances['a'] = data[0]
            digits_correspondances['c'] = data[1]
            digits_correspondances['f'] = data[2]
        if len(data) == 7:
            digits_correspondances['a'] = data[0]
            digits_correspondances['b'] = data[1]
            digits_correspondances['c'] = data[2]
            digits_correspondances['d'] = data[3]
            digits_correspondances['e'] = data[4]
            digits_correspondances['f'] = data[5]
            digits_correspondances['g'] = data[6]
    return digits_correspondances


def set_numbers(c):
    digits[0] = c['a'] + c['b'] + c['c'] + c['d'] + c['e'] + c['g']
    digits[1] = c['c'] + c['f']
    digits[2] = c['a'] + c['c'] + c['d'] + c['e'] + c['g']
    digits[3] = c['a'] + c['c'] + c['d'] + c['f'] + c['g']
    digits[4] = c['b'] + c['c'] + c['d'] + c['f'] 
    digits[5] = c['a'] + c['b'] + c['d'] + c['f'] + c['g']
    digits[6] = c['a'] + c['b'] + c['d'] + c['e'] + c['f'] + c['g']
    digits[7] = c['a'] + c['c'] + c['g']
    digits[8] = c['a'] + c['b'] + c['c'] + c['d'] + c['e'] + c['f'] + c['g']
    digits[9] = c['a'] + c['b'] + c['c'] + c['d'] + c['f'] + c['g']
    return digits

print(outputs)
for index_output, output in enumerate(outputs):
    print('output:', output)
    for index, value in enumerate(output):
        print('index:', index, 'value', value)
        sorted_value = sorted(value)
        outputs[index_output][index] = ''.join(sorted_value)
print(outputs)

digits_values = []
for index, output in enumerate(outputs):
    digits_correspondances = set_correspondances(signal_patterns[index])
    print(digits_correspondances)
    numbers_correspondances = set_numbers(digits_correspondances)
    print(numbers_correspondances)

    number_to_decode = ''
    for value in output:
        if value == numbers_correspondances[0]:
            number_to_decode += '0'
        if len(value) == 2:
            number_to_decode += '1' #ok
        if value == numbers_correspondances[2]:
            number_to_decode += '2'
        if value == numbers_correspondances[3]:
            number_to_decode += '3'
        if len(value) == 4:
            number_to_decode += '4' #ok
        if value == numbers_correspondances[5]:
            number_to_decode += '5'
        if value == numbers_correspondances[6]:
            number_to_decode += '6'
        if len(value) == 3:
            number_to_decode += '7' #ok
        if len(value) == 7:
            number_to_decode += '8' #ok
        if value == numbers_correspondances[9]:
            number_to_decode += '9'
    print('Digits are', number_to_decode)
    digits_values.append(number_to_decode)

map_object = map(int, digits_values)
digits_values = list(map_object)
print("Part 2:")
print("The output is", sum(digits_values)) #sum(digits_values)