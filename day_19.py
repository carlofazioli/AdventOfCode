from math import inf
import heapq
from utilities import load_data


YEAR = 2015
DAY = 19
input_data = load_data(year=YEAR, day=DAY)
rules, medicine = input_data.split('\n\n')
rules = rules.splitlines()


rules = [row.split(' => ') for row in rules]
shortening_rules = [b for a, b in rules if len(a) < len(b)]
shortening_rules.sort(key=lambda x: len(x))
rules.sort(key=lambda p: len(p[1])-len(p[0]), reverse=True)


rnar_rules = []
other_rules = []
for r in rules:
    if 'Rn' in r[1]:
        rnar_rules.append(r)
    else:
        other_rules.append(r)


def tokenize(mol):
    tokens = []
    while mol:
        if len(mol) == 1:
            tokens += [mol]
            mol = ''
        elif mol[1].islower():
            tokens.append(mol[:2])
            mol = mol[2:]
        else:
            tokens.append(mol[0])
            mol = mol[1:]
    return tokens


'''
Jesus fuck this puzzle took me like 20 hours, and I had to get
inspiration from Reddit.  

Here are the observations I made.  Certain tokens like Rn and Ar
are only produced in pairs by certain rules.  I sort them into 
the rnar_rules.  The others are in other_rules.  Furthermore, the
rnar_rules are the only ones that create Y.  

Each rule in other_rules increases the length of the molecule 
by 1.  Hence, undoing an other_rule shortens the molecule by 1.  

Each rule in rnar_rules lengthens the molecule by 3, 5, or 7.  
So, undoing those rules shortens by that amount.  By looking
closely at the rnar_rules, we can see that:
    if the rule contains no Y, it lengthens by 3
    if the rule contains  1 Y, it lengthens by 5
    if the rule contains  2 Y, it lengthens by 7

Thus, undoing each of the rnar rules shortens by the formula:
    shortens_by = 1 + #Rn + #Ar + 2(#Y)

This formula trivially applies to the other_rules, since they
contain 0 Rn, 0 Ar, and 0 Y.  

So, every reduction step reduces the count by 
    shortens_by = 1 + #Rn + #Ar + 2(#Y) 
no matter what.
'''

tokens = tokenize(medicine)
ys = 0
rnars = 0
for t in tokens:
    ys += t == 'Y'
    rnars += t in ['Rn', 'Ar']

'''
By subtracting rnars and ys from the total number of tokens, we 
obtain the length of the molecule that would result from shortening
out all of the Rn, Ar, and Y.  Then we would shorten by 1 until 
there is just the 'e' token remaining.'''

answer = len(tokens) - rnars - 2*ys - 1
print(answer)