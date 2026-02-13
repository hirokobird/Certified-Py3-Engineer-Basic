# No.9

months = ['January', 'March', 'May', 'July']
months.append('September')

for month in months[:]:

    if len(month) > 5:
        months.insert(0, month)

print(months, end ='')
