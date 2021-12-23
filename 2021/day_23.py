from math import inf
import random
from copy import deepcopy
import heapq
from collections import deque
from utilities import load_data


YEAR = 2021
DAY = 23
input_data = load_data(year=YEAR, day=DAY)
input_data = input_data.splitlines()


energies = {
    'a': 1,
    'b': 10,
    'c': 100,
    'd': 1000
}


# start = {
#     'rooms': {
#         'a': ['b', 'd'],
#         'b': ['a', 'c'],
#         'c': ['a', 'b'],
#         'd': ['d', 'c'],
#     },
#     'hall': [None] * 11
# }

start = {
    'rooms': {
        'a': ['b', 'd', 'd', 'd'],
        'b': ['a', 'c', 'b', 'c'],
        'c': ['a', 'b', 'a', 'b'],
        'd': ['d', 'a', 'c', 'c'],
    },
    'hall': [None] * 11
}

ROOM_DEPTH = len(start['rooms']['a'])


def state_to_tuple(state):
    out = []
    for pod in 'abcd':
        val = state['rooms'][pod]
        out += [None]*(ROOM_DEPTH - len(val))
        out += val
    out += state['hall']
    return tuple(out)


def legal_next_states(state):
    room_indices = {
        'a': 2,
        'b': 4,
        'c': 6,
        'd': 8
    }
    results = []
    for hall_idx, pod in enumerate(state['hall']):
        if pod is None:
            # If there's no pod at this location, continue.
            continue
        # The destination is state['rooms'][pod].  If there's any other pod
        # type in the room, then this pod can't go home.
        occupants = state['rooms'][pod]
        ready = all(ch == pod for ch in occupants)
        if not ready:
            continue
        room_idx = room_indices[pod]
        m = min(hall_idx, room_idx)
        M = max(hall_idx, room_idx)
        if all(o is None for o in state['hall'][m+1:M]):
            depth = ROOM_DEPTH - len(occupants)
            dist = abs(room_idx - hall_idx)
            cost = (depth + dist) * energies[pod]
            state_copy = deepcopy(state)
            state_copy['hall'][hall_idx] = None
            state_copy['rooms'][pod].insert(0, pod)
            results.append((cost, state_copy))
    for room, occupants in state['rooms'].items():
        if not occupants:
            continue
        room_idx = room_indices[room]
        pod = occupants[0]
        if pod == room and all(pod == o for o in occupants):
            continue
        for hall_idx, occ in enumerate(state['hall']):
            if hall_idx in [0, 1, 3, 5, 7, 9, 10] and occ is None:
                # If there's no one here in the hall, maybe we can move here
                # All intermediate locations need to be empty
                m = min(hall_idx, room_idx)
                M = max(hall_idx, room_idx)
                if all(o is None for o in state['hall'][m:M]):
                    depth = ROOM_DEPTH - len(occupants) + 1
                    dist = abs(room_idx - hall_idx)
                    cost = (depth + dist) * energies[pod]
                    state_copy = deepcopy(state)
                    state_copy['rooms'][room].pop(0)
                    state_copy['hall'][hall_idx] = pod
                    results.append((cost, state_copy))
    return results


computed_costs = {}


def finished(state):
    for room, occupants in state['rooms'].items():
        if occupants != [room]*ROOM_DEPTH:
            return False
    return True


def energy_cost_to_goal(state):
    if finished(state):
        return 0
    if state_to_tuple(state) in computed_costs:
        return computed_costs[state_to_tuple(state)]
    cost = inf
    next_states = legal_next_states(state)
    for delta, new in next_states:
        cost = min(cost, delta + energy_cost_to_goal(new))
    computed_costs[state_to_tuple(state)] = cost
    return cost


answer = energy_cost_to_goal(start)
print(answer)