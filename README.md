# Bonsai

---

### BinaryIndexedTree

- binary_indexed_tree  
  普通のやつ
- n_binary_indexed_tree  
  n 次元に拡張できるらしいので．(to do)
- 転倒数  
  binary_indexed_tree を用いて容易に実装できる

### Graph

- bellman_ford
  - 有向グラフの単一始点最短経路（負閉路の発見が可能）
- cayleys
  - n 個のラベル付き頂点を持つ木の個数
- chu_liu_edmond
- dijkstra
  - 単一始点最短経路（辺の重みは非負）
- kruskal
  - 最小全域木を作る．
  - 短い辺から繋いでいく．
- prim
  - 最小全域木を作る．
  - ある頂点から初めて，最短の辺を繋いでいく．
- warshall_floyd
  - 重み付き有向グラフの全ペアの最短経路

### LazySegTree

- range_add_query
- range_update_query

### Mathematics

- math_nandemo  
  約数列挙
  素因数分解
- nCk
- eratosthenes

### Other
- warizan.py
割る数が負の数のとき，あまりを正の数にする（詳しくは，Other/warizan.ipynb）
- todo: その他を書く．

### SegTree

- segtree_add
- segtree

### StronglyConnectedComponents

- scipy_strongly_connected_components
  - scipy を用いた強制連結成分分解．
- strongly_connected_components
  - 強制連結成分分解 graph の再構築も整備．
### UnionFind
- union_find
- wighted_union_find
