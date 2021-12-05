# PART 1 ----------------------
with open('input3.txt') as f:
    datas = f.readlines()

gamma = epsylon = ''
for i in range(len(datas[0]) - 1):
    zero = one = 0
    for data in datas:
        if int(data[i]) == 0:
            zero += 1
        if int(data[i]) == 1:
            one += 1
    if zero > one:
        gamma = gamma + '0'
        epsylon = epsylon + '1'
    if zero < one:
        gamma = gamma + '1'
        epsylon = epsylon + '0'

gamma = int(gamma, 2)
epsylon = int(epsylon, 2)
consumption = gamma * epsylon

print("The power consumption of the submarinec is about", consumption)

# PART 2 ----------------------
generator = datas.copy()
scrubber = datas.copy()
for i in range(len(datas[0]) - 1):
    zero = []
    one = []
    for index, data in enumerate(generator):
        if int(data[i]) == 0:
            zero.append(index)
        if int(data[i]) == 1:
            one.append(index)

    if len(generator) > 1:
        zero.reverse()
        one.reverse()
        if len(zero) == len(one):
            for j in zero:
                generator.pop(j)
        elif len(zero) > len(one):
            for j in one:
                generator.pop(j)
        elif len(zero) < len(one):
            for j in zero:
                generator.pop(j)

    # ----------------------

    zero = []
    one = []
    for index, data in enumerate(scrubber):
        if int(data[i]) == 0:
            zero.append(index)
        if int(data[i]) == 1:
            one.append(index)

    if len(scrubber) > 1:
        zero.reverse()
        one.reverse()
        if len(zero) == len(one):
            for j in one:
                scrubber.pop(j)
        elif len(zero) < len(one):
            for j in one:
                scrubber.pop(j)
        elif len(zero) > len(one):
            for j in zero:
                scrubber.pop(j)

print("The life support rating of the submarine is about", int(generator[0], 2) * int(scrubber[0], 2))
