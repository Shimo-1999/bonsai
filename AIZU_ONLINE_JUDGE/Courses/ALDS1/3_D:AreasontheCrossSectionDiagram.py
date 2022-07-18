# last_down_x[y] := y で "\\" だった最後の x
last_down_x = [-1 for _ in range(2 * 20000 + 1)]

s = input()
y = 20000
keep = []
for x in range(len(s)):
    if s[x] == "\\":
        y -= 1
        last_down_x[y] = x
    elif s[x] == "/":
        if last_down_x[y] == -1:
            continue
        a = last_down_x[y]
        b = x
        # 高さが y のとき a b の範囲に水が溜まっている
        keep.append((a, b))
        y += 1
    elif s[x] == "_":
        pass

# 範囲の広い順に sort
keep.sort(key=lambda ab: ab[1] - ab[0], reverse=True)

# waters[i] := [[a, b, water], ...] a b の間に water だけ水が貯まっている
waters = []
for a, b in keep:
    for i in range(len(waters)):
        aa, bb, water = waters[i]
        if aa < a and b < bb:
            waters[i][2] += b - a
            break
    else:
        waters.append([a, b, b - a])

waters.sort()
ans = []
for aa, bb, water in waters:
    ans.append(water)
print(sum(ans))
print(len(ans), *ans)
