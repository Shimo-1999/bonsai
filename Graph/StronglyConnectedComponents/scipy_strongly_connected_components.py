import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components


def strongly_connected_components(graph):
    """
    graph: scipy.sparse.csr.csr_matrix (疎行列)

    label: int
    group: [label, ...]
    """
    label, group = connected_components(graph, directed=True, connection='strong')

    return label, group


V, E = map(int, input().split())
lst = []
for i in range(E):
    u, v = map(int, input().split())
    lst.append([u, v])

edge = np.array(lst, dtype=np.int64).T
tmp = np.ones(E, dtype=np.int64).T

# 疎行列に変換 -> [((u, v), weight), ...]
graph = csr_matrix((tmp, (edge)), (V, V))
label, group = strongly_connected_components(graph)
Q = int(input())
for i in range(Q):
    u, v = map(int, input().split())
    print(int(group[u] == group[v]))
