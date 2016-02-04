from collections import namedtuple, Counter, defaultdict
from itertools import combinations, islice

Card = namedtuple('Card', ['rank', 'suit'])

rank_value = {i: c for i, c in enumerate('23456789TJQKA', start=2)}

def combos(hand):
    # return list of combos in sorted order
    combos = []
    ranks, suits = map(Counter, zip(*hand))
    ordered = sorted(rank_value[r] for r in ranks)
    straight = all(y - x == 1 for x, y in \
        zip(ordered, islice(ordered, 1, None)))
    runs = defaultdict(list)
    for k, v in ranks.items():
        if v > 1:
            runs[v].append(rank_value[k])

    if len(suits) == 1:
        combos.append((6, 'Flush'))
        if straight:
            combos.append((9, 'Straight Flush', ordered[0]))
            if ordered[0] == 10:
                combos.append((10, 'Royal Flush'))
    if straight:
        combos.append((5, 'Straight', ordered[0]))
    if 4 in runs:
        combos.append((8, 'Four of a Kind', runs[4]))
    if 3 in runs and 2 in runs:
        combos.append((7, 'Full House', runs[3], runs[2]))
    if 3 in runs:
        combos.append((4, 'Three of a Kind', runs[3]))
    if len(runs[2]) == 2:
        combos.append((3, 'Two Pairs', sorted(runs[2], reverse=True)))
    elif len(runs[2]) == 1:
        combos.append((2, 'One Pair', runs[2]))
    combos.append((1, 'High Card', ordered[-1]))
    return sorted(combos, reverse=True)

def parse_hand(card_list):
    hand = []
    for card in card_list:
        rank, suit = card
        try:
            rank = int(rank)
        except ValueError:
            pass
        hand.append(Card(rank=rank, suit=suit))
    return hand

values = {r:i for i,r in enumerate('23456789TJQKA', start=2)}
straights = [(v, v-1, v-2, v-3, v-4) for v in range(14, 5, -1)] + [(14, 5, 4, 3, 2)]
ranks = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(),(),(3,2),(4,1)]

def hand_rank(hand):
    score = zip(*sorted(((v, values[k]) for
        k,v in Counter(x[0] for x in hand).items()), reverse=True))
    score[0] = ranks.index(score[0])
    if len(set(card[1] for card in hand)) == 1: score[0] = 5  # flush
    if score[1] in straights: score[0] = 8 if score[0] == 5 else 4  # str./str. flush
    return score

p1_wins = 0
with open('p054_poker.txt') as f:
    for line in map(str.split, f.readlines()):
        hand1, hand2 = map(parse_hand, (line[:5], line[5:]))
        if combos(hand1) > combos(hand2):
            p1_wins += 1
print(p1_wins)


