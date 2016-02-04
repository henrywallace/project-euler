s = ''.join(map(str, range(1, 10**6)))
p = 1
for i in range(7):
    p *= int(s[10**i - 1])
print(p)

# COMPLEX MEMORY AND TIME EFFICIENT SOLUTION
# i, j = 0, 0
# prev, curr = 0, 0
# ds = []
# while i < 5:
#     if curr > 10**j:
#         t = 10**j - prev
#         k, r = t//i, t%i
#         if r > 0:
#             k += 1
#         d = str(prev + k)[r - 1]
#         print((i, j), prev, curr, (t, k, r), d)
#         j += 1
#     else:
#         prev, curr = curr, curr + (i + 1)*(10**(i + 1) - 10**i)
#         i += 1
