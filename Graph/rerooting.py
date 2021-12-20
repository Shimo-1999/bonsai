import sys
sys.setrecursionlimit(10 ** 9)


n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

sub_tree = [1 for _ in range(n)]
value = [0 for _ in range(n)]


def dfs_root0(u, parent):
    for v in graph[u]:
        if v == parent:
            continue
        dfs_root0(v, u)
        sub_tree[u] += sub_tree[v]
        value[u] += value[v] + sub_tree[v]


dfs_root0(0, -1)
ans = [0 for _ in range(n)]
ans[0] = value[0]


def dfs(u, parent):
    for v in graph[u]:
        if v == parent:
            continue
        ans[v] = ans[u] + n - 2 * sub_tree[v]
        dfs(v, u)


dfs(0, -1)
print(*ans, sep='\n')
