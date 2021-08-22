def insertion_sort(A, n, g):
    for i in range(g, n):
        v = A[i]
        j = i - g
        while (j >= 0) & (A[j] > v):
            A[j + g] = A[j]
            j = j - g
            cnt += 1
        A[j + g] = v


def shell_sort(A, n):
    global cnt, m, G
    cnt = 0
    m = n // 5
    G = list(range(1, m + 1))
    for i in range(m):
        insertion_sort(A, n, G[i])


def main():
    n = int(input())
    A = list(map(int, input().split()))
    shell_sort(A, n)
    print(m)
    print(*G)
    print(cnt)
    print(*A, sep='\n')


if '__main__' == __name__:
    main()
