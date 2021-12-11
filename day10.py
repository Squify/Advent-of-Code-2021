import math

from useful_methods import *

datas = import_matrice_from_file('input10.txt')
corrupt_points = 0
missing_points = []


def get_excepted(character):
    if character == "(":
        return ")"
    elif character == "{":
        return "}"
    elif character == "[":
        return "]"
    elif character == "<":
        return ">"


def count_missing_points(buffer):
    result = 0
    for character in buffer:
        points = 0
        if character == "(":
            points = 1
        elif character == "[":
            points = 2
        elif character == "{":
            points = 3
        elif character == "<":
            points = 4
        result = result * 5
        result = result + points
    missing_points.append(result)


def count_corrupt_points(character, points):
    if character == ")":
        points += 3
    elif character == "]":
        points += 57
    elif character == "}":
        points += 1197
    elif character == ">":
        points += 25137
    return points


for i, line in enumerate(datas):
    buffer = []
    for j, value in enumerate(line):
        if value == "(" or value == "{" or value == "[" or value == "<":
            buffer.append(value)
        else:
            excepted = get_excepted(buffer[-1])
            if value == excepted:
                buffer.pop()
            else:
                corrupt_points = count_corrupt_points(value, corrupt_points)
                break

        if j == (len(line) - 1):
            buffer.reverse()
            count_missing_points(buffer)

print("Part 1", corrupt_points)

middle_score_missing = (len(missing_points)) / 2
missing_points.sort()
missing_result = missing_points[math.floor(middle_score_missing)]
print("Part 2", missing_result)
