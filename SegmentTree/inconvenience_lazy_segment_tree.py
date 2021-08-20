"""Range Minimum Query & Range Update Query 遅い (おそらく，再起なので)"""
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


class LazySegmentTree:
    def __init__(self, initial_list, function, identity_element):
        n = len(initial_list)
        self.func = function
        self.ide_ele = identity_element
        self.num = 1 << (n - 1).bit_length()
        self.tree = [identity_element] * 2 * self.num
        self.lazy = [identity_element] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = initial_list[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def propagate(self, k):
        """遅延伝播"""
        if self.lazy[k] == self.ide_ele:
            return
        if k < self.num - 1:
            self.lazy[k * 2 + 1] = self.lazy[k]
            self.lazy[k * 2 + 2] = self.lazy[k]
        self.tree[k] = self.lazy[k]
        self.lazy[k] = self.ide_ele

    def query(self, a, b, k, left, right):
        self.propagate(k)
        if right <= a or b <= left:
            return self.ide_ele
        elif a <= left and right <= b:
            return self.tree[k]
        else:
            vleft = self.query(a, b, k * 2 + 1, left, (left + right) // 2)
            vright = self.query(a, b, k * 2 + 2, (left + right) // 2, right)
            return self.func(vleft, vright)

    def _query(self, a, b):
        return self.query(a, b, 0, 0, self.num)

    def update(self, a, b, x, k, left, right):
        self.propagate(k)
        if a <= left and right <= b:
            self.lazy[k] = x
            self.propagate(k)
        elif a < right and left < b:
            self.update(a, b, x, k * 2 + 1, left, (left + right) // 2)
            self.update(a, b, x, k * 2 + 2, (left + right) // 2, right)
            self.tree[k] = self.func(self.tree[k * 2 + 1], self.tree[k * 2 + 2])

    def _update(self, a, b, x):
        self.update(a, b, x, 0, 0, self.num)


n, q = map(int, input().split())
identity_element = 2 ** 31 - 1
initial_list = [identity_element] * n
function = min
lst = LazySegmentTree(initial_list, function, identity_element)
ans = []
for _ in range(q):
    com = list(map(int, input().split()))
    if com[0] == 0:
        s, t, x = com[1], com[2], com[3]
        lst._update(s, t + 1, x)
    if com[0] == 1:
        s, t = com[1], com[2]
        ans.append(lst._query(s, t + 1))
print(*ans, sep='\n')
