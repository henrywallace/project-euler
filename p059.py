from collections import Counter
from itertools import islice, product, repeat
from math import log
from string import ascii_lowercase

from nltk.corpus import gutenberg

with open('p059_cipher.txt') as f:
    chars = list(map(int, f.read().split(',')))

# use bigram transition probabilities
text = gutenberg.raw('whitman-leaves.txt')
c = Counter(zip(text, islice(text, 1, None)))
z = sum(c.values())
reference = {k: v/z for k, v in c.items()}


def decrypt(key):
    return ''.join(chr(ord(key[i % len(key)]) ^ x)
                   for i, x in enumerate(chars))


def likelihood(message, reference):
    l = 0
    for bigram in zip(message, islice(message, 1, None)):
        l += log(reference.get(bigram, 1))
    return l

m, k = float('inf'), None
for t in product(*repeat(ascii_lowercase, 3)):
    key = ''.join(t)
    l = likelihood(decrypt(key), reference)
    if l < m:
        m, k = l, key
print(m, k)
print(decrypt(k))
