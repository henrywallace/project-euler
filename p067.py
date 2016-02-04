tri = []
with open('p067_triangle.txt') as f:
    for nums in f.readlines():
        tri.append([int(n) for n in nums.split()])

def max_sum(tri):
    # assumes all entries are non-negative
    # changes entries of tri
    if len(tri) == 0:
        return 0
    for i in range(1, len(tri)):
        tri[i][0] += tri[i - 1][0]
        for j in range(1, len(tri[i]) - 1):
            tri[i][j] += max(tri[i - 1][j], tri[i - 1][j - 1])
        tri[i][-1] += tri[i - 1][-1]
    return max(tri[-1])

print(max_sum(tri))