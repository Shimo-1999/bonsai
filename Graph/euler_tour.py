import sys
sys.setrecursionlimit(10 ** 9)


def euler_tour(N, graph):
    begin = [-1] * N
    end = [-1] * N
    euler_tour = []

    def depth_first_search(u, p):
        nonlocal time
        begin[u] = time
        euler_tour.append(u)
        time += 1
        for v in graph[u]:
            if p != v and begin[v] == -1:
                depth_first_search(v, u)
                euler_tour.append(u)
                time += 1
        end[u] = time

    time = 0
    depth_first_search(0, -1)
    return euler_tour, begin, end


N = int(input())
graph = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
for i in range(N):
    graph[i].sort()
e_tour, _, _ = euler_tour(N, graph)
ans = []
for i in e_tour:
    ans.append(i + 1)
print(*ans)
