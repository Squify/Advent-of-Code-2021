with open('input1.txt') as f:
    datas = f.readlines()

larger_counter = 0
previous_data = None
for index, data in enumerate(datas):
    if index > 0:
        previous_data = int(datas[index - 1])
        if int(data) > previous_data:
            larger_counter += 1

larger_counter = 0
previous_data = int(datas[0])
for data in datas:
    if int(data) > previous_data:
        larger_counter += 1
    previous_data = int(data)

print(larger_counter)




# with open('example.txt') as f:
#     datas = f.readlines()

previous_sum = None
larger_counter_sum = 0
for index, data in enumerate(datas):
    if index >= 2:
        a = int(datas[index - 2])
        b = int(datas[index - 1])
        c = int(datas[index])
        sum = a + b + c

        if previous_sum is not None:
            if sum > previous_sum:
                larger_counter_sum += 1
        previous_sum = int(sum)

print(larger_counter_sum)
