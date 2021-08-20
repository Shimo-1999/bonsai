"""Range Update Query"""


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

    def query(self, k):
        k += self.num
        res = self.ide_ele
        while k >= 1:
            res = self.func(res, self.tree[k])
            k >>= 1
        return res

    def update(self, left, right, time, x):
        res = (time, x)
        left += self.num
        right += self.num
        while left < right:
            if left & 1:
                self.tree[left] = res
                left += 1
            if right & 1:
                self.tree[right - 1] = res
            left >>= 1
            right >>= 1


def func(a, b):
    a_time = a[0]
    b_time = b[0]
    if a_time > b_time:
        return a
    else:
        return b


n, q = map(int, input().split())
initial_list = [(-1, 2 ** 31 - 1)] * n
identity_element = (-1, 2 ** 31 - 1)
st = SegmentTree(initial_list, func, identity_element)
for time in range(q):
    com = list(map(int, input().split()))
    if com[0] == 0:
        s, t, x = com[1], com[2], com[3]
        st.update(s, t + 1, time, x)
    if com[0] == 1:
        i = com[1]
        print(st.query(i)[1])
    # print(st.tree)
