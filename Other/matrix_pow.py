MOD = 1_000_000_007


def matrix_product(mat1, mat2, mod):
    """
    mat1: n * k 行列
    mat2: k * m 行列
    """
    n = len(mat1)
    k = len(mat1[0])
    m = len(mat2[0])

    ret = [[0 for _j in range(m)] for _i in range(n)]
    for i in range(n):
        for j in range(m):
            for kk in range(k):
                ret[i][j] += (mat1[i][kk] * mat2[kk][j]) % mod

    return ret


N = int(input())
now = [[2, 1], [1, 0]]

ans = [[0 for _i in range(2)] for _i in range(2)]
for i in range(2):
    ans[i][i] = 1

k = N - 2
while k:
    if k & 1:
        ans = matrix_product(ans, now, MOD)
    now = matrix_product(now, now, MOD)
    k >>= 1

print((ans[0][0] + ans[0][1]) % MOD)
