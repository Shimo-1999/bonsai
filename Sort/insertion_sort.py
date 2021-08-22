def insertion_sort(N, A):
    for i in range(len(A)):
        v = A[i]
        j = i - 1
        while (j >= 0) & (A[j] > v):
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
        print(*A)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    insertion_sort(N, A)


if '__main__' == __name__:
    main()
