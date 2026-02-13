# ログ分析ツール - Pythonエンジニア基礎検定学習用

このプログラムは、Pythonエンジニア基礎検定の以下の項目を学習するための教材です。

## 学習項目

1. **for文やif文で使うbreakとcontinue**
2. ***args, **kwargs（可変長引数とアンパック）**
3. **比較演算子の短絡評価**
4. **raise文（カスタム例外）**
5. **argparse/ArgumentParser**

---

## 使い方

### 基本的な実行方法

```bash
python log_analyzer.py sample_access.log
```

### オプション付きの実行例

```bash
# ERRORレベルのみ表示
python log_analyzer.py sample_access.log --level ERROR

# 特定のキーワードを含む行を検索
python log_analyzer.py sample_access.log --keyword "Database"

# 最大5件まで表示
python log_analyzer.py sample_access.log --max 5

# 複数の条件を組み合わせ
python log_analyzer.py sample_access.log --level ERROR --keyword "connection"

# 統計情報のみ表示
python log_analyzer.py sample_access.log --stats-only

# 詳細表示（ファイル名と行番号を含む）
python log_analyzer.py sample_access.log --verbose
```

### ヘルプの表示

```bash
python log_analyzer.py --help
```

---

## 各項目の解説とコード内の該当箇所

### ① for文やif文で使うbreakとcontinue

**場所:** `analyze_logs()` 関数内（95〜135行目付近）

**continueの使用例:**
```python
for line_num, line in enumerate(f, start=1):
    line = line.strip()
    
    # 空行はスキップ（continue）
    if not line:
        continue  # ← ここで次のループへ
```

**学習ポイント:**
- `continue`は現在のループをスキップし、次の繰り返しへ進む
- 空行や不要なデータを除外する際に便利

**breakの使用例:**
```python
# 最大表示件数に達したらループを抜ける
if max_results and len(results['matched_lines']) >= max_results:
    print(f"最大表示件数（{max_results}件）に達したため、処理を終了します")
    break  # ← ここでループを終了
```

**学習ポイント:**
- `break`はループ全体を終了する
- 条件を満たしたら処理を打ち切る際に使用

---

### ② *args, **kwargs（可変長引数とアンパック）

**場所:** `print_log_info()` 関数（30〜48行目）、`analyze_logs()` 関数（51行目）

**可変長引数の定義:**
```python
def print_log_info(*messages, **options):
    """
    *messages: 任意の数の位置引数を受け取る（タプルになる）
    **options: 任意の数のキーワード引数を受け取る（辞書になる）
    """
    prefix = options.get('prefix', '[INFO]')
    message = ' | '.join(str(msg) for msg in messages)
```

**呼び出し例:**
```python
print_log_info(
    "メッセージ1",
    "メッセージ2", 
    "メッセージ3",
    prefix="[START]",
    separator=" - "
)
```

**アンパックの使用例:**
```python
# リストをアンパックして位置引数として渡す
results = analyze_logs(*args.logfiles, **filters)

# 辞書をアンパックしてキーワード引数として渡す
display_results(results, **display_opts)
```

**学習ポイント:**
- `*args`：複数の位置引数をタプルとして受け取る
- `**kwargs`：複数のキーワード引数を辞書として受け取る
- `*変数`：リストやタプルをアンパックして引数として展開
- `**変数`：辞書をアンパックしてキーワード引数として展開

---

### ③ 比較演算子の短絡評価

**場所:** `analyze_logs()` 関数内（108〜118行目）

```python
# 短絡評価の例1
if level_filter and level_filter not in line:
    continue

# 短絡評価の例2
if keyword_filter and keyword_filter not in line:
    continue

# 短絡評価の例3
if max_results and len(results['matched_lines']) >= max_results:
    break
```

**学習ポイント:**
- **and演算子**: 左辺が`False`なら右辺は評価されない
  - `level_filter`が`None`（False）の場合、`level_filter not in line`は評価されない
  - これにより`None`に対する不正な操作を防ぐ
  
- **短絡評価のメリット**:
  - 不要な処理をスキップして効率的
  - エラーを防ぐ（`None`に対する操作を回避）

