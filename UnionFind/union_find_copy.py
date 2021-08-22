from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

#############################################################################################################################


uf = UnionFind(6)
print(uf.parents)
# [-1, -1, -1, -1, -1, -1]

print(uf)
# 0: [0]
# 1: [1]
# 2: [2]
# 3: [3]
# 4: [4]
# 5: [5]

uf.union(0, 2)
print(uf.parents)
# [-2, -1, 0, -1, -1, -1]

print(uf)
# 0: [0, 2]
# 1: [1]
# 3: [3]
# 4: [4]
# 5: [5]

uf.union(1, 3)
print(uf.parents)
uf.union(4, 5)
print(uf.parents)
uf.union(1, 4)
print(uf.parents)
# [-2, -2, 0, 1, -1, -1]
# [-2, -2, 0, 1, -2, 4]
# [-2, -4, 0, 1, 1, 4]

print(uf)
# 0: [0, 2]
# 1: [1, 3, 4, 5]

print(uf.parents)
# [-2, -4, 0, 1, 1, 1]

print('-----------')
for i in range(len(uf.parents)):
    print(abs(uf.parents[uf.find(i)]))
print(uf.find(0))
# 0

print(uf.find(5))
# 1

print(uf.size(0))
# 2

print(uf.size(5))
# 4

print(uf.same(0, 2))
# True

print(uf.same(0, 5))
# False

print(uf.members(0))
# [0, 2]

print(uf.members(5))
# [1, 3, 4, 5]

print(uf.roots())
# [0, 1]

print(uf.group_count())
# 2

print(uf.all_group_members())
# {0: [0, 2], 1: [1, 3, 4, 5]}

print(list(uf.all_group_members().values()))
# [[0, 2], [1, 3, 4, 5]]
