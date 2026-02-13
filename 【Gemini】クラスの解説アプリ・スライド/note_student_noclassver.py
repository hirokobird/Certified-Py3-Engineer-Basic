# ---------------------------------------------------------
# 1. 関数（処理）の定義
# ---------------------------------------------------------

# 合計点を計算する関数
# ※ 引数として「生徒データ（辞書）」を受け取る必要がある
def calc_total(student_data):
    return student_data["jp"] + student_data["math"] + student_data["eng"]

# 平均点を計算する関数
def calc_average(student_data):
    total = calc_total(student_data) # 上で作った関数を使う
    return round(total / 3, 1)

# 結果を出力する関数
def print_result(student_data):
    total = calc_total(student_data)
    avg = calc_average(student_data)
    print(f"【{student_data['classname']}】{student_data['name']}さん のテスト結果：合計点 {total} / 平均点 {avg}です")

# ---------------------------------------------------------
# 2. メイン処理
# ---------------------------------------------------------

# 生徒Aのデータを作成（辞書型でまとめる）
student_a = {
    "name": "A山T太",
    "classname": "普通科",
    "jp": 55,
    "math": 65,
    "eng": 70
}

# 生徒Bのデータを作成
student_b = {
    "name": "B川C美",
    "classname": "普通科",
    "jp": 85,
    "math": 95,
    "eng": 80
}

# 関数にデータを渡して実行
# クラス版では student_a.result() だったが、
# こちらは 関数(データ) という書き方になる
print_result(student_a)
print_result(student_b)