def culc(a, b=1, squares=[], cubes=[]):
    squares.append(a ** 2)
    cubes.append(b ** 3)
    return squares, cubes

print(culc(1))
print(culc(2, 3))
print(culc(3, 4))
print(culc(4, 5))
print(culc(3, 4, [], []))
print(culc(5, 6))
print(culc(7, 8, [10], [10]))
# print(culc(8, 9, 20, 20)) ←このパターンはNG

# squares=[] は、関数を呼ぶたびにリセットされない
# 同じリストを使い回してしまうこれが「危険」と言われる理由です。
# 以下の形のほうがいい
def culc(a, b=1, squares=None, cubes=None):
    if squares is None:
        squares = []
    if cubes is None:
        cubes = []
    squares.append(a ** 2)
    cubes.append(b ** 3)
    return squares, cubes
