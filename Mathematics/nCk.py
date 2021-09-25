# 高速二項係数

MOD = 10 ** 9 + 7


def preprocess(n):
    global fac, finv
    fac = [1]
    finv = [1]
    for i in range(1, n):
        fac.append((fac[i - 1] * i) % MOD)
        finv.append(pow(fac[i - 1] * i, -1, MOD))


def nCk(n, k):
    if n < k:
        return 0
    if (n < 0) | (k < 0):
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


def nHk(n, k):
    return nCk(n + k - 1, n - 1)


def test():
    preprocess(10)
    for i in range(10):
        print(nCk(i, 3), i)


if __name__ == '__main__':
    # main()
    test()
