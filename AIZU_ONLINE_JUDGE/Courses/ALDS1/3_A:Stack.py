from collections import deque

a = input().split()

stack = deque([])
for i in a:
    if i == "+":
        b = stack.pop()
        c = stack.pop()
        stack.append(c + b)
    elif i == "-":
        b = stack.pop()
        c = stack.pop()
        stack.append(c - b)
    elif i == "*":
        b = stack.pop()
        c = stack.pop()
        stack.append(c * b)
    else:
        stack.append(int(i))
print(stack[-1])
