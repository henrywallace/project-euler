with open('p022_names.txt') as f:
	names = [n.strip("\"\'") for n in f.read().split(',')]

def alphabet_val(name):
	# assumes letters are uppercase
	return sum(ord(l) - 64 for l in name)

s = 0
for i, name in enumerate(sorted(names), start=1):
	s += i*alphabet_val(name)
print(s)