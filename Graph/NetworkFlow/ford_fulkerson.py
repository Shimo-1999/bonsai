INF = float('inf')


class FordFulkerson:
    """Maximum Flow"""

    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.graph[fr].append(forward)
        self.graph[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.graph[v1].append(edge1)
        self.graph[v2].append(edge2)

    def _depth_first_search(self, u, sink, f):
        """
        u -> sink の増加路の流量
        """
        if u == sink:
            return f
        self.used[u] = 1
        for edge in self.graph[u]:
            # u -(cap)-> v
            v, cap, rev = edge
            if cap and not self.used[v]:
                d = self._depth_first_search(v, sink, min(f, cap))
                if d:
                    edge[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, source, sink):
        flow = 0
        f = INF
        while f:
            self.used = [0] * self.n
            f = self._depth_first_search(source, sink, INF)
            flow += f
        return flow


n, m = map(int, input().split())
ff = FordFulkerson(n)
for _ in range(m):
    u, v, c = map(int, input().split())
    ff.add_edge(u, v, c)

print(ff.flow(0, n - 1))
