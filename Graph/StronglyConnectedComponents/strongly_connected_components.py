import sys
sys.setrecursionlimit(10 ** 9)


def strongly_connected_components(N, graph, reversed_graph):
    """
    u -> v の有向グラフ
    graph[u] := [v, ...]
    reversed_graph[v] := [u, ...]

    label: int
    group := [label, ...]
    label は topological の昇順
    """

    def dfs(u):
        used[u] = 1
        for v in graph[u]:
            if not used[v]:
                dfs(v)
        order.append(u)

    # 行きがけの dfs. 結果を order に保存.
    order = []
    used = [0 for _ in range(N)]
    for i in range(N):
        if not used[i]:
            dfs(i)

    def reverse_dfs(v, label):
        group[v] = label
        used[v] = 1
        for u in reversed_graph[v]:
            if not used[u]:
                reverse_dfs(u, label)

    # 帰りがけの dfs. 結果を label 付けして group に保存.
    group = [None] * N
    used = [0 for _ in range(N)]
    label = 0
    for i in reversed(order):
        if not used[i]:
            reverse_dfs(i, label)
            label += 1

    return label, group


V, E = map(int, input().split())
graph = [[] for i in range(V)]
reversed_graph = [[] for i in range(V)]
for i in range(E):
    s, t = map(int, input().split())
    graph[s].append(t)
    reversed_graph[t].append(s)

label, group = strongly_connected_components(V, graph, reversed_graph)
answer = [[] for _ in range(label)]
for idx, num in enumerate(group):
    answer[num].append(idx)
print(label)
for ans_i in answer:
    print(len(ans_i), *ans_i)
