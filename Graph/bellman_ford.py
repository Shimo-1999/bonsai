def bellman_ford(n, graph, start):
    """
    graph[u]: [(cost, v), ...]
    """
    # スタートからの距離を初期化
    distance = [float('inf') for i in range(n)]
    distance[start] = 0

    for i in range(n):  # 計算量は頂点の数 O(N)
        update = False
        for u in range(n):  # 以下の計算量は辺の数 O(E)
            for cost, v in graph[u]:
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
