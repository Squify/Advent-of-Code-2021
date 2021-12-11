cards = []
cards_truth = []


def check_bingo(card_truth, line, col):
    valid = True
    for i in range(0, len(card_truth[line])):
        if not card_truth[line][i]:
            valid = False
            break

    if valid:
        return True

    for i in range(0, len(card_truth)):
        if not card_truth[i][col]:
            return False

    return True


def compute_points(winner_card, winner_card_truth, last_number):
    points = 0
    for i in range(0, len(winner_card)):
        for j in range(0, len(winner_card[i])):
            if not winner_card_truth[i][j]:
                points = points + winner_card[i][j]
    return points * last_number


def search_winner():
    print(cards_truth)
    for bingo_number in bingo_numbers:
        print("You can check", bingo_number)
        for card_index in range(0, len(cards)):
            card = cards[card_index]
            card_truth = cards_truth[card_index]
            for i in range(0, len(card)):
                line = card[i]
                for j in range(0, len(line)):
                    card_number = line[j]
                    if card_number == int(bingo_number):
                        card_truth[i][j] = True
                        if check_bingo(card_truth, i, j):
                            print("Card number", card_index, "win this bingo with", compute_points(card, card_truth, int(bingo_number)), "points!")
                            return


with open('input4.txt') as f:
    bingo_numbers = f.readline().strip().split(',')
    f.readline()
    card = []
    card_truth = []
    for line in f:
        if line != "\n":
            list1 = line.strip().split()
            map_object = map(int, list1)
            line = list(map_object)
            card.append(line)
            card_truth.append([False] * len(line))
        else:
            cards.append(card)
            cards_truth.append(card_truth)
            card = []
            card_truth = []
    cards.append(card)  # la derniere ligne n'est pas un \n
    cards_truth.append(card_truth)

search_winner()
