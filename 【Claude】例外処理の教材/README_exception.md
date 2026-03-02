# Python 例外処理 教材セット

講師自身が理解を深め、生徒に教えるための完全ガイド

## 📚 教材の構成

### 1. 解説書（講師向け）
**ファイル**: `exception_guide.py`

あなた自身が例外処理を理解するための詳しい解説書です。

**内容:**
- 第1章: 例外処理の基本
- 第2章: try-except と if文の使い分け ⭐重要
- 第3章: raiseを使うシーン ⭐重要
- 第4章: else と finally の役割
- 第5章: 実行順序の完全理解
- 第6章: 複数の例外をキャッチする
- 第7章: as e の使い方
- 第8章: よくある間違い

**使い方:**
```bash
python exception_guide.py
```

実行すると、各章ごとに例が表示されます。
コードを読むだけでなく、必ず実行して動きを確認してください。

---

### 2. 実践プログラム（講師向け）
**ファイル**: `exception_practice.py`

実際に動く「ユーザー管理システム」で例外処理を体験します。

**機能:**
- ユーザーの追加・検索・更新・削除
- JSONファイルへの保存・読み込み
- 入力値の検証（raise）
- ファイル操作（try-except-finally）

**使い方:**
```bash
python exception_practice.py
```

全てのテストケースが自動で実行されます。
コードを読んで、どこで例外処理が使われているか確認してください。

---

### 3. 練習問題（生徒向け）

#### 3-1. try-except 基本（3問）
**ファイル**: `practice_try_except.py`

**内容:**
1. リストの要素を安全に取得
2. 文字列を整数に変換（as e を使う）
3. 辞書から値を安全に取得（複数の例外）

**難易度:** ★☆☆

---

#### 3-2. try-except-else-finally（2問）
**ファイル**: `practice_else_finally.py`

**内容:**
1. ファイルの行数を数える
2. 割り算の結果をログに記録

**難易度:** ★★☆

---

#### 3-3. raise（4問）
**ファイル**: `practice_raise.py`

**内容:**
1. 負の数をチェック
2. 年齢の範囲をチェック
3. 空リストをチェック
4. カスタム例外を作る

**難易度:** ★★☆

---

## 🎯 学習の進め方（推奨）

### ステップ1: 解説書を読む（講師自身）
```bash
python exception_guide.py
```

**目標:**
- try-except と if文の使い分けを理解する
- raiseを使うべきシーンを理解する
- else と finally の役割を理解する

**所要時間:** 30〜60分

---

### ステップ2: 実践プログラムを読む＆実行する
```bash
python exception_practice.py
```

**目標:**
- 実際のコードで例外処理がどう使われるか見る
- 各メソッドでの使い分けを理解する

**所要時間:** 30分

**さらに深く学ぶには:**
- コードを自分で修正してみる
- 新しいメソッドを追加してみる
- わざとエラーを起こしてみる

---

### ステップ3: 練習問題を解く

**順番:**
1. `practice_try_except.py`（基本から）
2. `practice_else_finally.py`（else/finally）
3. `practice_raise.py`（raise）

**所要時間:** 各30分（合計1.5時間）

---

### ステップ4: 生徒に教える準備

**チェックリスト:**
- [ ] try-except と if文の違いを説明できる
- [ ] raiseを使う場面を3つ以上説明できる
- [ ] else と finally の違いを説明できる
- [ ] as e の使い方を説明できる
- [ ] よくある間違いを指摘できる

---

## 📖 重要な概念まとめ

### try-except と if文の使い分け

```python
# ✅ if文を使う（予測可能）
if not isinstance(x, int):
    return "エラー"

# ✅ try-exceptを使う（予測不可能）
try:
    with open(file) as f:
        data = f.read()
except FileNotFoundError:
    return "ファイルがありません"
```

**原則:**
- 予測できる条件 → **if文**
- 予測できない異常 → **try-except**

---

### raiseを使うシーン

```python
def create_user(name, age):
    # 入力値の検証
    if not name:
        raise ValueError("名前を入力してください")
    
    if age < 0:
        raise ValueError("年齢は0以上にしてください")
    
    return {"name": name, "age": age}
```

