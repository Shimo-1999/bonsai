"""
ケイリーの公式（Cayley's formula）正整数 n に対し，n 個のラベル付き頂点を持つ木の個数は n^{n-2} である．
"""


# python 3.8 以降
def numbers_of_tree(n, MOD):
    return pow(n, n - 2, MOD)


# python 3.7 以前
def numbers_of_tree2(n, MOD):
    if n - 2 > 0:
        return pow(n, n - 2, MOD)
    else:
        return 1


print(numbers_of_tree(1, 10 ** 9 + 7))
