import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components


def strongly_connected_components(V, E, edges):
    """
    u -> v の有向辺
    edges: [(u, v), ...]

    label: int = 種類数
    group: [label, ...]
    label は topological の降順
    """
    edge = np.array(edges, dtype=np.int64).T
    tmp = np.ones(E, dtype=np.int64).T

    # 疎行列に変換 -> [((u, v), weight), ...]
    graph = csr_matrix((tmp, (edge)), (V, V))
    label, group = connected_components(graph, directed=True, connection='strong')

    return label, group


V, E = map(int, input().split())
edges = []
for i in range(E):
    u, v = map(int, input().split())
    edges.append([u, v])

label, group = strongly_connected_components(V, E, edges)
answer = [[] for _ in range(label)]
for idx, num in enumerate(group):
    answer[num].append(idx)
print(label)
for ans_i in reversed(answer):
    print(len(ans_i), *ans_i)
