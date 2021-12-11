def print_matrice(m):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in m]))


def map_matrice_str_to_int(m):
    for index, line in enumerate(m):
        map_object = map(int, line)
        m[index] = list(map_object)
    return m


def import_matrice_from_file(f):
    matrice = []
    for data in f:
        line = []
        for i in data:
            if i != '\n':
                line.append(i)
        matrice.append(line)
    return map_matrice_str_to_int(matrice)


def import_truth_matrice_from_file(f):
    matrice = []
    truth_matrice = []
    for data in f:
        line = []
        line_truth = []
        for i in data:
            if i != '\n':
                line.append(i)
                line_truth.append(0)
        matrice.append(line)
        truth_matrice.append(line_truth)
    return map_matrice_str_to_int(matrice), truth_matrice


def reset_truth(m, default):
    for line in m:
        for index, value in enumerate(line):
            line[index] = default
