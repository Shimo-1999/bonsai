"""
頂点 r を根とする最小全域有向木を求める.
計算量は O(E log V)
"""


def Chu_Liu_Edmond(V: int, r: int, es: list) -> int:
    """
    V := 頂点の数
    r := 始点
    es := リスト
    """
    # mins[t] := t から到着する path で最も軽いやつ
    mins = [(float('inf'), -1)] * V
    for s, t, w in es:
        mins[t] = min(mins[t], (w, s))
    mins[r] = (-1, -1)

    group = [0] * V
    comp = [0] * V
    cnt = 0

    used = [0] * V
    for v in range(V):
        if not used[v]:
            chain = []
            cur = v
            # スタートじゃないかつ、通ってもない
            while cur != -1 and not used[cur]:
                chain.append(cur)
                used[cur] = 1
                cur = mins[cur][1]
            if cur != -1:
                cycle = 0
                for e in chain:
                    group[e] = cnt
                    if e == cur:
                        cycle = 1
                        comp[cnt] = 1
                    if not cycle:
                        cnt += 1
                if cycle:
                    cnt += 1
            else:
                for e in chain:
                    group[e] = cnt
                    cnt += 1

    if cnt == V:
        return sum(map(lambda x: x[0], mins)) + 1

    res = sum(mins[v][0] for v in range(V) if v != r and comp[group[v]])

    n_es = []
    for s, t, w in es:
        gs = group[s]
        gt = group[t]
        if gs == gt:
            continue
        if comp[gt]:
            n_es.append((gs, gt, w - mins[t][0]))
        else:
            n_es.append((gs, gt, w))
    return res + Chu_Liu_Edmond(cnt, group[r], n_es)


def main():
    V, E, r = map(int, input().split())
    lst = []
    for i in range(E):
        s, t, w = map(int, input().split())
        lst.append((s, t, w))

    ans = Chu_Liu_Edmond(V, r, lst)
    print(ans)


if '__main__' == __name__:
    main()
