def segfunc(x, y):
    return max(x, y)


class RangeAddQuery:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        self.lazy = [0] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def gindex(self, left, right):
        left += self.num
        right += self.num
        lm = left >> (left & -left).bit_length()
        rm = right >> (right & -right).bit_length()
        while right > left:
            if left <= lm:
                yield left
            if right <= rm:
                yield right
            right >>= 1
            left >>= 1
        while left:
            yield left
            left >>= 1

    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if not v:
                continue
            self.lazy[2 * i] += v
            self.lazy[2 * i + 1] += v
            self.tree[2 * i] += v
            self.tree[2 * i + 1] += v
            self.lazy[i] = 0

    def update(self, left, right, x):
        ids = self.gindex(left, right)
        self.propagates(*self.gindex(left, right))
        left += self.num
        right += self.num
        while left < right:
            if left & 1:
                self.lazy[left] += x
                self.tree[left] += x
                left += 1
            if right & 1:
                self.lazy[right - 1] += x
                self.tree[right - 1] += x
            right >>= 1
            left >>= 1
        for i in ids:
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, left, right):
        # ids = self.gindex(left, right)
        self.propagates(*self.gindex(left, right))
        res = self.ide_ele
        left += self.num
        right += self.num
        while left < right:
            if left & 1:
                res = self.segfunc(res, self.tree[left])
                left += 1
            if right & 1:
                res = self.segfunc(res, self.tree[right - 1])
            left >>= 1
            right >>= 1
        return res


n, q = map(int, input().split())
ans = []
RUQ = RangeAddQuery([0] * n, segfunc, 0)
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        s, t, x = query[1], query[2], query[3]
        RUQ.update(s - 1, t, x)
    else:
        i = query[1]
        RUQ.query(i - 1, i)
        ans.append(RUQ.tree[RUQ.num + i - 1])
for i in range(len(ans)):
    print(ans[i])
