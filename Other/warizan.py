def warizan(x, n):
    sho = x // n
    amari = x % n

    if amari >= 0:
        return sho, amari
    else:
        return sho + 1, amari - n


def solve(n, k):
    ans = ''
    while n != 0:
        sho, amari = warizan(n, k)
        n = sho
        ans = str(amari) + ans

    if ans:
        return ans
    else:
        return 0

# n = int(input())
# print(solve(n, -2))
