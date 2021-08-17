A = {1, 3, 5, 7, 9}
B = {2, 4, 6, 8, 9}

print(A ^ B)  # 片方にしか含まれてないやつ
print(A | B)  # 共通部分
print(A & B)  # 両方に含まれてるやつ


C = {1, 2, 3, 4, 5}
D = {3, 4}
E = {6}

print(3 in D)
print(C <= D)  # 部分集合か判定 D に C が含まれているか判定 これは False
print(D <= C)  # 部分集合か判定 C に D が含まれているか判定 これは True
print(E <= C)

print(D.isdisjoint(E))  # 互いに素か判定
