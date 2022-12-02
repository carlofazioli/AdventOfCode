import itertools
from math import inf
from utilities import load_data


YEAR = 2016
DAY = 11
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()


# State = [E, ThG, ThM, PlG, PlM, StG, StM, PrG, PrM, RuG, RuM]
start =   [1,   1,   1,   1,   2,   1,   1,   3,   3,   3,   3]
# start =   [4,   4,   4,   4,   4,   4,   4,   4,   4,   4,   3]
goal  =   [4,   4,   4,   4,   4,   4,   4,   4,   4,   4,   4]
memo = {}


def is_valid(state):
    current_floor = state[0]
    if not 1 <= current_floor <= 4:
        return False
    for chip_idx in [2, 4, 6, 8, 10]:
        if state[chip_idx-1] != state[chip_idx]:
            # If the particular chip is not on the same floor as its
            # generator, then there can't be any other generators here.
            for gen_idx in [1, 3, 5, 7, 9]:
                if state[chip_idx] == state[gen_idx]:
                    return False
    return True


def sort_state(state):
    floor = state[0]
    pairs = [state[i:i+2] for i in range(1, len(state), 2)]
    pairs.sort(key=lambda x:sum(x))
    return


def build_dist_map(state, dist=0):
    memo[tuple(state)] = dist
    if state == goal:
        memo[tuple(goal)] = dist
        return
    current_floor = state[0]
    item_indices = [i for i in range(1, 11) if state[i] == current_floor]
    moves = []
    if min(state) < current_floor < 4:
        moves = [-1, 1]
    elif current_floor == min(state):
        moves = [1]
    elif current_floor == 4:
        moves = [-1]
    for move in moves:
        if move == 1:
            for item_tuple in itertools.combinations(item_indices, 2):
                new_state = list(state)
                new_state[0] += move
                new_state[item_tuple[0]] += move
                new_state[item_tuple[1]] += move
                if not is_valid(new_state):
                    continue
                if memo.get(tuple(new_state), inf) < dist + 1:
                    continue
                build_dist_map(new_state, dist + 1)
        if move == -1:
            # Move with 1 item:
            for item_tuple in itertools.combinations(item_indices, 1):
                new_state = list(state)
                new_state[0] += move
                new_state[item_tuple[0]] += move
                if not is_valid(new_state):
                    continue
                if memo.get(tuple(new_state), inf) < dist + 1:
                    continue
                build_dist_map(new_state, dist + 1)


build_dist_map(start)
answer = memo[tuple(goal)]
print(answer)