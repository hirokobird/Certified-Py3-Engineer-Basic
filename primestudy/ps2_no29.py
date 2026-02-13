
# No.29

try:
    raise TypeError("型が不正です", "正しい値を", "入力しなおしてください")
except TypeError as t:
    print(t.args)


