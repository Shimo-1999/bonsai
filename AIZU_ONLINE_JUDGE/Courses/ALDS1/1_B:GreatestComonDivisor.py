def greatest_common_divisor(x, y):
    if x > y:
        x, y = y, x
    if y % x == 0:
        return x
    else:
        return greatest_common_divisor(x, y % x)


x, y = map(int, input().split())
print(greatest_common_divisor(x, y))
