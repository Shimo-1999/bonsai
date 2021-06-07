from copy import copy
# V: 頂点数
# g[v] = {(w, cost)}:
#     頂点vから遷移可能な頂点(w)とそのコスト(cost)
# r: 始点の頂点

from heapq import heappush, heappop
INF = 10**10


def dijkstra(N, G, s):
    global dist
    dist = [INF] * N
    que = [(0, s)]
    dist[s] = 0
    while que:
        c, v = heappop(que)
        if dist[v] < c:
            continue
        for t, cost in G[v]:
            if dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                heappush(que, (dist[t], t))


N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    G[a - 1].append((b - 1, c))
    G[b - 1].append((a - 1, c))
GG = copy(G)
dijkstra(N, G, 0)
A = dist
dijkstra(N, GG, N - 1)
B = dist
for i, j in zip(A, B):
    print(i + j)
