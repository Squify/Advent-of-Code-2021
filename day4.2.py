m = []

with open('example.txt') as f:
    bingo_numbers = f.readline().strip().split(',')
    f.readline()
    n = []
    for index, line in enumerate(f):
        if line != "\n":
            list1 = line.strip().split()
            map_object = map(int, list1)
            list2 = list(map_object)
            n.append(list2)

        if line == "\n":
            m.append(n)
            n = []
    m.append(n)

print(m)

copy_okaou = m.copy()
matrice_index = 0
for number in bingo_numbers:
    if matrice_index < len(m):
        for line in m[matrice_index]:
            print(int(number) in line)
        matrice_index += 1
    matrice_index = 0


m2 = []
matrice_index = 0
if matrice_index < len(m):
    for index, line in enumerate(m[matrice_index]):
        n = []


        m2[matrice_index]




# 1- boucler sur les nombres du bingo_numbers
# 2- regarder dans chaque matrice si ya le nombre
# 3- si ya le nombre on mets un X
# 4- on vérifie si ya une ligne complète qqpart



























