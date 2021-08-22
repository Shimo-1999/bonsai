def selection_sort(N, A):
    cnt = 0
    for i in range(N):
        min_j = i
        for j in range(i, N):
            if A[j] < A[min_j]:
                min_j = j
        if i != min_j:
            A[i], A[min_j] = A[min_j], A[i]
            cnt += 1
    return A, cnt


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A, cnt = selection_sort(N, A)
    print(*A)
    print(cnt)


if '__main__' == __name__:
    main()
