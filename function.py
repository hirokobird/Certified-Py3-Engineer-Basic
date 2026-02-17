# 広域名前空間と局所名前空間：入門テキストP279

g1 = 1
g2 = 2

def outer():
    def inner():
        f2 = 6
        print(f'[2] inner()  g1, g2: {g1},{g2}')
        print(f'    inner()  f1, f2: {f1},{f2}')
    f1 = 3
    f2 = 4
    g2 = 5
    inner()
    print(f'[3] outer()  g1, g2: {g1},{g2}')
    print(f'    outer()  f1, f2: {f1},{f2}')

print(f'[1] global() g1, g2: {g1},{g2}')
outer()
print(f'[4] global() g1, g2: {g1},{g2}')

# 出力
# [1] global() g1, g2: 1,2
# [2] inner()  g1, g2: 1,5
#     inner()  f1, f2: 3,6
# [3] outer()  g1, g2: 1,5
#     outer()  f1, f2: 3,4
# [4] global() g1, g2: 1,2