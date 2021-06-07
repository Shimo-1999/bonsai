# ベルマンフォード法
def BF(p, n, s):
    """
    p: (start, goal cost)
    n: 頂点の数
    s: start
    """
    inf = float("inf")
    d = [inf for i in range(n)]
    d[s - 1] = 0
    for i in range(n + 1):
        for e in p:
            if e[0] != inf and d[e[1] - 1] > d[e[0] - 1] + e[2]:
                d[e[1] - 1] = d[e[0] - 1] + e[2]
        if i == n - 1:
            t = d[-1]
        if i == n and t != d[-1]:
            return [0, 'inf']
    return list(map(lambda x: -x, d))


n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
a = [[x, y, -z] for x, y, z in a]
print(BF(a, n, 1)[-1])

# O(EV)


def bellman_ford(p, n, s):
    """
    p: (start, goal cost)
    n: 頂点の数
    s: start
    """
    d = [float('inf')] * n  # 各頂点への最小コスト
    d[s] = 0  # 自身への距離は0
    for i in range(n):
        update = False  # 更新が行われたか
        for x, y, z in g:
            if d[y] > d[x] + z:
                d[y] = d[x] + z
                update = True
        if not update:
            break
        # 負閉路が存在
        if i == n - 1:
            return -1
    return d


n, w = [int(x) for x in input().split()]  # n:頂点数, w:辺の数
g = []
for _ in range(w):
    x, y, z = [int(x) for x in input().split()]  # 始点,終点,コスト
    g.append([x, y, z])
    g.append([y, x, z])  # 有向グラフでは削除
print(bellman_ford(0))
