i = 5
i = 6

def f(arg = i):
    i = 7
    print(arg)

i = 8
i = 9

f()

# iはどうなってる？関数に引数を渡すとどうなる？
print(i)
f(5)
f(arg=5)