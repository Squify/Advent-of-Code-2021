with open('example.txt') as f:
    lanternfishs = f.readline().strip().split(',')

map_object = map(int, lanternfishs)
lanternfishs = list(map_object)

print(lanternfishs)

days_to_go = int(input("How many days:"))
for day in range(1, days_to_go + 1):
    new_fish = 0
    for index, fish in enumerate(lanternfishs):
        if fish == 0:
            new_fish += 1
            lanternfishs[index] = 6
        else:
            lanternfishs[index] -= 1

    newborn_fish = [8] * new_fish
    lanternfishs.extend(newborn_fish)

print(len(lanternfishs))
