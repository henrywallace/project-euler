from collections import deque
from itertools import chain, repeat

def lagged_fib():
    s = deque(maxlen=55)
    for k in range(1, 55 + 1):
        s_val = (100003 - 200003*k + 300007*k**3) % 1000000 - 500000
        yield s_val
        s.append(s_val) 
    for k in range(56, 4*10**6 + 1):
        s_val = (s[-24] + s[-55] + 10**6) % 1000000 - 500000
        yield s_val
        s.append(s_val)

# generate the table
table = []
for s_val in lagged_fib():
    if len(table) == 0 or len(table[-1]) == 2000:
        table.append([])
    table[-1].append(s_val)

def max_contiguous(a, indices):
    global_max, suffix_max = 0, 0
    for i, j in indices:
        if a[i][j] + suffix_max > global_max:
            suffix_max += a[i][j]
            global_max = suffix_max
        elif a[i][j] + suffix_max > 0:
            suffix_max += a[i][j]

        else:
            suffix_max = 0
    return global_max

# horizontal slices
max_slice = max(max_contiguous(table, zip(repeat(i), range(2000))) \
    for i in range(2000))

# vertical slices
max_slice = max(max_slice, max(max_contiguous(table, \
    zip(range(2000), repeat(j))) for j in range(2000)))

# diagonal slices
def diagonals():
    for i, j in chain(zip(range(2000), repeat(0)), \
                    zip(repeat(0), range(1, 2000))):
        def diag_indices(i, j):
            while i < 2000 and j < 2000:
                yield i, j
                i += 1
                j += 1
        yield diag_indices(i, j)

def anti_diagonals():
    for i, j in chain(zip(repeat(0), range(2000)), \
                    zip(range(1, 2000), repeat(2000 - 1))):
        def diag_indices(i, j):
            while i < 2000 and j >= 0: 
                yield i, j
                i += 1
                j -= 1
        yield diag_indices(i, j)

max_slice = max(max_slice, max(max_contiguous(table, diag) \
    for diag in chain(diagonals(), anti_diagonals())))


print(max_slice)


