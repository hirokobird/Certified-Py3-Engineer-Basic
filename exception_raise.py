"""
例外処理を用いたプログラム例：点数入力
"""

# raiseによる例外の送出
def input_score(score):
    if score < 0 or score > 100:
        raise ValueError("エラー：点数は0から100の間で入力してください！")
    
    print(f"テストの点数【{score}点】を登録しました。")

# try-except節は関数を呼び出す際に使用する
try:
    print("--- 処理開始 ---")
    score = int(input("点数を入力："))
    input_score(score)

except ValueError as e:
    print(f"入力ミスを検知しました：{e}")
    
print("---プログラム終了---")

