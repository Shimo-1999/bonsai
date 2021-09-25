"""
スライド最小値
https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_3_D
自分で思いつかなかったので, とっておく.
一次元のものなら応用できそう
"""
from collections import deque

n, l = map(int, input().split())
a = list(map(int, input().split()))

d = deque([])
for i in range(l - 1):
    # l - 1 までの a[i] を昇順に保つような index を保管
    while d and (a[d[-1]] >= a[i]):
        d.pop()
    d.append(i)


# 実際に b を求めていく
b = []
for i in range(l - 1, n):
    # a を昇順に保つような index を保管
    # これに a[i] を追加
    while d and a[d[-1]] >= a[i]:
        d.pop()
    d.append(i)

    if d[0] == i - l:
        d.popleft()

    # d の一番前の値が a の [i - l, i] の範囲の最小値を取る index
    b_i = d[0]
    b.append(a[b_i])


print(*b)
