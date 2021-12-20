with open('input_files/day_22.txt') as f:
    raw = f.read().strip()


deck_1, deck_2 = raw.split('\n\n')

deck_1 = list(map(int, deck_1.split('\n')[1:]))
deck_2 = list(map(int, deck_2.split('\n')[1:]))

turns = 0
while deck_1 and deck_2:
    card_1 = deck_1.pop(0)
    card_2 = deck_2.pop(0)
    if card_1 > card_2:
        deck_1 += [card_1, card_2]
    else:
        deck_2 += [card_2, card_1]
    turns += 1
    if turns == 100000:
        raise RuntimeError