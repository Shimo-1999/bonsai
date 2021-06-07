"""
Binary Indexed Tree(Fenwick Tree)

memo: x の最も下に立っているビットは，x & -x で取り出せる
"""


class BinaryIndexedTree:
    def __init__(self, lst):
        self.n = len(lst)
        self.bit = lst

    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

    def sum(self, i):
        ret = 0
        while i > 0:
            ret += self.bit[i]
            i -= i & -i
        return ret
