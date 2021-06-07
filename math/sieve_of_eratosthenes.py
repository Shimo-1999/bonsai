import math


def get_sieve_of_eratosthenes(n):
    """
    :return: n 以下の素数のリスト
    """
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


print(get_sieve_of_eratosthenes(1000))


def main():
    """典型90-30"""
    N, K = map(int, input().split())
    prime_lst = [0] * (N + 1)

    # エラトステネスの本質 n * loglogn
    for i in range(2, N + 1):
        if prime_lst[i] != 0:
            continue
        for j in range(i, N + 1, i):
            prime_lst[j] += 1

    ans = 0
    for i in range(N + 1):
        ans += (prime_lst[i] >= K)
    print(ans)
