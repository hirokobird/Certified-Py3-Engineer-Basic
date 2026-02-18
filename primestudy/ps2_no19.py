
# No.19 zipとアンパック

# 内包表記
matrix = [[1,3,5], [4,9,25], [8,27,125]]
power = [[row[i] for row in matrix] for i in range(3)]
print(power)

# コード代替版
power2 = list(zip(*matrix))
print(power2)

# 展開
power3 = []
for row3 in matrix:
    for i3 in range(3):
        power3.append(row3[i3])
print(power3)