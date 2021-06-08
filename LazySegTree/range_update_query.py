def segfunc(x, y):
    return x + y


class RangeUpdateQuery:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        self.lazy = [None] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def gindex(self, l, r):
        l += self.num
        r += self.num
        lm = l >> (l & -l).bit_length()
        rm = r >> (r & -r).bit_length()
        while r > l:
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1

    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[i] = None
            self.lazy[2 * i] = v
            self.lazy[2 * i + 1] = v
            self.tree[2 * i] = v
            self.tree[2 * i + 1] = v

    def update(self, l, r, x):
        ids = self.gindex(l, r)
        self.propagates(*self.gindex(l, r))
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                self.lazy[l] = x
                self.tree[l] = x
                l += 1
            if r & 1:
                self.lazy[r - 1] = x
                self.tree[r - 1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l, r):
        ids = self.gindex(l, r)
        self.propagates(*self.gindex(l, r))
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


n, q = map(int, input().split())
ans = []
RUQ = RangeUpdateQuery([0] * n, segfunc, 0)
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        s, t, x = query[1], query[2], query[3]
        print(f'[{s}, {t + 1}) is {x}')
        RUQ.update(s, t + 1, x)
    else:
        left, right = query[1], query[2]
        print(f'[{left}, {right + 1})')
        ans.append(RUQ.query(left, right + 2))
    print('tree', RUQ.tree[0])
    print('lazy', RUQ.lazy[0])
    print('tree', RUQ.tree[1:3])
    print('lazy', RUQ.lazy[1:3])
    print('tree', RUQ.tree[3:7])
    print('lazy', RUQ.lazy[3:7])
    print('tree', RUQ.tree[8:17])
    print('lazy', RUQ.lazy[8:17])
    print(RUQ.tree[RUQ.num:])
    print()
for i in range(len(ans)):
    print(ans[i])
