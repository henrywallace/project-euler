a = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]]


def min_sum(a):
    b = [[0]*len(a[0]) for _ in range(len(a))]
    for i in range(len(a)):
        b[i][0] = a[i][0]
    for j in range(1, len(a[0])):
        for i in range(len(a)):
            if i == 0:
                b[i][j] = a[i][j] + \
                    min(b[i][j - 1], b[i + 1][j - 1] + a[i + 1][j])
            elif i == len(a) - 1:
                b[i][j] = a[i][j] + \
                    min(b[i][j - 1], b[i - 1][j - 1] + a[i - 1][j])
            else:
                b[i][j] = a[i][j] + \
                    min(b[i - 1][j - 1] + a[i - 1][j], b[i][j - 1],
                        b[i + 1][j - 1] + a[i + 1][j])
    return min(row[-1] for row in b)

with open('p082_matrix.txt') as f:
    a = [[int(x) for x in line.split(',')] for line in f.readlines()]
    print(min_sum(a))
