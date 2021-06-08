def k_bit_zentansaku(k, n):
    """
    k ** n の全探索を行う
    """
    ret = []
    for i in range(k ** n):
        tmp = i
        lst = [0 for i in range(n)]
        for j in range(n):
            lst[j] = tmp % k
            tmp //= k
        ret.append(lst)
    return ret


k = 3
n = 3
print(k_bit_zentansaku(k, n))
