"""
100 までの素数の数 25
1000 までの素数の数 168
10000 までの素数の数 1229
100000 までの素数の数 9592
1000000 までの素数の数 78498
"""

n = 1000000

num = [False, False] + [True] * (n - 1)
for i in range(2, int(n ** 0.5) + 1):
    for j in range(i ** 2, n + 1, i):
        num[j] = False

print(sum(num))
