"""
Prim's algorithmは
グラフ理論で重み付き連結グラフの最小全域木を求める最適化のアルゴリズム
木から出ている辺群で, 最も重みが小さいものを選んで繋げていく.

優先度付きキューと隣接リストで O(E + V log V)
"""

import heapq


def prim(n: int, s: int, graph: list) -> int:
    """
    n := 頂点の数
    s := スタートの場所
    graph := グラフの隣接リスト
    """
    seen = [0 for _ in range(n)]
    seen[s] = 1
    q = graph[s]
    heapq.heapify(q)
    ans = 0
    connected = 0
    while len(q):
        print(q)
        weight, t = heapq.heappop(q)
        if seen[t]:
            continue

        seen[t] = 1
        connected += 1
        ans += weight

        # 新たに繋げたノードから行けるところをエンキュー
        for i in graph[t]:
            heapq.heappush(q, i)

        # 全部のノードが繋がったら終了
        if connected == n:
            break
    return ans


def main():
    V, E, r = map(int, input().split())
    graph = [[] for _ in range(V)]
    for _ in range(E):
        s, t, w = map(int, input().split())
        graph[s].append((w, t))
        graph[t].append((w, s))
    print(graph)

    print(prim(V, r, graph))


if '__main__' == __name__:
    main()
