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