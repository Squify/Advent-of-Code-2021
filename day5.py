import numpy as np
from useful_methods import print_matrice

class Coordinates:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def display(self):
        print(self.x1, ";", self.y1, "->", self.x2,";", self.y2)

    def is_horizontal(self):
        if self.x1 == self.x2:
            return True
        return False

    def is_vertical(self):
        if self.y1 == self.y2:
            return True
        return False

    def is_diagonal(self):
        return self.is_horizontal() + self.is_vertical() == 1

    def reverse(self):
        if self.is_horizontal() and self.y2 < self.y1:
            y1 = self.y1
            self.y1 = self.y2
            self.y2 = y1
        elif self.is_vertical() and self.x2 < self.x1:
            x1 = self.x1
            self.x1 = self.x2
            self.x2 = x1


def get_coordinates(line):
    line = line.split()
    start = line[0].split(',')
    end = line[2].split(',')
    coordinates = Coordinates(int(start[0]), int(start[1]), int(end[0]), int(end[1]))
    return coordinates


def count_elements(diagram):
    count = 0
    for line in diagram:
        for i in line:
            if isinstance(i, int):
                if i >= 2:
                    count = count + 1
    print("There's", count, "points with at least two lines overlap")


lines_of_vents = [f.rstrip() for f in open('input5.txt').readlines()]
diagram = np.full([1000, 1000], '.').tolist()

for line in lines_of_vents:
    coordinates = get_coordinates(line)
    if not coordinates.is_diagonal():
        continue
    coordinates.reverse()
    if coordinates.is_horizontal():
        for y in range(coordinates.y1, coordinates.y2 + 1):
            if diagram[y][coordinates.x1] == '.':
                diagram[y][coordinates.x1] = 1
            else:
                diagram[y][coordinates.x1] += 1
    elif coordinates.is_vertical():
        for x in range(coordinates.x1, coordinates.x2 + 1):
            if diagram[coordinates.y1][x] == '.':
                diagram[coordinates.y1][x] = 1
            else:
                diagram[coordinates.y1][x] += 1

count_elements(diagram)
print_matrice(diagram)