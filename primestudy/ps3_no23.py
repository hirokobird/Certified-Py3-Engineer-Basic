
# No.23 補足説明用コード

d = {
    "banana": 100,
    "apple": 200,
    "orange": 150
}


# パターン1: キーだけにenumerate
for i, key in enumerate(d):
    print(f"{i}番目のキー: {key}")
# 0番目のキー: banana
# 1番目のキー: apple
# 2番目のキー: orange

# パターン2: キーと値の両方を取得
for i, (key, value) in enumerate(d.items()):
    print(f"{i}: {key} = {value}")
# 0: banana = 100
# 1: apple = 200
# 2: orange = 150

# パターン2の補足: インデックスなしでキーと値の両方を取得
# 辞書は序列を持っているがindexを持たない。
for key, value in d.items():
    print(f"{key} = {value}")
# banana = 100
# apple = 200
# orange = 150

# パターン3: インデックスを1から開始
for i, (key, value) in enumerate(d.items(), start=1):
    print(f"{i}. {key}: {value}円")
# 1. banana: 100円
# 2. apple: 200円
# 3. orange: 150円