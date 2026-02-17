'''
具体例：日記保存プログラム (diary.py)
argparseを使った一行日記をつけるプログラムです。
'''

import argparse

# 1. 設定を作る
parser = argparse.ArgumentParser(description="一行日記ツール")

# 2. --head: 日記のタイトル（オプション引数：--head ※オプション引数はなくてもいい）
parser.add_argument("--head", help="日記のタイトル")

# 3. --mood：今日の気分（オプション引数：--mood）
parser.add_argument("--mood", help="今日の気分")

# 4. body: 日記の本文（nargs="+" なので、スペース区切りの単語を全部リストにまとめる）
parser.add_argument("body", nargs="+", help="日記の本文")

# 5. 解析実行
args = parser.parse_args()

# --- ここからメイン処理 ---
print(f"【タイトル】: {args.head}")
print(f"【気分】: {args.mood}")
print(f"【本文】: {args.body}")

'''
【コマンドライン上の入力例】
パターンA：タイトル・気分ありの場合
コマンド：
python parse_diary.py --mood "元気" --head 買い物メモ 牛乳と卵  を買う

出力
【タイトル】: 買い物メモ
【気分】: 元気
【本文】: ['牛乳と卵', 'を買う']

パターンB：タイトルと気分なし（オプション省略）の場合
コマンド：
python parse_diary.py 今日はいい天気だ

出力
【タイトル】: None
【気分】: None
【本文】: ['今日はいい天気だ']

パターンC：位置引数とオプション引数の順番を逆に入力した場合
コマンド：
python argparse_diary.py 検査の結果 インフルエンザだった --mood 怠い --head 風邪ぎみで通院

【タイトル】: 風邪ぎみで通院
【気分】: 怠い
【本文】: ['検査の結果', 'インフルエンザだった']
'''