# No.17
# 内包表記
print([(x, y) for x in [0, 1, 2] for y in [1, 2, 3] if x !=y])

print("===========")

# 展開
zz = []
for xx in [0, 1, 2]:
    for yy in [1, 2, 3]:
        if xx != yy:
            zz.append((xx, yy))

print(zz)
