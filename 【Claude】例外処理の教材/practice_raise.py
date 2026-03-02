# ============================================
# raise 練習問題（4問）
# 目的：適切に例外を発生させる方法を身につける
# ============================================

# --------------------------------------------
# 第1問：負の数をチェックしよう
# --------------------------------------------
# 【問題】
# 関数 sqrt(x) を完成させてください。
# x の平方根を計算して return します（x ** 0.5）。
# ただし、x が負の数の場合は ValueError を raise してください。
# メッセージは「負の数の平方根は計算できません」としてください。
#
# 【ヒント】
# - if x < 0:
# - raise ValueError("...")
# - return x ** 0.5

def sqrt(x):
    # TODO: ここを実装
    pass


# 動作確認（期待する動き）
try:
    print(sqrt(9))    # 3.0
    print(sqrt(16))   # 4.0
    print(sqrt(-4))   # ValueError
except ValueError as e:
    print(f"エラー: {e}")


# --------------------------------------------
# 第2問：年齢の範囲をチェックしよう
# --------------------------------------------
# 【問題】
# 関数 validate_age(age) を完成させてください。
# age が有効な年齢（0〜120）かチェックします。
#
# ルール：
# - age が int でない場合は TypeError を raise
#   メッセージ：「年齢は整数で入力してください」
# - age が 0 未満または 120 より大きい場合は ValueError を raise
#   メッセージ：「年齢は0〜120の範囲で入力してください」
# - 有効な場合は True を return
#
# 【ヒント】
# - isinstance(age, int) で型チェック
# - raise TypeError("...")
# - raise ValueError("...")
# - return True

def validate_age(age):
    # TODO: ここを実装
    pass


# 動作確認（期待する動き）
try:
    print(validate_age(25))    # True
    print(validate_age("25"))  # TypeError
except (TypeError, ValueError) as e:
    print(f"エラー: {e}")

try:
    print(validate_age(150))   # ValueError
except ValueError as e:
    print(f"エラー: {e}")


# --------------------------------------------
# 第3問：空リストをチェックしよう
# --------------------------------------------
# 【問題】
# 関数 get_average(numbers) を完成させてください。
# リストの平均値を計算して return します。
#
# ルール：
# - numbers が空リストの場合は ValueError を raise
#   メッセージ：「空のリストの平均は計算できません」
# - numbers が list でない場合は TypeError を raise
#   メッセージ：「リストを入力してください」
# - 有効な場合は平均値を return
#
# 【ヒント】
# - isinstance(numbers, list) で型チェック
# - len(numbers) == 0 で空チェック
# - sum(numbers) / len(numbers) で平均

def get_average(numbers):
    # TODO: ここを実装
    pass


# 動作確認（期待する動き）
try:
    print(get_average([10, 20, 30]))  # 20.0
    print(get_average([]))            # ValueError
except ValueError as e:
    print(f"エラー: {e}")

try:
    print(get_average("123"))         # TypeError
except TypeError as e:
    print(f"エラー: {e}")


# --------------------------------------------
# 第4問：カスタム例外を作ろう
# --------------------------------------------
# 【問題】
# カスタム例外クラス PasswordError を作成してください。
# さらに、関数 validate_password(password) を完成させてください。
#
# パスワードのルール：
# - 長さが 8 文字以上
# - 数字を少なくとも1つ含む
#
# ルールに違反する場合は PasswordError を raise してください。
#
# 【ヒント】
# - class PasswordError(Exception): pass
# - len(password) で長さチェック
# - any(c.isdigit() for c in password) で数字チェック
# - raise PasswordError("...")

# カスタム例外クラス
class PasswordError(Exception):
    """パスワードに関するエラー"""
    pass


def validate_password(password):
    # TODO: ここを実装
    pass


# 動作確認（期待する動き）
try:
    validate_password("password123")  # OK
    print("✓ パスワードは有効です")
except PasswordError as e:
    print(f"✗ {e}")

try:
    validate_password("short1")       # 長さが足りない
except PasswordError as e:
    print(f"✗ {e}")

try:
    validate_password("passwordonly") # 数字がない
except PasswordError as e:
    print(f"✗ {e}")


# ============================================
# 解答例（実行後に確認してください）
# ============================================

"""
# 第1問の解答例
def sqrt(x):
    if x < 0:
        raise ValueError("負の数の平方根は計算できません")
    return x ** 0.5


# 第2問の解答例
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("年齢は整数で入力してください")
    
    if age < 0 or age > 120:
        raise ValueError("年齢は0〜120の範囲で入力してください")
    
    return True


# 第3問の解答例
def get_average(numbers):
    if not isinstance(numbers, list):
        raise TypeError("リストを入力してください")
    
    if len(numbers) == 0:
        raise ValueError("空のリストの平均は計算できません")
    
    return sum(numbers) / len(numbers)


# 第4問の解答例
class PasswordError(Exception):
    pass

def validate_password(password):
    if len(password) < 8:
        raise PasswordError("パスワードは8文字以上にしてください")
    
    if not any(c.isdigit() for c in password):
        raise PasswordError("パスワードには数字を含めてください")
    
    return True
"""
