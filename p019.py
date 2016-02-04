from itertools import cycle

def month_days(month, year):
	if month in {'sep', 'apr', 'jun', 'nov'}:
		return 30
	if month == 'feb':
		if year % 4 == 0:
			if year % 100 == 0 and year % 400 != 0:
				return 28
			return 29
		return 28
	return 31

def calendar():
	# yields dates from monday 1 jan 1900
	days = cycle(('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'))
	months = cycle(('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 
					'aug', 'sep', 'oct', 'nov', 'dec'))
	d, m, y = next(days), next(months), 1900
	yield (d, 1, m, y)
	while True:
		for i in range(1, month_days(m, y) + 1):
			yield (d, i, m, y)
			d = next(days)
		if m == 'dec':
			y += 1
		m = next(months)
		yield (d, i, m, y)

c = calendar()
d, i, m, y = next(c)
while (i, m, y) != (1, 'jan', 1901):
	d, i, m, y = next(c)

nsundays = 1 if d == 'sun' else 0
while (i, m, y) != (31, 'dec', 2000):
	d, i, m, y = next(c)
	if (d, i) == ('sun', 1):
		nsundays += 1
print(nsundays)