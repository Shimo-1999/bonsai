import random

n = int(input())
c = [[random.randint(1, 10) for i in range(n)] for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])
for i in c:
    print(i)