**使う場面:**
1. 入力値の検証
2. 関数の前提条件が満たされていない
3. カスタムエラーを作る

---

### else と finally

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("エラー")
else:
    # エラーが起きなかったときだけ
    print(f"成功: {result}")
finally:
    # 必ず実行される
    print("処理を終了")
```

**役割:**
- **else**: 正常時の処理を分離
- **finally**: 必ず実行するクリーンアップ

---

## 🎓 生徒に教えるときのポイント

### ポイント1: 具体例から始める

❌ 「例外処理は異常な状態を扱う仕組みです」
✅ 「0で割ったり、存在しないファイルを開こうとするとエラーが出ますよね。そのエラーを適切に処理するのが例外処理です」

### ポイント2: if文との違いを強調

生徒は最初、「if文で全部チェックすればいいのでは？」と思います。

**説明例:**
「ファイルが存在するか if文でチェックしても、その後すぐに削除されるかもしれません。実際に開いてみて、ダメだったら例外処理で対応する方が安全です」

### ポイント3: raiseは「通知」だと伝える

「raise は単にエラーを出すだけじゃありません。『この状態は異常だから、呼び出し側で対処してね』と通知するんです」

### ポイント4: 紙に書いて実行順序を追う

特に else と finally は、紙に書いて実行順序を追うと理解しやすいです。

```
try → エラーなし → else → finally
try → エラー → except → finally
```

### ポイント5: よくある間違いを先に教える

- tryブロックが長すぎる
- 全ての例外をキャッチしてしまう（except:）
- 例外を無視する（pass）

これらを先に教えると、生徒が同じ間違いをしにくくなります。

---

## 💡 よくある質問と回答

### Q1: いつ raise を使って、いつ None を返すの？

**A:**
- **raise**: 呼び出し側に必ず気づいてほしいとき
- **None**: 見つからないだけで異常ではないとき

```python
# raise を使う
def get_user_by_id(user_id):
    if user_id < 0:
        raise ValueError("IDは0以上です")  # これは異常

# None を返す
def find_user_by_email(email):
    for user in users:
        if user.email == email:
            return user
    return None  # 見つからないだけ、異常ではない
```

### Q2: except と finally の順番は？

**A:**
必ず `except` → `else` → `finally` の順番です。

```python
try:
    pass
except:
    pass
else:
    pass
finally:
    pass
```

### Q3: finally は本当に必要？

**A:**
with文を使えば、ファイルは自動で閉じられるので、多くの場合は不要です。
でも、複雑なクリーンアップが必要な場合は finally が便利です。

```python
# with を使えば finally は不要
with open(file) as f:
    data = f.read()

# 複雑な場合は finally が便利
try:
    # データベース接続
    # ファイル操作
    # ネットワーク通信
finally:
    # 全てのリソースを確実に解放
```

---

## 📝 補足資料

### エラーの種類

よく使う例外:

| 例外 | 説明 | 例 |
|------|------|-----|
| `ValueError` | 値が不正 | `int("abc")` |
| `TypeError` | 型が不正 | `"hello" + 5` |
| `IndexError` | リストの範囲外 | `[1, 2][10]` |
| `KeyError` | 辞書のキーが存在しない | `{"a": 1}["b"]` |
| `FileNotFoundError` | ファイルが見つからない | `open("x.txt")` |
| `ZeroDivisionError` | 0で割る | `10 / 0` |

---

## 🚀 次のステップ

この教材を終えたら:

1. **自分でプログラムを作る**: 例外処理を実際に使ってみる
2. **生徒の質問に答える**: 実際に教えてみる
3. **コードレビュー**: 生徒のコードで例外処理をチェック
4. **発展課題**: ログ記録、リトライ処理、カスタム例外クラス

---

## ✅ 最後に

例外処理は最初は難しいですが、パターンを覚えれば自然に使えるようになります。

**重要な3つのポイント:**
1. try-except と if文の使い分け
2. raiseで適切にエラーを通知
3. finally でクリーンアップ

この教材で、あなた自身の理解が深まり、生徒にも自信を持って教えられるようになることを願っています！

頑張ってください！ 📚✨
