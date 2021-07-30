def make_divisors(n):
    """
    約数列挙
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

    # 約数列挙
    print(make_divisors(67280421310721))
    print(make_divisors(67280421310722))


if __name__ == '__main__':
    main()
