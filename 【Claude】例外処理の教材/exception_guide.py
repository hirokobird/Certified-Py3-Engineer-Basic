# Python 例外処理 完全解説書
# 講師が理解を深めるための教材

"""
この解説書の目的:
1. try-except と if文の使い分けを理解する
2. raise を使うシーンを理解する
3. else と finally の役割を理解する
4. 生徒に教えられるようになる
"""

# ============================================
# 第1章: 例外処理とは何か？
# ============================================

print("=" * 60)
print("第1章: 例外処理の基本")
print("=" * 60)

# 例外とは「プログラムの異常な状態」のこと
# 例：0で割る、存在しないファイルを開く、リストの範囲外にアクセス

# 例1: ZeroDivisionError
try:
    result = 10 / 0  # エラーが起きる
    print(result)
except ZeroDivisionError:
    print("0で割ることはできません")

print()

# 例2: IndexError
try:
    numbers = [1, 2, 3]
    print(numbers[10])  # 範囲外
except IndexError:
    print("リストの範囲外です")

print()

# 例3: FileNotFoundError
try:
    with open("存在しないファイル.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("ファイルが見つかりません")

print("\n")


# ============================================
# 第2章: try-except と if文の使い分け
# ============================================

print("=" * 60)
print("第2章: try-except と if文の使い分け")
print("=" * 60)

# 【重要な原則】
# - 予測できる条件 → if文
# - 予測できない異常 → try-except

# --- ケース1: 数値チェック（予測できる） ---
print("\n【ケース1: 数値チェック】")

# ❌ 良くない例: try-exceptで型チェック
def bad_example(x):
    try:
        result = x + 10
        return result
    except TypeError:
        return "数値を入力してください"

# ✅ 良い例: if文で型チェック
def good_example(x):
    if not isinstance(x, (int, float)):
        return "数値を入力してください"
    return x + 10

print("Bad:", bad_example("abc"))
print("Good:", good_example("abc"))

print("\n【理由】")
print("型チェックは予測可能 → if文で事前にチェックする方が明確")

# --- ケース2: ファイル操作（予測できない） ---
print("\n【ケース2: ファイル操作】")

# ❌ 良くない例: if文でファイルの存在確認
import os

def bad_file_read(path):
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    else:
        return "ファイルが見つかりません"

# ✅ 良い例: try-exceptで例外処理
def good_file_read(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        return "ファイルが見つかりません"

print("\n【理由】")
print("ファイルは:")
print("- 確認後に削除されるかも")
print("- 権限がないかも")
print("- ネットワークドライブで消えるかも")
print("→ try-exceptで実際に開いてみる方が安全")

# --- ケース3: ユーザー入力の変換（try-exceptが適切） ---
print("\n【ケース3: 文字列→数値変換】")

def convert_to_int(value):
    """文字列を整数に変換"""
    try:
        return int(value)
    except ValueError:
        return None

print("変換成功:", convert_to_int("123"))
print("変換失敗:", convert_to_int("abc"))

print("\n【理由】")
print("int()がエラーを出すかどうかは、実際に試すまで分からない")
print("→ try-exceptが適切")

print("\n\n")


# ============================================
# 第3章: raiseを使うシーン
# ============================================

print("=" * 60)
print("第3章: raiseを使うシーン")
print("=" * 60)

# raiseは「意図的にエラーを起こす」こと
# 使うシーン:
# 1. 入力値の検証
# 2. 関数の前提条件が満たされていない
# 3. カスタムエラーを作る

# --- シーン1: 入力値の検証 ---
print("\n【シーン1: 入力値の検証】")

def create_user(name, age):
    """ユーザーを作成する"""
    # 名前が空はダメ
    if not name:
        raise ValueError("名前を入力してください")
    
    # 年齢が負の数はダメ
    if age < 0:
        raise ValueError("年齢は0以上にしてください")
    
    return {"name": name, "age": age}

try:
    user1 = create_user("太郎", 20)
    print("✓", user1)
    
    user2 = create_user("", 20)  # エラー
except ValueError as e:
    print("✗", e)

print("\n【なぜraiseを使うのか？】")
print("- 関数を呼ぶ側に「これは異常だ」と知らせる")
print("- Noneを返すだけだと気づかれないかも")
print("- エラーメッセージで原因が明確になる")

# --- シーン2: 型チェック ---
print("\n【シーン2: 型チェック】")

def multiply(a, b):
    """2つの数を掛け算する"""
    if not isinstance(a, (int, float)):
        raise TypeError(f"aは数値である必要があります。受け取った型: {type(a)}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"bは数値である必要があります。受け取った型: {type(b)}")
    
    return a * b

try:
    print(multiply(5, 3))      # ✓ 15
    print(multiply("5", 3))    # ✗ TypeError
except TypeError as e:
    print("エラー:", e)

# --- シーン3: カスタム例外 ---
print("\n【シーン3: カスタム例外】")

class AgeError(Exception):
    """年齢に関するエラー"""
    pass

def check_adult(age):
    """18歳以上かチェック"""
    if age < 18:
        raise AgeError(f"{age}歳は未成年です")
    return True

try:
    check_adult(20)  # ✓
    print("✓ 成人です")
    
    check_adult(15)  # ✗
except AgeError as e:
    print("✗", e)

print("\n【カスタム例外の利点】")
print("- エラーの種類が明確")
print("- 特定のエラーだけキャッチできる")
print("- コードが読みやすくなる")

print("\n\n")


# ============================================
# 第4章: else と finally の役割
# ============================================

print("=" * 60)
print("第4章: else と finally")
print("=" * 60)

# --- else: エラーが起きなかったときだけ実行 ---
print("\n【else の役割】")

def divide_with_else(a, b):
    """割り算（elseあり）"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("エラー: 0で割れません")
        return None
    else:
        # エラーが起きなかったときだけ実行される
        print(f"計算成功: {a} / {b} = {result}")
        return result

print("--- 正常な場合 ---")
divide_with_else(10, 2)

print("\n--- エラーの場合 ---")
divide_with_else(10, 0)

print("\n【elseを使う理由】")
print("- 正常時の処理を明確に分離できる")
print("- tryブロックを短くできる（推奨）")

# --- finally: 必ず実行される ---
print("\n【finally の役割】")

def read_file_with_finally(path):
    """ファイル読み込み（finallyあり）"""
    file = None
    try:
        print(f"ファイルを開きます: {path}")
        file = open(path)
        content = file.read()
        return content
    except FileNotFoundError:
        print("エラー: ファイルが見つかりません")
        return None
    else:
        print("ファイル読み込み成功")
    finally:
        # 必ず実行される（エラーでも正常でも）
        print("クリーンアップ処理を実行します")
        if file:
            file.close()
            print("ファイルを閉じました")

# テスト用ファイル作成
with open("test.txt", "w") as f:
    f.write("テストデータ")

print("--- 正常な場合 ---")
read_file_with_finally("test.txt")

print("\n--- エラーの場合 ---")
read_file_with_finally("存在しない.txt")

# 後片付け
import os
os.remove("test.txt")

print("\n【finallyを使う場面】")
print("- ファイルを閉じる")
print("- データベース接続を閉じる")
print("- ロックを解放する")
print("- 一時ファイルを削除する")
print("→ 必ず実行したいクリーンアップ処理")

print("\n\n")


# ============================================
# 第5章: 実行順序の完全理解
# ============================================

print("=" * 60)
print("第5章: try-except-else-finally の実行順序")
print("=" * 60)

def execution_order_demo(will_error):
    """実行順序のデモ"""
    print("\n--- 開始 ---")
    
    try:
        print("1. try ブロック実行")
        if will_error:
            raise ValueError("意図的なエラー")
        print("2. try ブロック正常終了")
    except ValueError as e:
        print(f"3. except ブロック実行: {e}")
    else:
        print("4. else ブロック実行（エラーなし）")
    finally:
        print("5. finally ブロック実行（必ず）")
    
    print("6. 関数終了")

print("\n【パターン1: エラーなし】")
execution_order_demo(False)
# 実行順: 1 → 2 → 4 → 5 → 6

print("\n【パターン2: エラーあり】")
execution_order_demo(True)
# 実行順: 1 → 3 → 5 → 6

print("\n【まとめ】")
print("✓ try で正常終了 → else → finally")
print("✓ try でエラー → except → finally")
print("✓ finally は必ず実行される")

print("\n\n")


# ============================================
# 第6章: 複数の例外をキャッチする
# ============================================

print("=" * 60)
print("第6章: 複数の例外処理")
print("=" * 60)

# --- 方法1: 個別にキャッチ ---
print("\n【方法1: 個別にキャッチ】")

def method1(data, index):
    try:
        value = data[index]
        number = int(value)
        return number
    except IndexError:
        print("エラー: インデックスが範囲外です")
        return None
    except ValueError:
        print("エラー: 数値に変換できません")
        return None

data = ["10", "20", "abc"]
print(method1(data, 1))   # 20
print(method1(data, 2))   # ValueError
print(method1(data, 10))  # IndexError

# --- 方法2: まとめてキャッチ ---
print("\n【方法2: まとめてキャッチ】")

def method2(data, index):
    try:
        value = data[index]
        number = int(value)
        return number
    except (IndexError, ValueError) as e:
        print(f"エラー: {e}")
        return None

print(method2(data, 1))   # 20
print(method2(data, 2))   # ValueError
print(method2(data, 10))  # IndexError

print("\n【使い分け】")
print("- 個別: エラーごとに違う処理をしたい")
print("- まとめて: 同じ処理でOK")

print("\n\n")


# ============================================
# 第7章: as e でエラー情報を取得
# ============================================

print("=" * 60)
print("第7章: as e の使い方")
print("=" * 60)

# as e を使うと、エラーオブジェクトを取得できる

def demo_as_e():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"エラーの型: {type(e)}")
        print(f"エラーメッセージ: {e}")
        print(f"エラー詳細: {repr(e)}")

demo_as_e()

print("\n【as e を使う場面】")
print("- エラーメッセージをログに記録")
print("- エラー内容をユーザーに表示")
print("- デバッグ情報の収集")

# 実践例
def safe_operation(a, b, operation):
    """安全な計算"""
    try:
        if operation == "divide":
            return a / b
        elif operation == "index":
            return [a, b][10]
    except Exception as e:
        # ログに記録する想定
        error_log = f"[ERROR] {type(e).__name__}: {e}"
        print(error_log)
        return None

safe_operation(10, 0, "divide")
safe_operation(10, 20, "index")

print("\n\n")


# ============================================
# 第8章: よくある間違い
# ============================================

print("=" * 60)
print("第8章: よくある間違いと正しい書き方")
print("=" * 60)

# --- 間違い1: tryブロックが長すぎる ---
print("\n【間違い1: tryブロックが長すぎる】")

# ❌ 悪い例
def bad_practice():
    try:
        x = 10
        y = 20
        result = x / y  # これだけがエラーの可能性
        data = [1, 2, 3]
        item = data[0]
        return result + item
    except:
        return None

# ✅ 良い例
def good_practice():
    x = 10
    y = 20
    
    # エラーが起きる可能性がある部分だけtryで囲む
    try:
        result = x / y
    except ZeroDivisionError:
        return None
    
    data = [1, 2, 3]
    item = data[0]
    return result + item

print("【ポイント】tryブロックは最小限に")

# --- 間違い2: 全ての例外をキャッチ ---
print("\n【間違い2: 全ての例外をキャッチ】")

# ❌ 悪い例
def bad_catch_all():
    try:
        return 10 / 0
    except:  # 何でもキャッチしてしまう
        return None

# ✅ 良い例
def good_specific_catch():
    try:
        return 10 / 0
    except ZeroDivisionError:  # 具体的な例外のみ
        return None

print("【ポイント】具体的な例外を指定する")

# --- 間違い3: 例外を無視 ---
print("\n【間違い3: 例外を無視】")

# ❌ 悪い例
def bad_silent_fail():
    try:
        result = 10 / 0
    except:
        pass  # 何も情報がない

# ✅ 良い例
def good_logging():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"エラー発生: {e}")  # 最低限ログを残す
        return None

print("【ポイント】せめてログを残す")

print("\n\n")


# ============================================
# まとめ: 例外処理の判断フローチャート
# ============================================

print("=" * 60)
print("まとめ: いつ何を使うか？")
print("=" * 60)

summary = """
【判断フローチャート】

1. 条件が事前に分かる？
   YES → if文を使う
   NO  → 次へ

2. エラーが起きる可能性がある？
   YES → try-except を使う
   NO  → 普通に書く

3. 入力値が不正？
   YES → raise でエラーを投げる
   
4. 正常時に特別な処理が必要？
   YES → else を使う
   
5. 必ず実行したい処理がある？
   YES → finally を使う

【具体例】
- ユーザー入力のチェック → if文 + raise
- ファイル操作 → try-except-finally
- 数値変換 → try-except
- 型チェック → if文 + raise
- データベース操作 → try-except-finally
"""

print(summary)

print("\n" + "=" * 60)
print("解説書は以上です！")
print("=" * 60)
