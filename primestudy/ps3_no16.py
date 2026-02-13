
# No.16

pairs = [(3, 'b'), (1, 'b'), (2, 'a')]

# lambdaの後のargは引数
pairs.sort(key=lambda arg:arg[1])
print(pairs)

# 関数で定義するなら。

# def func(arg):
#     return arg[1]

# pairs.sort(key=func)
# print(func((3, 'b')))
