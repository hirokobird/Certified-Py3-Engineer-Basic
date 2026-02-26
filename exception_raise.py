"""
例外処理を用いた例：点数入力プログラム
"""

# raiseによる例外の送出
def input_score(score_str):
    # ① まずは入力値が数値かをチェック
    try:
        score = int(score_str)  # ここで入力値が整数以外ならエラーが起きる
    except ValueError:
        # Pythonが出力する英語のエラーをキャッチし、日本語のエラーとして「投げ直す（raise）」
        raise ValueError("エラー：文字ではなく『数値』を入力してください")
    
    # ② 次に「0〜100の範囲か？」をチェック
    if score < 0 or score > 100:
        raise ValueError("エラー：点数は0から100の間で入力してください")
    
    print(f"テストの点数【{score}点】を登録しました。")

# try-except節は関数を呼び出す際に使用する
try:
    print("--- 処理開始 ---")
    
    # inputの時点では int() にせず、ただの文字列として受け取る
    user_input = input("点数を入力：") 
    
    # 関数に文字列のまま引数を渡す
    input_score(user_input)

except ValueError as e:
    # 関数で設定した「日本語の分かりやすいエラー」をここで表示
    print(f"【入力ミスを検知】 {e}")

print("---プログラム終了---")