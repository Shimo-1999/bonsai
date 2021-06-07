"""
Binary Indexed Tree(Fenwick Tree)
n 次元に容易に拡張できる

memo: x の最も下に立っているビットは，x & -x で取り出せる
"""


class BinaryIndexedTree:
    def __init__(self, n, m, bit):
        self.n = n
        self.m = m
        self.bit = bit

    def add(self, i, j, x):
        while i <= self.m:
            while j <= self.n:
                self.bit[i][j] += x
                j += j & -j
            i += i & -i

    def sum(self, i, j):
        ret = 0
        while i > 0:
            while j > 0:
                ret += self.bit[i][j]
                j -= j & -j
            i -= i & -i
        return ret
