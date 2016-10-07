# Simply iterate and check divisibility.
print(sum(n for n in range(10**3)
          if n % 3 == 0 or n % 5 == 0))
