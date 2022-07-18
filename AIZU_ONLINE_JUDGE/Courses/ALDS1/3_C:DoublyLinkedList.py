from collections import deque
import sys


q = deque([])

n = int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline().rstrip()
    if command == "deleteFirst":
        q.popleft()
    elif command == "deleteLast":
        q.pop()

    else:
        com, x = command.split()
        if com == "insert":
            q.appendleft(x)
        elif com == "delete":
            try:
                q.discard(x)
            except:
                pass

print(" ".join(q))
