# ============================================
# try-except 練習問題（3問）
# 目的：基本的な例外処理を身につける
# ============================================

# --------------------------------------------
# 第1問：リストの要素を安全に取得しよう
# --------------------------------------------
# 【問題】
# 関数 safe_get(lst, index) を完成させてください。
# lst[index] を取得して return します。
# ただし、index が範囲外の場合は IndexError が起きるので、
# try-except で捕まえて None を return してください。
#
# 【ヒント】
# - try: で lst[index] を取得
# - except IndexError:
# - return None

def safe_get(lst, index):
    # TODO: ここを実装
    pass


# 動作確認（期待する動き）
numbers = [10, 20, 30, 40, 50]

print(safe_get(numbers, 2))   # 30
print(safe_get(numbers, 10))  # None（IndexError）


# --------------------------------------------
# 第2問：文字列を整数に変換しよう（as e を使う）
# --------------------------------------------
# 【問題】
# 関数 str_to_int(s) を完成させてください。
# 文字列 s を int に変換して return します。
# ただし、変換に失敗する場合は ValueError が起きるので、
# try-except で捕まえて None を return してください。
#
# さらに、エラーが起きた場合は、エラーメッセージを print で表示してください。
# 例：print(f"変換エラー: {e}")
#
# 【ヒント】
# - try: で int(s)
# - except ValueError as e:
# - print(f"変換エラー: {e}")
# - return None

def str_to_int(s):
    # TODO: ここを実装
    pass


# 動作確認（期待する動き）
print(str_to_int("123"))   # 123
print(str_to_int("abc"))   # None（エラーメッセージも表示）
print(str_to_int("12.5"))  # None（エラーメッセージも表示）


# --------------------------------------------
# 第3問：辞書から値を安全に取得しよう（複数の例外）
# --------------------------------------------
# 【問題】
# 関数 safe_dict_get(d, key, convert_to_int) を完成させてください。
# d[key] を取得します。
# convert_to_int が True の場合は、値を int に変換します。
#
# ただし、以下のエラーが起きる可能性があります：
# - key が存在しない → KeyError
# - int への変換失敗 → ValueError
#
# これらをまとめて捕まえて、None を return してください。
# さらに、エラーが起きたら「エラー: <例外メッセージ>」と表示してください。
#
# 【ヒント】
# - except (KeyError, ValueError) as e:
# - print(f"エラー: {e}")
# - return None

def safe_dict_get(d, key, convert_to_int=False):
    # TODO: ここを実装
    pass


# 動作確認（期待する動き）
data = {
    "name": "太郎",
    "age": "25",
    "score": "abc"
}

print(safe_dict_get(data, "name"))                    # 太郎
print(safe_dict_get(data, "age", convert_to_int=True)) # 25
print(safe_dict_get(data, "score", convert_to_int=True)) # None（ValueError）
print(safe_dict_get(data, "address"))                 # None（KeyError）


# ============================================
# 解答例（実行後に確認してください）
# ============================================

"""
# 第1問の解答例
def safe_get(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None


# 第2問の解答例
def str_to_int(s):
    try:
        return int(s)
    except ValueError as e:
        print(f"変換エラー: {e}")
        return None


# 第3問の解答例
def safe_dict_get(d, key, convert_to_int=False):
    try:
        value = d[key]
        if convert_to_int:
            value = int(value)
        return value
    except (KeyError, ValueError) as e:
        print(f"エラー: {e}")
        return None
"""
