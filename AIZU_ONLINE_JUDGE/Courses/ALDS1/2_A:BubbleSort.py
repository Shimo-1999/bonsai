def bubble_sort(a, n):
    global swap_count
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
                swap_count += 1
                flag = True


n = int(input())
a = list(map(int, input().split()))
swap_count = 0
bubble_sort(a, n)
print(*a)
print(swap_count)
