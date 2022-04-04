def k_zentansaku(n, k):
    """
    k ** n 個の重複順列を生成
    k = 2 なら bit 全探索
    """
    ret = [[None for _j in range(n)] for _i in range(k ** n)]
    for i in range(k ** n):
        tmp = i
        for j in reversed(range(n)):
            ret[i][j] = tmp % k
            tmp //= k
    return ret


k = 4
n = 3
print(k_zentansaku(n, k))

# これと同じなのでいらないかもです
import itertools
print(list(itertools.product(range(k), repeat=n)))
