def bubble_sort(N, A):
    flag = 1
    cnt = 0
    while flag:
        flag = 0
        for j in range(1, N):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                cnt += 1
                flag = 1
    return A, cnt


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans_A, ans_cnt = bubble_sort(N, A)
    print(*ans_A)
    print(ans_cnt)


if '__main__' == __name__:
    main()
