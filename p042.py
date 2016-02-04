"""the positive solution to n/2(n + 1) == m is n = 1/2(-1 + sqrt(1 + 8m))"""

def is_tri_num(m):
	k = (-1 + (1 + 8*m)**0.5)/2
	return k == int(k)

def word_score(string):
	assert(all(c.isalpha() for c in string))
	return sum(ord(c) - 64 for c in string)

with open('p042_words.txt') as f:
	names = (n.strip("\'\"") for n in f.read().split(','))
	print(sum(1 for n in names if is_tri_num(word_score(n))))