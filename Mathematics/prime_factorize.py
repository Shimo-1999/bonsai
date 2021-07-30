from collections import Counter


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


def main():
    # 素因数分解
    print(prime_factorize(67280421310721))
    print(prime_factorize(67280421310722))
    print(Counter(prime_factorize(840)))


if __name__ == '__main__':
    main()
