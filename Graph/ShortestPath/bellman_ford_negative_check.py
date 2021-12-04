def bellman_ford(n, edges, start):
    """
    edges: [(u, v, cost), ...]
        u -- cost --> v
    """
    # スタートからの距離を初期化
    distance = [float('inf') for _ in range(n)]
    distance[start] = 0

    for i in range(n):  # 計算量は 頂点数 * 辺の数
        update = False
        for u, v, cost in edges:
            # v までの距離が u + cost より大きければ更新
            if distance[v] > distance[u] + cost:
                distance[v] = distance[u] + cost
                update = True

        # 一つも更新がなければ終わり
        if not update:
            break

        # 負のサイクル
        if i == n - 1:
            return -1
    return distance
