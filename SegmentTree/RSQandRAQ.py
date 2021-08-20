"""Range Sum Query & Range Add Query"""
import sys
input = sys.stdin.readline


class LazySegmentTree:
    def __init__(self, initial_list, function, identity_element):
        n = len(initial_list)
        self.tree_height = (n - 1).bit_length()
        self.num = 2 ** self.tree_height
        self.func = function
        self.ide_ele = identity_element
        self.tree = [self.ide_ele] * 2 * self.num
        self.lazy = [0] * 2 * self.num

        # for i in range(n):
        # self.tree[self.num + i] = initial_list[i]
        # for i in range(self.num - 1, 0, -1):
        # self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def generate_index(self, left, right):
        """
        遅延伝播するインデックスを収集
        最下層から上に調べていく
        """
        # 最下層の伝播範囲のインデックス [L, R)
        i_left = left + self.num
        i_right = right + self.num

        # bit列で右側から見て連続してる 0 の数 (Number of Training Zero)
        l_ntz = (i_left & -i_left).bit_length() - 1
        r_ntz = (i_right & -i_right).bit_length() - 1

        indexes = []
        for i in range(self.tree_height):
            # 下から i 番目の伝播範囲のインデックス [L, R)
            i_left //= 2
            i_right //= 2
            if r_ntz <= i:
                indexes.append(i_right)
            if i_left < i_right and l_ntz <= i:
                indexes.append(i_left)
        return indexes

    def propagate(self, indexes):
        """遅延伝播"""
        # 上から下に伝播するので reversed になっています
        for i in reversed(indexes):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[2 * i] += v >> 1
            self.tree[2 * i] += v >> 1
            self.lazy[2 * i + 1] += v >> 1
            self.tree[2 * i + 1] += v >> 1
            self.lazy[i] = 0

    def update(self, left, right, x):
        """区間 [left, right) を x で更新"""
        indexes = self.generate_index(left, right)
        self.propagate(indexes)

        # 遅延伝播が済んだので最下層から x に update
        left += self.num
        right += self.num
        while left < right:
            if right & 1:
                self.lazy[right - 1] += x
                self.tree[right - 1] += x
            if left & 1:
                self.lazy[left] += x
                self.tree[left] += x
                left += 1
            left //= 2
            right //= 2
            x <<= 1
        # 下層から tree の内容を update
        for i in indexes:
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, left, right):
        """[L, R) の範囲の func の結果を得る"""
        indexes = self.generate_index(left, right)
        self.propagate(indexes)
        # 遅延伝播が済んだので最下層から調べて query の答えを得る
        left += self.num
        right += self.num
        res = self.ide_ele
        while left < right:
            if right & 1:
                res = self.func(res, self.tree[right - 1])
            if left & 1:
                res = self.func(res, self.tree[left])
                left += 1
            left >>= 1
            right >>= 1
        return res


def function(a, b):
    return a + b


n, q = map(int, input().split())
identity_element = 0
initial_list = [identity_element] * n
lst = LazySegmentTree(initial_list, function, identity_element)
ans = []
for _ in range(q):
    com = list(map(int, input().split()))
    if com[0] == 0:
        s, t, x = com[1], com[2], com[3]
        lst.update(s - 1, t, x)
    if com[0] == 1:
        s, t = com[1], com[2]
        ans.append(lst.query(s - 1, t))
    # print(lst.tree)
print(*ans, sep='\n')
