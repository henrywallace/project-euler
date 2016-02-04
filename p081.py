from itertools import chain

def min_path(a):
    for i, j in chain(((k, 0) for k in range(1, len(a))),
                      ((len(a) - 1, k) for k in range(1, len(a[0])))):
        while i >= 0 and j < len(a[0]):
            if j == 0:
                a[i][j] += a[i - 1][j]
            elif i == 0:
                a[i][j] += a[i][j - 1]
            else:
                a[i][j] += min(a[i - 1][j], a[i][j - 1])
            i -= 1
            j += 1
    return a[-1][-1]

with open('p081_matrix.txt') as f:
    a = [[int(x) for x in line.split(',')] for line in f.readlines()]
    print(min_path(a))
