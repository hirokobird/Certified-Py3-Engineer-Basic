'''
Geminiが生成したそのままVer
'''

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# ---------------------------------------------------------
# 1. クラスの定義
# ---------------------------------------------------------
class Student:
    # クラス変数：全員共通の合格ライン
    PASSING_SCORE = 200

    def __init__(self, name, classname, jp, math, eng):
        self.name = name
        self.classname = classname  # ここに「普通科」などが入る
        self.jp = int(jp)
        self.math = int(math)
        self.eng = int(eng)
    
    def calc_total(self):
        return self.jp + self.math + self.eng

    def calc_average(self):
        return round(self.calc_total() / 3, 1)
    
    def get_status(self):
        return "合格" if self.calc_total() >= Student.PASSING_SCORE else "不合格"

# 継承：体育科クラス
class SportsStudent(Student):
    def __init__(self, name, classname, jp, math, eng, sport):
        super().__init__(name, classname, jp, math, eng)
        self.sport = int(sport)

    # 合計計算をオーバーライド
    def calc_total(self):
        return super().calc_total() + self.sport
    
    # 平均計算もオーバーライド（4科目）
    def calc_average(self):
        return round(self.calc_total() / 4, 1)

# ---------------------------------------------------------
# 2. GUIアプリの構築
# ---------------------------------------------------------
def add_student():
    # 入力値を取得
    classname = combo_classname.get()  # プルダウンから取得
    name = entry_name.get()
    jp = entry_jp.get()
    math = entry_math.get()
    eng = entry_eng.get()
    sport = entry_sport.get()

    # 基本エラーチェック
    if not classname or not name or not jp or not math or not eng:
        messagebox.showerror("エラー", "基本項目を全て入力してください")
        return

    try:
        # ★ここで条件分岐：クラス名（classname）によって生成するオブジェクトを変える
        if classname == "普通科":
            # 普通科クラスのインスタンス化（sportは無視）
            new_student = Student(name, classname, jp, math, eng)
            
        elif classname == "体育科":
            # 体育科クラスのインスタンス化
            if not sport:
                messagebox.showerror("エラー", "体育科は実技点の入力が必要です")
                return
            new_student = SportsStudent(name, classname, jp, math, eng, sport)
        
        else:
            messagebox.showerror("エラー", "不明なクラス名です")
            return
        
        # --- 以下、表示処理（共通） ---
        
        # どちらのクラスで作られていても、同じメソッド名で計算できる（ポリモーフィズム）
        total = new_student.calc_total()
        avg = new_student.calc_average()
        status = new_student.get_status()

        # 体育の点数表示用（普通科はハイフン）
        # getattrを使うと「もしsport属性があれば取得、なければ"-"」という処理が書ける
        sport_display = getattr(new_student, "sport", "-")

        tree.insert("", "end", values=(
            new_student.classname, # ここが「普通科」か「体育科」になる
            new_student.name,
            new_student.jp, 
            new_student.math, 
            new_student.eng, 
            sport_display, 
            total, 
            avg,
            status
        ))
        
        # 入力欄クリア（今回は省略せず記述）
        entry_name.delete(0, tk.END)
        entry_jp.delete(0, tk.END)
        entry_math.delete(0, tk.END)
        entry_eng.delete(0, tk.END)
        entry_sport.delete(0, tk.END)
        
    except ValueError:
        messagebox.showerror("エラー", "点数は半角数字で入力してください")

# メインウィンドウ
root = tk.Tk()
root.title("クラス成績管理アプリ（継承編）")
root.geometry("750x450")

input_frame = tk.Frame(root, pady=10)
input_frame.pack()

# --- 入力項目の配置 ---

# ★クラス名選択（プルダウンに変更）
tk.Label(input_frame, text="所属:").grid(row=0, column=0)
combo_classname = ttk.Combobox(input_frame, values=["普通科", "体育科"], width=8, state="readonly")
combo_classname.current(0) # 初期値は普通科
combo_classname.grid(row=0, column=1, padx=5)

tk.Label(input_frame, text="氏名:").grid(row=0, column=2)
entry_name = tk.Entry(input_frame, width=12)
entry_name.grid(row=0, column=3)

tk.Label(input_frame, text="国:").grid(row=0, column=4)
entry_jp = tk.Entry(input_frame, width=4)
entry_jp.grid(row=0, column=5)

tk.Label(input_frame, text="数:").grid(row=0, column=6)
entry_math = tk.Entry(input_frame, width=4)
entry_math.grid(row=0, column=7)

tk.Label(input_frame, text="英:").grid(row=0, column=8)
entry_eng = tk.Entry(input_frame, width=4)
entry_eng.grid(row=0, column=9)

# 体育科用の実技点
tk.Label(input_frame, text="体(実技):").grid(row=0, column=10)
entry_sport = tk.Entry(input_frame, width=4, bg="#e0ffff")
entry_sport.grid(row=0, column=11)

# 追加ボタン
btn_add = tk.Button(input_frame, text="追加", command=add_student, bg="#dddddd")
btn_add.grid(row=0, column=12, padx=10)

# --- 表の設定 ---
# 「Type」カラムを削除し、Classに統合
columns = ("Class", "Name", "JP", "Math", "Eng", "Sport", "Total", "Avg", "Status")
tree = ttk.Treeview(root, columns=columns, show="headings")

tree.heading("Class", text="所属")
tree.heading("Name", text="氏名")
tree.heading("JP", text="国")
tree.heading("Math", text="数")
tree.heading("Eng", text="英")
tree.heading("Sport", text="体")
tree.heading("Total", text="合計")
tree.heading("Avg", text="平均")
tree.heading("Status", text="合否")

# 列幅調整
for col in columns:
    tree.column(col, width=60, anchor="center")
tree.column("Class", width=80)
tree.column("Name", width=100)

tree.pack(pady=20, fill="both", expand=True)

root.mainloop()