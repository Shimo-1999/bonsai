from collections import deque

INF = float('inf')


class Dinic:
    """Max Flow"""

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

    def _breadth_first_search(self, source, sink):
        self.level = [None] * self.n
        self.level[source] = 0
        q = deque([source])
        while q:
            u = q.popleft()
            u_level = self.level[u] + 1
            for v, cap, _ in self.graph[u]:
                if cap and self.level[v] is None:
                    self.level[v] = u_level
                    q.append(v)
        return self.level[sink] is not None

    def _depth_first_search(self, u, sink, f):
        """
        u -> sink の増加路の流量
        """
        if u == sink:
            return f
        for edge in self.graph[u]:
            v, cap, rev = edge
            if cap and self.level[u] < self.level[v]:
                d = self._depth_first_search(v, sink, min(f, cap))
                if d:
                    edge[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, source, sink):
        flow = 0
        # 幅優先探索で source から sink に到達できるうちは増加路が存在
        while self._breadth_first_search(source, sink):
            f = INF
            # 増加路を検出
            while f:
                f = self._depth_first_search(source, sink, INF)
                flow += f
        return flow


n, m = map(int, input().split())
dinic = Dinic(n)
for _ in range(m):
    u, v, c = map(int, input().split())
    dinic.add_edge(u, v, c)

print(dinic.flow(0, n - 1))
