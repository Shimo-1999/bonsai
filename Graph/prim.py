from heapq import heapify, heappop, heappush


def prim(n, graph, start):
    """
    graph[u]: [(weight, v), ...]
        u -- weight --> v
    """
    # 初期化
    seen = [0 for _ in range(n)]
    seen[start] = 1

    minimum_spanning_tree_sum = 0
    connected_nodes = 0

    # これから調べる頂点の (重み, 点)
    # q = [(weight_a, a), (weight_b, b), ...]
    q = graph[start]
    heapify(q)
    while q:
        weight_u, u = heappop(q)

        # 頂点 u が確定済みでなければ u への辺を追加
        if seen[u]:
            continue
        seen[u] = 1
        connected_nodes += 1
        minimum_spanning_tree_sum += weight_u

        # 新たに繋げた頂点 u から行ける頂点 v を enqueue
        for weight_v, v in graph[u]:
            heappush(q, (weight_v, v))

        # 全部のノードが繋がったら終了
        if connected_nodes == n:
            break
    return minimum_spanning_tree_sum
