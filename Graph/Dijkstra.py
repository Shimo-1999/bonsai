from heapq import heappush, heappop


def dijkstra(n, graph, start):
    """
    graph[u] := [(cost, v), ...]
    """
    distance = [float('inf') for _ in range(n)]
    distance[start] = 0
    Q = [(0, start)]
    while Q:
        u_cost, u = heappop(Q)
        if u_cost > distance[u]:
            continue
        for cost, v in graph[u]:
            if distance[v] > distance[u] + cost:
                distance[v] = distance[u] + cost
                heappush(Q, (distance[v], v))
    return distance


def dijkstra_test(n, graph, start):
    """
    graph[u] := [(cost, v), ...]
        u -- cost --> v
    """
    # 初期化
    distance = [float('inf') for _ in range(n)]
    distance[start] = 0
    # 始点を queue に追加
    Q = [(0, start)]
    while Q:
        u_cost, u = heappop(Q)
        # u_cost が u までの距離より大きかったら破棄
        if u_cost > distance[u]:
            continue
        # u に更新があれば行けるところも更新
        for cost, v in graph[u]:
            # v までの距離が u + cost より大きかったら更新して queue に追加
            if distance[v] > distance[u] + cost:
                distance[v] = distance[u] + cost
                heappush(Q, (distance[v], v))
    return distance
