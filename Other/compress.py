x = [1, 10000, 30, 5, 2000, 2000]

# 圧縮
d = {e: i for i, e in enumerate(sorted(set(x)))}

print(d)
