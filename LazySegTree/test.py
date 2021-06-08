def segfunc(x, y):
    return x + y


class RangeUpdateQuery:
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

    def generate_index(self, left, right):
        """
        伝搬される区間のインデックス(1-indexed)を全て列挙する
        """
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
            if v == 0:
                continue
            self.lazy[i] = 0
            self.lazy[2 * i] += v
            self.lazy[2 * i + 1] += v
            self.tree[2 * i] += v
            self.tree[2 * i + 1] += v

    def update(self, left, right, x):
        ids = self.generate_index(left, right)
        self.propagates(*self.generate_index(left, right))
        left += self.num
        right += self.num
        while left < right:
            if left & 1:
                self.lazy[left] = x
                self.tree[left] = x
                left += 1
            if right & 1:
                self.lazy[right - 1] = x
                self.tree[right - 1] = x
            right >>= 1
            left >>= 1
        for i in ids:
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, left, right):
        self.propagates(*self.generate_index(left, right))
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
