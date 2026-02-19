# リストのアンパック

def max3(a, b, c):
    max = a
    if b > max: max =b
    if c > max: max =c
    return max

lst1 = [1, 2, 3]
m = max3(*lst1)
print(f'{lst1}の最大値は{m}です。')

# 辞書のアンパック

def puts(n,s):
    for _ in range(n):
        print(s, end='')

d1 = {'n':3, 's':'*'}
d2 = {'s':'+', 'n':7}

puts(**d1)
print()
puts(**d2)

