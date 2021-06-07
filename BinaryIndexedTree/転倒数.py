"""
転倒数をもとめる．

転倒数: 自分より右にある，自分より小さな数の個数
"""


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


N = int(input())
lst = list(map(int, input().split()))
sorted_lst = sorted(lst)

# 圧縮
keep = {}
for i in range(N):
    keep[sorted_lst[i]] = i + 1
for i in range(N):
    lst[i] = keep[lst[i]]

bit = BinaryIndexedTree(N)
ans = 0
for i, p in enumerate(lst):
    bit.add(p, 1)
    ans += i + 1 - bit.sum(p)
print(ans)
