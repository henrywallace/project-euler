from itertools import groupby

with open('p098_words.txt') as f:
    words = f.read().split('","')

words = sorted(words, key=len)
for k, g in groupby(words, key=len):
    pass
