import sys
sys.setrecursionlimit(10000000)


class LowLink:
    def __init__(self, V, graph):
        """
        ord[i]: 頂点 i の訪問順序
        low[i]: 頂点 i のlowlink
        """
        self.ord = [-1] * V
        self.low = [-1] * V
        self.graph = graph
        self.V = V
        self.parent = [-1] * V

        def depth_first_search(u):
            self.ord[u] = self.time
            self.low[u] = self.time
            self.time += 1
            for v in self.graph[u]:
                if self.low[v] < 0:
                    self.parent[v] = u
                    depth_first_search(v)
                    self.low[u] = min(self.low[u], self.low[v])
                elif v != self.parent[u]:
                    self.low[u] = min(self.low[u], self.ord[v])

        self.time = 0
        depth_first_search(0)

    def articulation_points(self):
        """
        関節点:
            1. u が DFS の根で，子が二つ以上存在
            2. u が DFS の根でなく，頂点 u のある子 v について ord[u] <= low[v] を満たす
        """
        aps = set()
        # 0 を親とする子が二つ以上存在したら追加
        if self.parent.count(0) >= 2:
            aps.add(0)

        for v in range(self.V):
            u = self.parent[v]
            # DFS の走査時の辺 u -> v を調べる
            # 「v に親が存在しないとき」　または 「u が DFS の根のとき」は continue
            if u == -1 or u == 0:
                continue
            if self.ord[u] <= self.low[v]:
                aps.add(u)
        return aps

    def bridges(self):
        """
        橋: ord[u] < low[v] を満たす辺
        """
        bridge_edges = set()

        # 辺 (u, v) を調べる
        for u in range(self.V):
            for v in self.graph[u]:
                if self.ord[u] < self.low[v]:
                    if u > v:
                        bridge_edges.add((v, u))
                    else:
                        bridge_edges.add((u, v))
        return bridge_edges


V, E = map(int, input().split())
graph = [[] for _ in range(V)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

lowlink = LowLink(V, graph)
ans = list(lowlink.articulation_points())
ans.sort()
for u in ans:
    print(u)
