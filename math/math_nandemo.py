from collections import Counter


def prime_factorize(n):
    """
    高速素因数分解
    """
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def make_divisors(n):
    """
    高速約数列挙
    """
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def main():
    # 素因数分解
    print(prime_factorize(67280421310721))
    print(prime_factorize(67280421310722))
    print(Counter(prime_factorize(840)))

    # 約数列挙
    print(make_divisors(67280421310721))
    print(make_divisors(67280421310722))


if __name__ == '__main__':
    main()
