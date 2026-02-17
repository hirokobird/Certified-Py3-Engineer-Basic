
# No.19

cubes_a = [a**3 for a in range(5)]
print(f"【コードA】{cubes_a}")


# map関数を使用： リストなどの要素に、同じ処理を順番に適用する」ための関数
# map(処理する関数, データ)
cubes_b = list(map(lambda b: b**3, range(5)))
print(f"【コードB】{cubes_b}")

# cubes_aを展開してfor文でも記述できる
cubes_c = []
for c in range(5):
    cubes_c.append(c**3)
print(f"【コードC】{cubes_c}")

