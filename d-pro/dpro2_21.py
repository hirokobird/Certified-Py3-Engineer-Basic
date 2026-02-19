# No.22

'''
演算子の優先順位
算術演算子(+, *, /, %等)
比較演算子（==, >, <, is等）
論理演算子（not⇒and⇒or）
'''

x =True
y = False 
print(not x == y) #比較演算子の方が優先される

name1, name2, name3, name4 = '', 'suzuki', 'tanaka', 'sato'
selected_name = name1 or name2 or name3 or name4
print(selected_name)