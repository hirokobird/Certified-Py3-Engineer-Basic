
# No.9

months = ['January', 'March', 'May', 'July']
months.append('September')

for month in months[:]:

    if len(month) > 5:
        months.insert(0, month)

print(months, end ='')

print('================')

py = ["P","y","t","h","o","n"]
print(py[1:3])
print(py[3])
print(py[-2:-5])

try:
    raise TypeError("型が不正です", "入力しなおしてください")
except TypeError as t:
    print(t.args)

