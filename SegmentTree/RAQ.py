"""Range Add Query"""


class SegmentTree():
    def __init__(self, initial_list, identity_element):
        n = len(initial_list)
        # self.func = function
        self.ide_ele = identity_element
        self.num = 1 << (n - 1).bit_length()
        self.tree = [identity_element] * 2 * self.num
        # for i in range(n):
        # self.tree[self.num + i] = initial_list[i]
        # for i in range(self.num - 1, 0, -1):
        # self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, k):
        k += self.num
        res = 0
        while k >= 1:
            res += self.tree[k]
            k >>= 1
        return res

    def update(self, left, right, x):
        left += self.num
        right += self.num
        while left < right:
            if left & 1:
                self.tree[left] += x
                left += 1
            if right & 1:
                self.tree[right - 1] += x
            left >>= 1
            right >>= 1


n, q = map(int, input().split())
initial_list = [0] * n
identity_element = 0
st = SegmentTree(initial_list, identity_element)
for _ in range(q):
    com = list(map(int, input().split()))
    if com[0] == 0:
        s, t, x = com[1], com[2], com[3]
        st.update(s - 1, t, x)
    if com[0] == 1:
        i = com[1] - 1
        print(st.query(i))
    # print(st.tree)
