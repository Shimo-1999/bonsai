"""Range Minimum Query"""


class SegmentTree():
    def __init__(self, initial_list, function, identity_element):
        n = len(initial_list)
        self.func = function
        self.ide_ele = identity_element
        self.num = 1 << (n - 1).bit_length()
        self.tree = [identity_element] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = initial_list[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.func(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def add(self, k, x):
        self.update(k, self.tree[self.num + k] + x)

    def query(self, left, right):
        res = self.ide_ele
        left += self.num
        right += self.num
        while left < right:
            if left & 1:
                res = self.func(res, self.tree[left])
                left += 1
            if right & 1:
                res = self.func(res, self.tree[right - 1])
            left >>= 1
            right >>= 1
        return res


n, q = map(int, input().split())
init_val = [2 ** 31 - 1] * n
ide_ele = 2 ** 31 - 1
st = SegmentTree(init_val, min, ide_ele)

for i in range(q):
    com = list(map(int, input().split()))
    if com[0] == 0:
        i, x = com[1], com[2]
        st.update(i, x)
    if com[0] == 1:
        s, t = com[1], com[2]
        print(st.query(s, t + 1))
