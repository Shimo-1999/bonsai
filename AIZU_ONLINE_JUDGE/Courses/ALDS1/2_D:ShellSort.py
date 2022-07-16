def insertion_sort(a, n, g):
    global count
    for i in range(g, n):
        v = a[i]
        j = i - g
        while j >= 0 and a[j] > v:
            a[j + g] = a[j]
            j = j - g
            count += 1
        a[j + g] = v


n = int(input())
a = []
for i in range(n):
    a_i = int(input())
    a.append(a_i)

# shell sort
count = 0
G = [1]
tmp = 1
while G[-1] + 3**tmp < n:
    G.append(G[-1] + 3**tmp)
    tmp += 1
G.reverse()
m = len(G)
for i in range(m):
    insertion_sort(a, n, G[i])

print(m)
print(*G)
print(count)
print(*a, sep="\n")
