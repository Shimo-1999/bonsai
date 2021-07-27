import sys
sys.setrecursionlimit(10 ** 9)


def strongly_connected_components(N, graph, reversed_graph):
    """
    u -> v の有向グラフ
    graph[u] := [v, ...]
    reversed_graph[v] := [u, ...]

    label: int
    group := [label, ...]
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


def reconstruct_graph(N, graph, label, group):
    """
    強制連結分解後のグラフを構築

    components[label] := [a, b, c, ...]
    labeled_graph[label_u] := set(label_v, ...)
    """
    labeled_graph = [set() for i in range(label)]
    components = [[] for i in range(label)]
    for u in range(N):
        label_u = group[u]
        components[label_u].append(u)
        for v in graph[u]:
            label_v = group[v]
            if label_u == label_v:
                continue
            labeled_graph[label_u].add(label_v)
    return components, labeled_graph


V, E = map(int, input().split())
graph = [[] for i in range(V)]
reversed_graph = [[] for i in range(V)]
for i in range(E):
    s, t = map(int, input().split())
    graph[s].append(t)
    reversed_graph[t].append(s)
# print(graph)
# print(reversed_graph)

label_num, group = strongly_connected_components(V, graph, reversed_graph)
# print(label_num, group)
componets, labeled_graph = reconstruct_graph(V, graph, label_num, group)
for i in componets:
    print(i)

for i in labeled_graph:
    print(i)
