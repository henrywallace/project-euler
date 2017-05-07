"""
We solve this problem by modeling the transition probabilities, running
several walks in parallel, and summing their arrival counts.

Luckily, we are asked for only the top k=3 probabilities. The true arrival
probabilities seem to get very close to each other whenver k > 3.
Unfortunately, our naive solution is sufficient for a green checkmark.

More interestingly, for general k, how many steps in a walk are _probably
sufficient_? Can the total number of sufficient steps be reduced if we do
multiple walks?

We can view each state's stationary arrival propbability as a Bernoulli
variable p. With Hoeffding's inequality, we can draw a tight confidence ball
around each empirical esimate q. Specifically, q +- sqrt( 1/(2n) *
log(2/alpha) ), for some confidence alpha. We call the radius of this ball
interval r.

We wish to determine the most frequent k states. Let S(p) denote those true
states, and S(q) denote our estimate. Let m denote the minimum distance
between the probabilites of S(p). If we choose r < m/2, then we can be
confident that our ordered S(q) is S(p). But how do we estimate m?
"""
from random import randint, shuffle
from collections import deque, Counter
from functools import partial
import multiprocessing as mp


BOARD = '''
    GO A1 CC1 A2 T1 R1 B1 CH1 B2 B3
    JAIL C1 U1 C2 C3 R2 D1 CC2 D2 D3
    FP E1 CH2 E2 E3 R3 F1 F2 U2 F3
    G2J G1 G2 CC3 G3 R4 CH3 H1 T2 H2
'''.strip().split()

INDEX = {s: i for (i, s) in enumerate(BOARD)}

COMMUNITY = deque([None]*14 + [
    'Advance to GO',
    'Go to JAIL'])

CHANCE = deque([None]*6 + [
    'Advance to GO',
    'Go to JAIL',
    'Go to C1',
    'Go to E3',
    'Go to H2',
    'Go to R1',
    'Go to next R',
    'Go to next R',
    'Go to next U',
    'Go back 3 squares'])


def resolve_community(i, card):
    """Return the index of the next square given a Community Chest card."""
    if card is None:
        return i

    if card == 'Advance to GO':
        return INDEX['GO']
    if card == 'Go to JAIL':
        return INDEX['JAIL']

    raise NotImplementedError


def next_closest(i, choices):
    """Return the _next_ closest index, given some choice indices."""
    offsets = [((c - i) % len(BOARD), i) for c in choices]

    return min(offsets)[1]


def resolve_chance(i, card):
    """Return the index of the next square given a Chance card."""
    if card is None:
        return i

    if card == 'Advance to GO':
        return INDEX['GO']
    if card == 'Go to JAIL':
        return INDEX['JAIL']
    if card == 'Go to C1':
        return INDEX['C1']
    if card == 'Go to E3':
        return INDEX['E3']
    if card == 'Go to H2':
        return INDEX['H2']
    if card == 'Go to R1':
        return INDEX['R1']
    if card == 'Go to next R':
        choices = [INDEX[r] for r in ('R1', 'R2', 'R3', 'R4')]
        return next_closest(i, choices)
    if card == 'Go to next U':
        choices = [INDEX[u] for u in ('U1', 'U2')]
        return next_closest(i, choices)
    if card == 'Go back 3 squares':
        return i - 3

    raise NotImplementedError


def draw(deck):
    """Draw a card from a deque of cards."""
    card = deck.pop()
    deck.appendleft(card)
    return card


def roll_dice(num_sides=6, num_dice=2):
    """Roll some number of fair dice with some number of sides."""
    return [randint(1, num_sides) for _ in range(num_dice)]


def shuffle_decks():
    """
    Shuffle copies of the Community Chest and Chance decks.

    We make copies so that concurrent Markov chain simulations won't interfere
    with each other.
    """
    community_deck = COMMUNITY.copy()
    chance_deck = CHANCE.copy()
    shuffle(community_deck)
    shuffle(chance_deck)
    return community_deck, chance_deck


def simulate(roll_dice, steps, burn=100):
    """Return emperically visit counts from a several Monopoly walks."""
    visits = Counter()
    doubles = 0
    i = 0
    community_deck, chance_deck = shuffle_decks()

    for k in range(steps):
        dice = roll_dice()
        if len(set(dice)) == 1:
            doubles += 1
        else:
            doubles = 0

        if doubles == 3:
            i = INDEX['JAIL']
        else:
            i = (i + sum(dice)) % len(BOARD)
            if i == INDEX['G2J']:
                i = INDEX['JAIL']
            elif BOARD[i].startswith('CC'):
                card = draw(community_deck)
                i = resolve_community(i, card)
            elif BOARD[i].startswith('CH'):
                card = draw(chance_deck)
                i = resolve_chance(i, card)

        if k >= burn:
            visits[i] += 1

    return visits


if __name__ == '__main__':
    steps = 10**5
    walks = 4
    r = partial(roll_dice, num_sides=4)

    with mp.Pool(processes=4) as pool:
        sims = [pool.apply_async(simulate, (r, steps)) for i in range(walks)]
        visits = sum((s.get() for s in sims), Counter())

    modal_string = ''
    for i, count in visits.most_common(3):
        modal_string += format(i, '02')
        print(BOARD[i], i, count/(walks*steps))
    print(modal_string)
