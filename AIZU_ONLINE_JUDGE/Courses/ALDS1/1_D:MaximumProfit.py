n = int(input())
min_number = 10**10

answer = -(10**10)
for _ in range(n):
    m = int(input())
    answer = max(answer, m - min_number)
    min_number = min(m, min_number)
print(answer)
