"""拡張ユークリッドの互除法"""


def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
        return d, x, y
    return a, 1, 0


def main():
    a, b = map(int, input().split())
    i, j, k = extgcd(a, b)
    print(j, k)


if '__main__' == __name__:
    main()
