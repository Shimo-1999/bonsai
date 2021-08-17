def bellman_ford(n, edges, start):
    """
    edges: [(u, v, cost), ...]
        u -- cost --> v
    """
    # スタートからの距離を初期化
    distance = [float('inf') for i in range(n)]
    distance[start] = 0

    for i in range(n):  # 計算量は 頂点数 * 辺の数
        for u, v, cost in edges:
            # v までの距離が u + cost より大きければ更新
            if distance[v] > distance[u] + cost:
                distance[v] = distance[u] + cost

    # 負閉路の調査
    for _ in range(n):  # 計算量は頂点の数 頂点数 * 辺の数
        for u, v, cost in edges:
            # v までの距離が u + cost より大きければ更新
            if distance[v] > distance[u] + cost:
                distance[v] = -float('inf')

    return distance
