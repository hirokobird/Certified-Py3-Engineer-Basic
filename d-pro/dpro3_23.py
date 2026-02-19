# No.23

for i in range(20):
    if i % 3 ==0:
        print("{}は3で割り切れます".format(i), end='\n')
    elif i > 8 and i % 2 == 0:
        break
    else:
        continue