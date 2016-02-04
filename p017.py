# http://english.stackexchange.com/a/111837

words = {
	1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
	6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',

	10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
	14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
	18: 'eighteen', 19: 'nineteen',

	20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
	60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',

	100: 'hundred', 1000: 'thousand'}

def num2word(n):
	if n < 20:
		return words[n]
	elif n < 100:
		if n % 10 == 0:
			return words[n]
		return ' '.join((words[(n//10)*10], words[n % 10]))
	elif n < 1000:
		if n % 100 == 0:
			return ' '.join((words[n//100], words[100]))
		return ' '.join((words[n//100], 'hundred', 'and', num2word(n % 100)))
	else:
		return ' '.join(('one', words[n]))

def alphasum(string):
	return sum(1 for c in string if c.isalpha())

k = 1000
for n in range(1, k + 1):
	print(n, num2word(n))
print(sum(map(alphasum, map(num2word, range(1, k + 1)))))