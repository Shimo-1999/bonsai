def warizan(x, n):
    """
    x を -n で割る際にあまりを非負にする
    """
    sho = x // (-n)
    amari = x % (-n)

    if amari >= 0:
        return sho, amari
    else:
        return sho + 1, amari + n


def main():
    N = int(input())
    ans = ''
    while N != 0:
        sho, amari = warizan(N, 2)
        N = sho
        ans = str(amari) + ans

    if ans:
        print(ans)
    else:
        print(0)


def test():
    print('7 ÷ 3 =', 7 // 3, 'あまり', 7 % 3)
    print('-7 ÷ 3 =', (-7) // 3, 'あまり', (-7) % 3)
    print('7 ÷ -3 =', 7 // (-3), 'あまり', 7 % (-3))
    print('-7 ÷ -3 =', (-7) // (-3), 'あまり', (-7) % (-3))


if __name__ == '__main__':
    # main()
    test()
