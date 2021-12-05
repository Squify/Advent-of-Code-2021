import numpy as np

with open('example.txt') as f:
    bingo_numbers = f.readline()
    datas = f.readlines()

datas.pop(0)
datas.remove("\n")
datas_clean = []
for data in datas:
    datas_clean.append(data.strip())
print((datas_clean))
print(len(datas_clean))
a = (len(datas_clean)-1) / 5
print(a)
matrice = np.zeros((int(a), 5), dtype='int8')
matrice2 = []
print(matrice)
m = -1
for index, data in enumerate(datas_clean):
    if index%5 == 0:
        m += 1

    list1 = data.split()
    map_object = map(int, list1)
    list2 = list(map_object)
    matrice2.append([[list2]])

    # matrice[index][m].append(list2)

print(matrice2)
# matrice[index] = list2
# print(matrice)
# print(index, index%5)


# a_string = "1 2 3"
# a_list = a_string.split()
# map_object = map(int, a_list)
#
# list_of_integers = list(map_object)
# print(list_of_integers)
