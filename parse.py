import argparse

parser = argparse.ArgumentParser() #argparseを使う準備
parser.add_argument("--head") #オプション引数の定義
parser.add_argument("body", nargs="+") #引数の定義
#引数の定義は3、4…行と追加可能
args = parser.parse_args() #判断と整理
print(args)

# ＊＊＊説明資料用＊＊＊

import argparse

# 1. パーサー（受付係）を作る
parser = argparse.ArgumentParser(description='数値を2乗するプログラム')

# 2. 引数を定義する： add_argument() で、「どんな引数が必要か」を登録します。
parser.add_argument('number', type=int, help='計算したい数値') # 整数型の数値が来ると設定（引数の定義は3、4…行と追加可能）
parser.add_argument('--verbose', action='store_true', help='詳細を表示するか') # オプション

# 3. 解析する： parse_args() を呼ぶだけで解析済みのデータが手に入る（sys.argvの中身を整理してくれる）
args = parser.parse_args()

# --- ここからメイン処理 ---

# ★ここがすごい！ args.number は自動的に「整数」になっている
result = args.number ** 2

if args.verbose:
    print(f"{args.number} の2乗は {result} です。")
else:
    print(result)