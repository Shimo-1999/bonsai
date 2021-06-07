def bit_search(n: int, lst: list) -> list:
    bit_list = []
    for i in range(2 ** n):
        bit_j = []
        for j in range(n):
            if ((i >> j) & 1):
                bit_j.append(lst[j])
        bit_list.append(bit_j)
    return bit_list
