"""
doubling[k][i] := i 番目の要素から 2 ** k 先の要素

doubling[k + 1][i] = i 番目の要素から 2 ** (k + 1) 先の要素
                   = (i 番目の要素から 2 ** k 先の要素) から 2 ** k 先の要素
                   = doubling[k][i] 番目の要素から 2 ** k 先の要素
                   = doubling[k][doubling[k][i]]
"""

N, K = map(int, input().split())
a = list(map(int, input().split()))

log_k = 1
while (1 << log_k) <= K:
    log_k += 1

doubling = [[-1 for i in range(N)] for k in range(log_k)]
for i in range(N):
    doubling[0][i] = a[i] - 1
for k in range(log_k - 1):
    for i in range(N):
        doubling[k + 1][i] = doubling[k][doubling[k][i]]

now = 0
for k in range(log_k):
    if K & (1 << k):
        now = doubling[k][now]
print(now + 1)
