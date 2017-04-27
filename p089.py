ranks = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
symbols = {
    1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
    90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}


def parse_roman(num_str):
    n, i = 0, 0
    while i < len(num_str) - 1:
        r, s = ranks[num_str[i]], ranks[num_str[i + 1]]
        if s > r:
            n += s - r
            i += 2
        else:
            n += r
            i += 1
    if i < len(num_str):
        n += ranks[num_str[i]]
    return n


def to_roman(n):
    u = sorted(symbols.keys())
    s = ''
    while n > 0:
        v = u.pop()
        k = n//v
        if k > 0:
            s += symbols[v]*k
        n %= v
    return s

chars_saved = 0
with open('p089_roman.txt') as f:
    for num_str in map(str.strip, f.readlines()):
        short = to_roman(parse_roman(num_str))
        chars_saved += len(num_str) - len(short)
print(chars_saved)
