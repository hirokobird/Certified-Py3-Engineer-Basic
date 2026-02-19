# No.31

diver = [d*2 for d in 'diver']
print(diver)

print("===========")

diver2 = []
for i in 'diver':   
    diver2.append(i*2)
print(diver2)

'''
for i in 'diver':
for 変数 in [反復可能体（イテラブル）]:

上記の反復可能体には、リスト、タプル、辞書、そして 文字列 を置くことができる。
それらは変数で定義されているかどうかは関係ない。文字列そのままでも置ける。

その場限りで、二度と使わないデータだったり、検定試験や「リスト内包表記（[x for x in 'diver']）」のような短いコードでは、コードを短く書くためにこの 「直打ちスタイル」 が好んで使われる。
'''