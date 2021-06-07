from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, M, X, Y = map(int, input().split())


def aaa(du, time):
    if du % time == 0:
        return du // time
    else:
        return du // time + 1


p = {i: [] for i in range(N)}
for i in range(M):
    A, B, T, K = map(int, input().split())
    p[A - 1].append((B - 1, T, K))
    p[B - 1].append((A - 1, T, K))

d = [float('inf') for i in range(N)]
d[X - 1] = 0

prev = [None] * N
q = []
heappush(q, (d[X - 1], X - 1))
cnt = 0
while q:
    # print(q, d, prev)
    du, u = heappop(q)
    if d[u] < du:
        continue
    for v, weight, time in p.get(u, []):
        # print(v, weight)
        # 要修正
        alt = aaa(du, time) * time + weight
        # print(u, v, du, aaa(du, time) * time, weight)
        if d[v] > alt:
            d[v] = alt
            prev[v] = u
            heappush(q, (alt, v))


if d[Y - 1] == float('inf'):
    print(-1)
else:
    print(d[Y - 1])
