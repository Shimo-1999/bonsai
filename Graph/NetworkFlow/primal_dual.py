INF = float('inf')


class PrimalDual:
    """
    Minimum Cost Flow
    PrimalDual with bellman ford
    """

    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u, v, cap, cost):
        """
        u -(cap, cost)-> v
        """
        forward = [v, cap, cost, None]
        backward = forward[3] = [u, 0, -cost, forward]
        self.graph[u].append(forward)
        self.graph[v].append(backward)

    def minimum_cost_flow(self, source, sink, f):
        flow = 0
        prev_node = [0 for _ in range(self.n)]
        prev_edge = [None for _ in range(self.n)]

        while f:
            # bellman ford で最短路
            dist = [INF for _ in range(self.n)]
            dist[source] = 0
            update = True
            while update:
                update = False
                for u in range(self.n):
                    if dist[u] == INF:
                        continue
                    for i in range(len(self.graph[u])):
                        v, cap, cost, _ = self.graph[u][i]
                        if cap > 0 and dist[v] > dist[u] + cost:
                            dist[v] = dist[u] + cost
                            prev_node[v] = u
                            prev_edge[v] = i
                            update = True

            if dist[sink] == INF:
                return -1

            # sink から source まで経路復元 & flow に足す
            d = f
            v = sink
            while v != source:
                d = min(d, self.graph[prev_node[v]][prev_edge[v]][1])
                v = prev_node[v]
            f -= d
            flow += d * dist[sink]
            v = sink
            while v != source:
                edge = self.graph[prev_node[v]][prev_edge[v]]
                edge[1] -= d  # source -> sink の cap から d(実際に流した flow) を引く
                edge[3][1] += d  # sink -> source の cap に d(実際に流した flow) を足す
                v = prev_node[v]

        return flow


V, E, F = map(int, input().split())
pd = PrimalDual(V)
for i in range(E):
    u, v, c, d = map(int, input().split())
    pd.add_edge(u, v, c, d)
flow = pd.minimum_cost_flow(0, V - 1, F)

if flow is None:
    print(-1)
else:
    print(flow)
