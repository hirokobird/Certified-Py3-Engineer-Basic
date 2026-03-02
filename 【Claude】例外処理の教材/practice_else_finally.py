# ============================================
# try-except-else-finally 練習問題（2問）
# 目的：else と finally の使い方を身につける
# ============================================

# --------------------------------------------
# 第1問：ファイルの行数を数えよう
# --------------------------------------------
# 【問題】
# 関数 count_lines(filepath) を完成させてください。
# ファイルを開いて、行数を数えて return します。
#
# ルール：
# - ファイルが見つからない場合（FileNotFoundError）は None を return
# - エラーが起きなかった場合（正常時）は else 節で行数を return
# - finally 節では必ず「処理を終了しました」と print する
#
# 【ヒント】
# - try: で open(filepath) してファイルを開く
# - except FileNotFoundError:
# - else: で行数を数えて return
# - finally: で必ず print
# - with open を使ってもOK

def count_lines(filepath):
    # TODO: ここを実装
    pass


# テスト用ファイルを作成
with open("test1.txt", "w") as f:
    f.write("1行目\n2行目\n3行目")

# 動作確認（期待する動き）
print(count_lines("test1.txt"))      # 3（最後に「処理を終了しました」）
print(count_lines("notfound.txt"))   # None（最後に「処理を終了しました」）

# クリーンアップ
import os
os.remove("test1.txt")


# --------------------------------------------
# 第2問：割り算の結果をログに記録しよう
# --------------------------------------------
# 【問題】
# 関数 divide_with_log(a, b, logfile) を完成させてください。
# a / b を計算して return します。
#
# ルール：
# - b が 0 の場合（ZeroDivisionError）は None を return
# - エラーが起きなかった場合（正常時）は else 節で：
#   - 結果を print する（例：「計算成功: 10 / 2 = 5.0」）
#   - 結果を return する
# - finally 節では必ず：
#   - ログファイルに結果を書き込む
#   - 成功時：「SUCCESS: a / b = result」
#   - 失敗時：「ERROR: a / b - division by zero」
#
# 【ヒント】
# - try: で a / b を計算
# - except ZeroDivisionError:
# - else: で print と return
# - finally: でログファイルに書き込み
# - ログファイルは追記モード（'a'）で開く

def divide_with_log(a, b, logfile="calc_log.txt"):
    # TODO: ここを実装
    pass


# 動作確認（期待する動き）
print("--- 正常な計算 ---")
result1 = divide_with_log(10, 2)  # 計算成功メッセージ表示
print(f"結果: {result1}")

print("\n--- エラーの計算 ---")
result2 = divide_with_log(10, 0)  # エラー
print(f"結果: {result2}")

# ログファイルを確認
print("\n--- ログファイルの内容 ---")
with open("calc_log.txt") as f:
    print(f.read())

# クリーンアップ
import os
os.remove("calc_log.txt")


# ============================================
# 解答例（実行後に確認してください）
# ============================================

"""
# 第1問の解答例
def count_lines(filepath):
    try:
        with open(filepath) as f:
            lines = f.readlines()
    except FileNotFoundError:
        return None
    else:
        return len(lines)
    finally:
        print("処理を終了しました")


# 第2問の解答例
def divide_with_log(a, b, logfile="calc_log.txt"):
    result = None
    error_occurred = False
    
    try:
        result = a / b
    except ZeroDivisionError:
        error_occurred = True
        return None
    else:
        print(f"計算成功: {a} / {b} = {result}")
        return result
    finally:
        with open(logfile, 'a') as f:
            if error_occurred:
                f.write(f"ERROR: {a} / {b} - division by zero\n")
            else:
                f.write(f"SUCCESS: {a} / {b} = {result}\n")
"""
