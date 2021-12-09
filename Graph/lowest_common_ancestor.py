class LowestCommonAncestor:
    def __init__(self, n, tree):

        self.log_K = 1
        while 1 << self.log_K <= n:
            self.log_K += 1

        # p[k][i] := i 番目の要素から 2 ** k 個親の要素
        self.p = [[0 for _i in range(n)] for _k in range(self.log_K)]
        self.depth = [0 for _ in range(n)]

        for u in range(n):
            for v in tree[u]:
                self.p[0][v] = u
                self.depth[v] = self.depth[self.p[0][v]] + 1

        # doubling
        for k in range(self.log_K - 1):
            for i in range(n):
                self.p[k + 1][i] = self.p[k][self.p[k][i]]

    def level_ancestor(self, v, h):
        """頂点 v の h 個親"""
        for k in reversed(range(self.log_K)):
            if h & (1 << k):
                v = self.p[k][v]
        return v

    def query(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        # 高さを揃える
        u = self.level_ancestor(u, self.depth[u] - self.depth[v])
        if u == v:
            return u
        for k in reversed(range(self.log_K)):
            if self.p[k][u] != self.p[k][v]:
                u = self.p[k][u]
                v = self.p[k][v]
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
