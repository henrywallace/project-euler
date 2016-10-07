from collections import namedtuple, defaultdict
from itertools import combinations

Card = namedtuple('Card', ['rank', 'suit'])
rank_value = {rank: value for value, rank in
              enumerate('23456789TJQKA', start=2)}

def get_combos(cards):
    combos = []
    value_bins = defaultdict(list)
    for card in cards:
        value = rank_value[card.rank]
        value_bins[value] = card
    
    # High Card
    combos += [(1, rank_value[card.rank]) for card in cards]

    # One Pair
    for value, bin in value_bins.items():
        if len(bin) == 2:
            combos.append((2, value))

    


def parse_line(line):
    cards = [Card(*code) for code in line.split()]
    hand1, hand2 = cards[:5], cards[:5]
    return hand1, hand2





if __name__ == '__main__':
    with open('p054_poker.txt') as f:
        for line in f:
            hand1, hand2 = parse_line(line)
            print(hand1)
