from math import inf
import itertools
from utilities import load_data


YEAR = 2015
DAY = 22
input_data = load_data(year=YEAR, day=DAY)


spell_costs = {
    'missile': 53,
    'drain': 73,
    'shield': 113,
    'poison': 173,
    'recharge': 229
}


def player_wins(spell_list):
    boss_hp = 58
    boss_dmg = 9
    player_hp = 50
    player_mana = 500
    player_armor = 0
    shield_timer = 0
    poison_timer = 0
    recharge_timer = 0
    mana_spent = 0
    turn = 'player'
    while True:
        if shield_timer:
            shield_timer -= 1
            if shield_timer == 0:
                player_armor -= 7
        if poison_timer:
            boss_hp -= 3
            if boss_hp <= 0:
                return True, mana_spent
            poison_timer -= 1
        if recharge_timer:
            player_mana += 101
            recharge_timer -= 1
        if turn == 'player':
            # Player turn:
            turn = 'boss'
            player_hp -= 1
            if player_hp <= 0:
                return False, mana_spent

            spell = None
            while not spell:
                if spell_list:
                    spell = spell_list.pop(0)
                else:
                    break
                if spell and spell_costs[spell] > player_mana:
                    spell = None
            if spell is None:
                return False, mana_spent
            mana_spent += spell_costs[spell]
            player_mana -= spell_costs[spell]

            if spell == 'missile':
                boss_hp -= 4
                if boss_hp <= 0:
                    return True, mana_spent
            elif spell == 'drain':
                boss_hp -= 2
                if boss_hp <= 0:
                    return True, mana_spent
                player_hp += 2
            elif spell == 'shield':
                if shield_timer:
                    return False, mana_spent
                player_armor += 7
                shield_timer = 6
            elif spell == 'poison':
                if poison_timer:
                    return False, mana_spent
                poison_timer = 6
            elif spell == 'recharge':
                if recharge_timer:
                    return False, mana_spent
                recharge_timer = 5
        else:
            # Boss turn:
            turn = 'player'
            player_hp -= boss_dmg - player_armor
            if player_hp <= 0:
                return False, mana_spent



def solve():
    min_mana = inf
    min_spell_list = None
    for spell_list_length in range(10, 11):
        print(f'{spell_list_length=}')
        for spell_list in itertools.product(['missile', 'drain', 'shield', 'poison', 'recharge'], repeat=spell_list_length):
            player_win, mana = player_wins(list(spell_list))
            if player_win:
                print(f'Got a win! {mana=}, {spell_list=}')
                if mana < min_mana:
                    min_mana = mana
                    min_spell_list = list(spell_list)
    return min_mana, min_spell_list


answer, sl = solve()
print(answer)
print(sl)
