class LowestCommonAncestor:
    def __init__(self, n, tree):
        self.p = [[0 for _i in range(n + 10)] for _j in range(20)]
        self.depth = [0 for _ in range(n + 10)]

        for u in range(n):
            for v in tree[u]:
                self.p[0][v] = u
                self.depth[v] = self.depth[self.p[0][v]] + 1

        # doubling
        for i in range(1, 20):
            for v in range(n):
                self.p[i][v] = self.p[i - 1][self.p[i - 1][v]]

    def la(self, x, h):
        for i in reversed(range(20)):
            if h >= 1 << i:
                x = self.p[i][x]
                h -= 1 << i
        return x

    def query(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        u = self.la(u, self.depth[u] - self.depth[v])
        if u == v:
            return u
        for i in reversed(range(20)):
            if self.p[i][u] != self.p[i][v]:
                u = self.p[i][u]
                v = self.p[i][v]
        return self.p[0][u]


N = int(input())
tree = [[] for _ in range(N)]
for i in range(N):
    k_c = list(map(int, input().split()))
    tree[i] += k_c[1:]
lca = LowestCommonAncestor(N, tree)

Q = int(input())
for _ in range(Q):
    u, v = map(int, input().split())
    print(lca.query(u, v))
