import collections

from utilities import load_data


YEAR = 2021
DAY = 21
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()
p1_loc = int(input_data[0][-1])
p2_loc = int(input_data[1][-1])


def simulate(p1_loc, p2_loc):
    rolls = 0
    die = 1
    p1_score = 0
    p2_score = 0
    turn = 1
    while True:
        turn += 1
        for _ in range(3):
            p1_loc += die
            rolls += 1
            die += 1
            while p1_loc > 10:
                p1_loc -= 10
            while die > 100:
                die -= 100
        p1_score += p1_loc
        if p1_score >= 1000:
            return p2_score * rolls
        for _ in range(3):
            p2_loc += die
            rolls += 1
            die += 1
            while p2_loc > 10:
                p2_loc -= 10
            while die > 100:
                die -= 100
        p2_score += p2_loc
        if p2_score >= 1000:
            return p1_score * rolls


answer = simulate(p1_loc, p2_loc)
print(answer)


def update_multiverse(universes, player):
    odds = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    new_universes = collections.defaultdict(int)
    p1_new_wins = 0
    p2_new_wins = 0
    for state, count in universes.items():
        if player == 1:
            player_score = state[0]
            player_loc = state[1]
            other_score = state[2]
            other_loc = state[3]
        else:
            player_score = state[2]
            player_loc = state[3]
            other_score = state[0]
            other_loc = state[1]
        for roll_sum, quantity in odds.items():
            new_loc = (player_loc + roll_sum)
            while new_loc > 10:
                new_loc -= 10
            new_score = player_score + new_loc
            if player == 1:
                new_state = (new_score, new_loc, other_score, other_loc)
            else:
                new_state = (other_score, other_loc, new_score, new_loc)
            new_count = count * quantity
            if new_state[0] >= 21:
                p1_new_wins += new_count
            elif new_state[2] >= 21:
                p2_new_wins += new_count
            else:
                new_universes[new_state] += new_count
    return new_universes, p1_new_wins, p2_new_wins


def sim_2(x, y):
    p1_wins = 0
    p2_wins = 0
    universes = {(0, x, 0, y): 1}
    while universes:
        for player in [1, 2]:
            universes, a, b = update_multiverse(universes, player)
            p1_wins += a
            p2_wins += b
    return p1_wins, p2_wins


a, b = sim_2(9, 6)
answer = max(a, b)
print(answer)
