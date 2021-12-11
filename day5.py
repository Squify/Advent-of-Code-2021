import numpy as np


class Coordinates:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def display(self):
        print(self.x1, ";", self.y1, "->", self.x2, ";", self.y2)

    def is_horizontal(self):
        return self.x1 == self.x2

    def is_vertical(self):
        return self.y1 == self.y2

    def is_diagonal(self):
        if self.is_horizontal() + self.is_vertical() == 0:
            if self.x2 > self.x1:
                x1 = self.x1
                y1 = self.y1

                self.x1 = self.x2
                self.y1 = self.y2

                self.x2 = x1
                self.y2 = y1
            return True
        return False

    def reverse_if_necessary(self):
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
# print_matrice(diagram)

for line in lines_of_vents:
    coordinates = get_coordinates(line)
    if coordinates.is_diagonal():
        y_ = coordinates.y2 - coordinates.y1
        x_ = coordinates.x2 - coordinates.x1
        if y_ < 0 and x_ < 0:
            for i, j in zip(range(0, -(y_) + 1), range(0, -(x_) + 1)):
                if diagram[coordinates.y1 - i][coordinates.x1 - j] == '.':
                    diagram[coordinates.y1 - i][coordinates.x1 - j] = 1
                else:
                    diagram[coordinates.y1 - i][coordinates.x1 - j] += 1

        elif y_ < 0 and x_ > 0:
            for i, j in zip(range(0, -(y_) + 1), range(0, x_ + 1)):
                if diagram[coordinates.y1 - i][coordinates.x1 + j] == '.':
                    diagram[coordinates.y1 - i][coordinates.x1 + j] = 1
                else:
                    diagram[coordinates.y1 - i][coordinates.x1 + j] += 1

        elif y_ > 0 and x_ < 0:
            for i, j in zip(range(0, y_ + 1), range(0, -(x_) + 1)):
                if diagram[coordinates.y1 + i][coordinates.x1 - j] == '.':
                    diagram[coordinates.y1 + i][coordinates.x1 - j] = 1
                else:
                    diagram[coordinates.y1 + i][coordinates.x1 - j] += 1

        elif y_ > 0 and x_ > 0:
            for i, j in zip(range(0, y_ + 1), range(0, x_ + 1)):
                if diagram[coordinates.y1 + i][coordinates.x1 + j] == '.':
                    diagram[coordinates.y1 + i][coordinates.x1 + j] = 1
                else:
                    diagram[coordinates.y1 + i][coordinates.x1 + j] += 1
        continue
    coordinates.reverse_if_necessary()
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
# print_matrice(diagram)
