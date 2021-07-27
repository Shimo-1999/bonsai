from heapq import heapify, heappop, heappush


def prim(n, graph, start):
    """
    graph[u] := [(weight, v), ...]
    """
    # 初期化
    seen = [0 for _ in range(n)]
    seen[start] = 1

    minimum_spanning_tree_sum = 0
    connected = 0

    # 確定済みの木に繋がっている (重み, 点)
    # q := [(weight_a, a), (weight_b, b), ...]
    q = graph[start]
    heapify(q)
    while q:
        weight, u = heappop(q)

        # 頂点 t が確定済みでなければ t への辺を追加
        if seen[u]:
            continue
        seen[u] = 1
        connected += 1
        minimum_spanning_tree_sum += weight

        # 新たに繋げたノードから行けるところを enqueue
        for weight, v in graph[u]:
            heappush(q, (weight, v))

        # 全部のノードが繋がったら終了
        if connected == n:
            break
    return minimum_spanning_tree_sum
