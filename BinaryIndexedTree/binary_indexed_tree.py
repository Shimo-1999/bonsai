"""
Binary Indexed Tree(Fenwick Tree)
- a_1 ~ a_i の和が求められる．
- a_i += x ができる．
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
