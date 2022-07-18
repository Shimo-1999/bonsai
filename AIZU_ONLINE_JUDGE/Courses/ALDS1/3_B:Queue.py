from collections import deque

n, q = map(int, input().split())
queue = deque([])
for _ in range(n):
    name, time = input().split()
    queue.append((name, int(time)))


elapsed_time = 0
ans = []
while queue:
    name, time = queue.popleft()
    if time > q:
        elapsed_time += q
        queue.append((name, time - q))
    else:
        elapsed_time += time
        ans.append((name, elapsed_time))

for name, time in ans:
    print(name, time)
