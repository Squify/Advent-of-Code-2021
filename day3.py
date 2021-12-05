with open('input3.txt') as f:
    datas = f.readlines()

# x = 0
# gamma = epsylon = ""
# while x < (len(datas[0]) - 1):
#     zero = one = 0
#     for data in datas:
#         if int(data[x]) == 0:
#             zero += 1
#         if int(data[x]) == 1:
#             one += 1
#     if zero > one:
#         gamma = gamma + '0'
#         epsylon = epsylon + '1'
#     if zero < one:
#         gamma = gamma + '1'
#         epsylon = epsylon + '0'
#     x += 1
#
# gamma = int(gamma, 2)
# epsylon = int(epsylon, 2)
# consumption = gamma*epsylon
#
# print(consumption)


x = 0
generator = datas.copy()
scrubber = datas.copy()
while x < (len(datas[0]) - 1):

    zero = []
    one = []
    for index, data in enumerate(generator):
        if int(data[x]) == 0:
            zero.append(index)
        if int(data[x]) == 1:
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
        print("generator : ", generator)

# ----------------------

    zero = []
    one = []
    for index, data in enumerate(scrubber):
        if int(data[x]) == 0:
            zero.append(index)
        if int(data[x]) == 1:
            one.append(index)

    print(len(scrubber))
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
        print("scrubber : ", scrubber)

    x += 1

print(int(generator[0], 2), int(scrubber[0], 2))
print(int(generator[0], 2) * int(scrubber[0], 2))