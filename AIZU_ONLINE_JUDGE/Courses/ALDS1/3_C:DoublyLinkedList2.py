# TODO: TLE するので修正する
import sys


class Node:
    def __init__(self, prev_node, value, next_node):
        self.prev = prev_node
        self.value = value
        self.next = next_node


class DoublyLinkedList:
    def __init__(self):
        self.first_node = Node(None, None, None)
        self.last_node = Node(self.first_node, None, None)
        self.first_node.next = self.last_node
        self.x_count = {}

    def insert(self, x):
        self.x_count.setdefault(x, 0)
        self.x_count[x] += 1
        new_node = Node(self.first_node, x, self.first_node.next)
        self.first_node.next.prev = new_node
        self.first_node.next = new_node

    def delete(self, x):
        self.x_count.setdefault(x, 0)
        if self.x_count[x] == 0:
            return
        current_node = self.first_node.next
        while current_node.value is not None:
            if current_node.value == x:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                break
            current_node = current_node.next

    def delete_first(self):
        self.x_count[self.first_node.next.value] -= 1
        self.first_node.next.next.prev = self.first_node
        self.first_node.next = self.first_node.next.next

    def delete_last(self):
        self.x_count[self.last_node.prev.value] -= 1
        self.last_node.prev.prev.next = self.last_node
        self.last_node.prev = self.last_node.prev.prev


n = int(sys.stdin.readline())
dll = DoublyLinkedList()
for _ in range(n):
    command = sys.stdin.readline().rstrip()
    if command == "deleteFirst":
        dll.delete_first()
    elif command == "deleteLast":
        dll.delete_last()
    else:
        com, x = command.split()
        if com == "insert":
            dll.insert(x)
        elif com == "delete":
            dll.delete(x)

ans = []
current_node = dll.first_node.next
while current_node.value is not None:
    ans.append(current_node.value)
    current_node = current_node.next

print(" ".join(ans))
