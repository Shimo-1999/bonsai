def selection_sort(a, n):
    global swap_count
    for i in range(n):
        min_j = i
        for j in range(i, n):
            if a[j] < a[min_j]:
                min_j = j
        if i != min_j:
            a[i], a[min_j] = a[min_j], a[i]
            swap_count += 1


n = int(input())
a = list(map(int, input().split()))
swap_count = 0
selection_sort(a, n)
print(*a)
print(swap_count)
