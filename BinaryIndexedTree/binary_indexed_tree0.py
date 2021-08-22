"""
Binary Indexed Tree(Fenwick Tree) 0-indexed
- a_0 ~ a_i の和が求められる．
- a_i += x ができる．
"""


class BinaryIndexedTree:
    def __init__(self, n):
        self.size = n
        self.bit = [0] * n

    def add(self, i, x):
        while i < self.size:
            self.bit[i] += x
            i |= i + 1

    def sum(self, i):
        ret = 0
        while i >= 0:
            ret += self.bit[i]
            i = (i & (i + 1)) - 1
        return ret