**動作の違い:**
```python
# 短絡評価あり（安全）
if level_filter and level_filter not in line:
    # level_filterがNoneの時、右辺は評価されない

# 短絡評価なし（危険）
if level_filter not in line:
    # level_filterがNoneの時、エラーになる可能性
```

---

### ④ raise文（カスタム例外）

**場所:** 例外クラス定義（18〜29行目）、例外の発生（139〜144行目）

**カスタム例外クラスの定義:**
```python
class LogAnalyzerError(Exception):
    """ログ分析ツール専用の例外クラス"""
    pass

class LogFileNotFoundError(LogAnalyzerError):
    """ログファイルが見つからない場合の例外"""
    pass
```

**例外を発生させる:**
```python
try:
    with open(log_file, 'r', encoding='utf-8') as f:
        # ファイル処理
        pass
except FileNotFoundError:
    # カスタム例外を発生させる
    raise LogFileNotFoundError(f"ログファイルが見つかりません: {log_file}")
```

**例外をキャッチする（main関数内）:**
```python
try:
    results = analyze_logs(*args.logfiles, **filters)
except LogFileNotFoundError as e:
    print(f"エラー: {e}")
    return 1
except LogAnalyzerError as e:
    print(f"エラー: {e}")
    return 1
```

**学習ポイント:**
- `raise`文で例外を明示的に発生させる
- カスタム例外クラスを定義することで、エラーの種類を明確化
- 適切なエラーハンドリングにより、プログラムの堅牢性が向上

---

### ⑤ argparse/ArgumentParser

**場所:** `main()` 関数内（171〜238行目）

**ArgumentParserの作成:**
```python
parser = argparse.ArgumentParser(
    description='ログファイルを分析するツール',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="使用例が表示される部分"
)
```

**位置引数の追加:**
```python
parser.add_argument(
    'logfiles',
    nargs='+',  # 1つ以上の引数を受け取る
    help='分析対象のログファイルパス'
)
```

**オプション引数の追加:**
```python
# 選択肢を限定
parser.add_argument(
    '-l', '--level',
    choices=['ERROR', 'WARNING', 'INFO'],
    help='特定のログレベルのみ表示'
)

# 整数型
parser.add_argument(
    '-m', '--max',
    type=int,
    help='最大表示件数を指定'
)

# フラグ（True/False）
parser.add_argument(
    '-v', '--verbose',
    action='store_true',
    help='詳細情報を表示'
)
```

**引数の解析:**
```python
args = parser.parse_args()

# 解析結果の使用
if args.level:
    filters['level'] = args.level
if args.verbose:
    display_opts['verbose'] = True
```

**学習ポイント:**
- `argparse`モジュールでコマンドライン引数を簡単に処理
- `nargs='+'`で複数の値を受け取る
- `choices`で選択肢を制限
- `type`で型変換を自動化
- `action='store_true'`でフラグを実装

---

## プログラムの実行フロー

1. **コマンドライン引数の解析** (`argparse`)
2. **フィルタ条件の準備** (辞書作成)
3. **ログファイルの読み込みと分析**
   - ファイルが見つからない場合は例外発生 (`raise`)
   - 各行を処理 (`for`ループ)
   - 空行をスキップ (`continue`)
   - フィルタ条件を短絡評価でチェック
   - 最大件数に達したら終了 (`break`)
4. **結果の表示** (可変長引数でオプション渡し)
5. **エラーハンドリング** (カスタム例外のキャッチ)

---

## 演習課題

このプログラムを理解したら、以下の課題にチャレンジしてみましょう：

### 初級
1. `sample_access.log`に新しいログ行を追加してみる
2. 異なるフィルタ条件で実行し、結果の違いを確認する
3. 新しいログレベル（例：DEBUG）を追加する

### 中級
4. 日付範囲でフィルタリングする機能を追加する
5. 分析結果をCSVファイルに出力する機能を追加する
6. 正規表現を使ったキーワード検索機能を追加する

### 上級
7. 複数のログファイルをマージして時系列順に表示する
8. ログの統計情報をグラフ化する
9. リアルタイムでログを監視する機能（`tail -f`のような動作）

---

## まとめ

このプログラムでは、Pythonエンジニア基礎検定で問われる重要な項目を実践的に学習できます。
各項目がどのように実際のプログラムで使われるかを理解し、自分でもコードを書いて試してみましょう！
