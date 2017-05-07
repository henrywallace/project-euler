from collections import Counter
from itertools import cycle
from math import log
from string import ascii_lowercase


def read_cipher(path):
    """Read the cipher file, and return a list of code points."""
    with open(path) as f:
        return [int(cp) for cp in f.read().strip().split(',')]


def corpus_counts(path):
    """Return unigram counts from a corpus."""
    with open(path) as f:
        text = f.read()
    return Counter(text)


def score(text, counts):
    """
    Return a score deciphered text given unigram counts from another corpus.

    A higher score indicates a better decipher solution. While we could
    define this score as the product of probabilities, we realize that
    everything is normalized the same. So, we can just use counters. And
    to then avoid overflow, we just do a log sum.
    """
    return sum(log(counts.get(c, 1)) for c in text)


def partial_decipher(cipher, code_point, i, keylen):
    """Partially decipher with just one code point of a key."""
    return ''.join(chr(cp ^ code_point) for j, cp in enumerate(cipher)
                   if j % keylen == i)


def decipher(cipher, key):
    """Return a complete decipher solution."""
    partials = [iter(partial_decipher(cipher, cp, i, len(key)))
                for i, cp in enumerate(key)]
    return ''.join(map(next, cycle(partials)))


def solve(cipher, counts, keylen=3):
    """
    Return the highest scoring cipher key.

    We define the best key to be the sequence of highest scoring
    code points from partial decipher solutions.
    """
    best_key = []
    for i in range(keylen):
        best_score, best_cp = -1, None
        for cp in map(ord, ascii_lowercase):
            text = partial_decipher(cipher, cp, i, keylen)
            s = score(text, counts)
            if s > best_score:
                best_score, best_cp = s, cp
        best_key.append(best_cp)
    return best_key


if __name__ == '__main__':
    counts = corpus_counts('p059_ulysses.txt')
    cipher = read_cipher('p059_cipher.txt')
    best_key = solve(cipher, counts)
    deciphered = decipher(cipher, best_key)

    print(''.join(chr(cp) for cp in best_key))
    print(deciphered)
    print(sum(ord(c) for c in deciphered))
