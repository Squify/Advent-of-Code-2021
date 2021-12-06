with open('input6.txt') as f:
    lanternfishs = f.readline().strip().split(',')


def get_timers(lanternfishs):
    return {
        "8": len(list(filter(lambda timer: timer == 8, lanternfishs))),
        "7": len(list(filter(lambda timer: timer == 7, lanternfishs))),
        "6": len(list(filter(lambda timer: timer == 6, lanternfishs))),
        "5": len(list(filter(lambda timer: timer == 5, lanternfishs))),
        "4": len(list(filter(lambda timer: timer == 4, lanternfishs))),
        "3": len(list(filter(lambda timer: timer == 3, lanternfishs))),
        "2": len(list(filter(lambda timer: timer == 2, lanternfishs))),
        "1": len(list(filter(lambda timer: timer == 1, lanternfishs))),
        "0": len(list(filter(lambda timer: timer == 0, lanternfishs))),
    }


def sum_of_fishs(lanternfishs):
    total = 0
    for i in range(0, 9):
        total += lanternfishs[str(i)]
    return total


map_object = map(int, lanternfishs)
lanternfishs = list(map_object)

days_to_go = int(input("How many days:"))

timers = get_timers(lanternfishs)
for day in range(1, days_to_go + 1):
    timers_2 = get_timers(lanternfishs)
    new_fishs = timers['0']
    for i in range(0, 8):
        timers_2[str(i)] = timers[str(i + 1)]
    timers_2['6'] = timers['7'] + new_fishs
    timers_2['8'] = new_fishs
    timers = timers_2

    print("There's", sum_of_fishs(timers), "lanternfishs on day", day)
