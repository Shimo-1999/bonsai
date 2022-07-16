class trump:
    def __init__(self, mark, number):
        self.mark: str = mark
        self.number: int = number


def bubble_sort(c, n):
    for i in range(n):
        for j in reversed(range(i + 1, n)):
            if c[j].number < c[j - 1].number:
                c[j], c[j - 1] = c[j - 1], c[j]


def selection_sort(c, n):
    for i in range(n):
        min_j = i
        for j in range(i, n):
            if c[min_j].number > c[j].number:
                min_j = j
        c[i], c[min_j] = c[min_j], c[i]


n = int(input())
a = input().split()

# bubble sort
c = []
for i in range(n):
    c.append(trump(a[i][0], int(a[i][1])))
bubble_sort(c, n)

answer1 = []
for i in range(n):
    answer1.append(c[i].mark + str(c[i].number))
print(*answer1)
print("Stable")

# selection sort
c = []
for i in range(n):
    c.append(trump(a[i][0], int(a[i][1])))
selection_sort(c, n)

answer2 = []
for i in range(n):
    answer2.append(c[i].mark + str(c[i].number))
print(*answer2)
if answer1 == answer2:
    print("Stable")
else:
    print("Not stable")
