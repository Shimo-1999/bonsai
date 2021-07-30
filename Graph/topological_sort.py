from collections import deque


def topological_sort(N, graph, indegree):
    """
    graph[u]: [v, ...]
    indegree(入次数): [int, ...]

    sorted_lst: [int, ...]
    """
    sorted_lst = []

    # 入次数が 0 のものを追加
    q = deque([])
    for i in range(N):
        if indegree[i] == 0:
            q.append(i)

    while q:
        u = q.pop()
        sorted_lst.append(u)

        for v in graph[u]:
            # u から v への辺を消去
            indegree[v] -= 1
            # v の入次数が 0 なら q に追加
            if indegree[v] == 0:
                q.append(v)

    return sorted_lst


N, E = map(int, input().split())
graph = [[] for i in range(N)]
# 頂点の入次数を持っておく
indegree = [0 for _ in range(N)]
for i in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    indegree[v] += 1

ans = topological_sort(N, graph, indegree)
for i in ans:
    print(i)
