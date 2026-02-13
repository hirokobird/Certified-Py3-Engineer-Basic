import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# ---------------------------------------------------------
# 1. クラスの定義（設計図）
# ---------------------------------------------------------
class Student:
    def __init__(self, name, classname, jp, math, eng):
        self.name = name
        self.classname = classname
        self.jp = int(jp)     # 計算用に整数化
        self.math = int(math)
        self.eng = int(eng)
    
    # 合計点を計算するメソッド
    def calc_total(self):
        return self.jp + self.math + self.eng

    # 平均点を計算するメソッド
    def calc_average(self):
        return round(self.calc_total() / 3, 1) # 小数第1位まで
    
    #結果を出力するメソッド
    def result(self):
        print(
            f"【{self.classname}組】{self.name}さんのテスト結果：合計点{self.calc_total()} / 平均点{self.calc_average()}です"
            )


# student01 = Student("徳重博子", "さくら", 75, 65, 80).result()

# result関数は以下に置き換えも可能 
# print(f"【{student01.classname}組】{student01.name}さんのテスト結果：合計点{student01.calc_total()} / 平均点{student01.calc_average()}です")

# ---------------------------------------------------------
# 2. GUIアプリの構築
# ---------------------------------------------------------
def add_student():
    """登録ボタンが押されたときの処理"""
    # 入力値を取得
    name = entry_name.get()
    classname = entry_classname.get()
    jp = entry_jp.get()
    math = entry_math.get()
    eng = entry_eng.get()

    # エラーチェック（空欄がないか）
    if not name or not classname or not jp or not math or not eng:
        messagebox.showerror("エラー", "全ての項目を入力してください")
        return

    try:
        # ★ここでクラスから「インスタンス（実体）」を作成！★
        new_student = Student(name, classname, jp, math, eng)
        
        # クラスのメソッドを使って計算
        total = new_student.calc_total()
        avg = new_student.calc_average()

        # 表（Treeview）に追加
        tree.insert("", "end", values=(
            new_student.name,
            new_student.classname,
            new_student.jp, 
            new_student.math, 
            new_student.eng, 
            total, 
            avg
        ))
        
        # 入力欄をクリア
        entry_name.delete(0, tk.END)
        entry_jp.delete(0, tk.END)
        entry_math.delete(0, tk.END)
        entry_eng.delete(0, tk.END)
        
    except ValueError:
        messagebox.showerror("エラー", "点数は半角数字で入力してください")

# メインウィンドウ作成
root = tk.Tk()
root.title("クラス成績管理アプリ")
root.geometry("600x400")

# 入力エリアの作成（フレームでまとめる）
input_frame = tk.Frame(root, pady=10)
input_frame.pack()

# 氏名
tk.Label(input_frame, text="氏名:").grid(row=0, column=0)
entry_name = tk.Entry(input_frame, width=15)
entry_name.grid(row=0, column=1, padx=5)

# クラス名
tk.Label(input_frame, text="クラス名:").grid(row=0, column=2)
entry_classname = tk.Entry(input_frame, width=10)
entry_classname.grid(row=0, column=3, padx=5)

# 国語
tk.Label(input_frame, text="国語:").grid(row=0, column=4)
entry_jp = tk.Entry(input_frame, width=5)
entry_jp.grid(row=0, column=5, padx=5)

# 数学
tk.Label(input_frame, text="数学:").grid(row=0, column=6)
entry_math = tk.Entry(input_frame, width=5)
entry_math.grid(row=0, column=7, padx=5)

# 英語
tk.Label(input_frame, text="英語:").grid(row=0, column=8)
entry_eng = tk.Entry(input_frame, width=5)
entry_eng.grid(row=0, column=9, padx=5)

# 登録ボタン
btn_add = tk.Button(input_frame, text="成績追加", command=add_student, bg="#dddddd")
btn_add.grid(row=0, column=10, padx=10)

# 表（Treeview）の作成
columns = ("Name", "Classname", "JP", "Math", "Eng", "Total", "Avg")
tree = ttk.Treeview(root, columns=columns, show="headings")

# ヘッダーの設定
tree.heading("Name", text="氏名")
tree.heading("Classname", text="クラス名")
tree.heading("JP", text="国語")
tree.heading("Math", text="数学")
tree.heading("Eng", text="英語")
tree.heading("Total", text="合計")
tree.heading("Avg", text="平均")

# 列幅の設定
for col in columns:
    tree.column(col, width=80, anchor="center")

tree.pack(pady=20, fill="both", expand=True)

root.mainloop()