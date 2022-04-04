MOD = 10 ** 9 + 7


def preprocess(n):
    global fac, finv
    fac = [1]
    finv = [1]
    for i in range(1, n):
        fac.append((fac[i - 1] * i) % MOD)
        finv.append(pow(fac[i - 1] * i, MOD - 2, MOD))


def permutation(n):
    return fac[n]


def combination(n, k):
    if (k < 0) or (k > n):
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


def homogeneous(n, k):
    return combination(n + k - 1, n - 1)


preprocess(10 ** 6)

import math
from random import randint
for _ in range(10):
    n = randint(0, 10 ** 3)
    k = randint(0, n)

    assert combination(n, k) == (math.comb(n, k) % MOD)
