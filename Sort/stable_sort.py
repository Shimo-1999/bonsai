def bubble_sort(C, N):
    for i in range(N):
        for j in reversed(range(i + 1, N)):
            if int(C[j][1]) < int(C[j - 1][1]):
                C[j], C[j - 1] = C[j - 1], C[j]
    return C


def selection_sort(C, N):
    for i in range(N):
        min_j = i
        for j in range(i, N):
            if int(C[j][1]) < int(C[min_j][1]):
                min_j = j
        C[i], C[min_j] = C[min_j], C[i]
    return C


def isStable(N, in_, out_):
    for i in range(N):
        for j in range(i + 1, N):
            for a in range(N):
                for b in range(a + 1, N):
                    if (in_[i][1] == in_[j][1]) & (in_[i] == out_[b]) & (in_[j] == out_[a]):
                        return False
    return True


def main():
    N = int(input())
    C = list(map(str, input().split()))
    C_bu = []
    C_se = []
    for i in C:
        C_bu.append(i)
        C_se.append(i)

    C_bubble = bubble_sort(C_bu, N)
    print(*C_bubble)
    if isStable(N, C, C_bubble):
        print('Stable')
    else:
        print('Not stable')

    C_selection = selection_sort(C_se, N)
    print(*C_selection)
    if isStable(N, C, C_selection):
        print('Stable')
    else:
        print('Not stable')


if '__main__' == __name__:
    main()
