class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += (i & -i)

    def sum(self, i):
        ret = 0
        while i > 0:
            ret += self.bit[i]
            i -= (i & -i)
        return ret


def inversion_number(N, lst):
    """
    転倒数をもとめる．
    転倒数: 自分より左にあり，自分より小さな数の個数
    """
    # 圧縮
    keep = {}
    for idx, num in enumerate(sorted(lst)):
        keep[num] = idx + 1
    for i in range(N):
        lst[i] = keep[lst[i]]

    bit = BinaryIndexedTree(N)
    cnt = 0
    for idx, p in enumerate(lst):
        bit.add(p, 1)
        cnt += idx + 1 - bit.sum(p)
    return cnt


N = int(input())
lst = list(map(int, input().split()))
cnt = inversion_number(N, lst)
print(cnt)
