with open('example.txt') as f:
    formula = f.readline().strip().split(',')[0]
    f.readline()
    pair_insertions = f.readlines()

print(formula)
steps = int(input("How many steps:"))
for step in range(0, steps):
    pairs = pair_insertions.copy()
    for formula_pair in range(0, len(formula)):
        pair_split = pairs[0].split()
        if formula[formula_pair] == pair_split[0][0]:
            if formula[formula_pair + 1] == pair_split[0][1]:
                print(formula, formula[formula_pair], formula[formula_pair + 1])
                print(formula[:(formula_pair + 1)], formula[(formula_pair + 1):])
                print(pair_split[2])
                formula = formula[:(formula_pair + 1)] + pair_split[2] + formula[(formula_pair + 1):]
                print(formula)
                print("----")
                print()
                formula_pair += 1
print(formula)
