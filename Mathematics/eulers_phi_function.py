"""
オイラーのファイ関数
正の整数 n に対して n と互いに素である 1 以上 n 以下の自然数の個数は
p_i が の i 番目の素因数だとすると

\phi(n) = n * \prod_{i = 1}^k (1 - 1/p_i)
"""


def prime_factorize(n):
    """
    素因数分解
    """
    prime_lst = []
    # 2 で割る
    while n % 2 == 0:
        prime_lst.append(2)
        n //= 2
    # 3 以降で割る
    divisor = 3
    while divisor ** 2 <= n:
        if n % divisor == 0:
            prime_lst.append(divisor)
            n //= divisor
        else:
            divisor += 2
    if n != 1:
        prime_lst.append(n)
    return prime_lst


n = int(input())
ans = n
for i in set(prime_factorize(n)):
    ans *= (i - 1)
    ans /= i
print(int(ans))
