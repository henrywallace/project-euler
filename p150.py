from itertools import chain, islice

def s_generator():
    t = 0
    for k in range(1, 500500 + 1):
        t = (615949*t + 797807) % pow(2, 20)
        yield t - pow(2, 19)

triangle = [[]]
row = 1
for i, s in enumerate(s_generator(), start=1):
    if len(triangle[-1]) == row:
        triangle.append([])
        row += 1
    triangle[-1].append(s)

# triangle = [
#     [15],
#     [-14, -7],
#     [20, -13, -5],
#     [-3, 8, 23, -26],
#     [1, -4, -5, -18, 5],
#     [-16, 31, 2, 9, 28, 3]]

def stride_sums(row, stride):
    # runs O(row)
    assert(stride <= row + 1)
    s = sum(islice(triangle[row], stride))
    yield s
    for i in range(row - stride + 1):
        s -= triangle[row][i]
        s += triangle[row][i + stride]
        yield s

subs = []
global_min = float('inf')
for i, row in enumerate(triangle):
    for sub, m in zip(subs, range(i + 1, 1, -1)):
        for j, s in zip(range(len(sub)), stride_sums(i, m)):
            sub[j] += s
    subs.append(row)
    global_min = min(global_min, min(chain.from_iterable(subs)))
print(global_min)
