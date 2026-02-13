import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# ---------------------------------------------------------
# 1. クラスの定義（設計図）
# ---------------------------------------------------------
class Student:
    # ★クラス変数：全員共通の合格ライン
    PASSING_SCORE = 200

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
        # 平均は科目数で割る（体育科は4で割る必要があるため、lenで管理もできるが今回は簡易的に3）
        return round(self.calc_total() / 3, 1)
    
    # ★合否判定
    def get_status(self):
        return "合格" if self.calc_total() >= Student.PASSING_SCORE else "不合格"
    
    #結果を出力するメソッド
    def result(self):
        print(
            f"【{self.classname}組】{self.name}さんのテスト結果：合計点{self.calc_total()} / 平均点{self.calc_average()}です"
            )
        

# student01 = Student("徳重博子", "さくら", 75, 65, 80).result()
# result関数は以下に置き換えも可能 
# print(f"【{student01.classname}組】{student01.name}さんのテスト結果：合計点{student01.calc_total()} / 平均点{student01.calc_average()}です")

# ---------------------------------------------------------
# 2. Studentクラス（親）を継承した、SportsStudent（子）を作る
# ---------------------------------------------------------

# ★継承：体育科クラス
class SportsStudent(Student):
    def __init__(self, name, classname, jp, math, eng, sport):
        # 親クラスの __init__ を呼び出して、基本設定を任せる
        super().__init__(name, classname, jp, math, eng)
        self.sport = int(sport) # ★体育科だけの追加データ

    # 合計計算をオーバーライド（上書き）
    def calc_total(self):
        # 親の計算(3教科) + 体育
        return super().calc_total() + self.sport
    
    # 平均計算もオーバーライド（4科目で割る）
    def calc_average(self):
        return round(self.calc_total() / 4, 1)

# ---------------------------------------------------------
# 3. GUIアプリの構築
# ---------------------------------------------------------
def add_student():
    """登録ボタンが押されたときの処理"""
    # 入力値を取得
    name = entry_name.get()
    classname = entry_classname.get()
    jp = entry_jp.get()
    math = entry_math.get()
    eng = entry_eng.get()
    sport = entry_sport.get() # 体育の点数
    
    # コースの選択状態を取得 (1=普通, 2=体育)
    course_type = var_course.get()

    if not name or not classname or not jp or not math or not eng:
        messagebox.showerror("エラー", "基本項目を全て入力してください")
        return

    try:
        # ★ここで条件分岐：選ばれたコースによって作るインスタンスを変える
        if course_type == 1:
            # 普通科
            new_student = Student(name, classname, jp, math, eng)
        else:
            # 体育科（体育の点数が必須）
            if not sport:
                messagebox.showerror("エラー", "体育科は実技点が必要です")
                return
            new_student = SportsStudent(name, classname, jp, math, eng, sport)
        
        # クラスが違っても、使うメソッド名は同じ（calc_totalなど）
        total = new_student.calc_total()
        avg = new_student.calc_average()
        status = new_student.get_status() # 合否判定

        # 体育の点数表示（普通科はハイフンにする）
        sport_display = new_student.sport if course_type == 2 else "-"

        tree.insert("", "end", values=(
            new_student.classname,
            new_student.name,
            "体育科" if course_type == 2 else "普通科", # コース列追加
            new_student.jp, 
            new_student.math, 
            new_student.eng, 
            sport_display, # 体育列追加
            total, 
            avg,
            status # 合否列追加
        ))
        
        # 入力欄クリア（省略）
        
    except ValueError:
        messagebox.showerror("エラー", "点数は半角数字で入力してください")

# メインウィンドウ
root = tk.Tk()
root.title("クラス成績管理アプリ（継承・クラス変数編）")
root.geometry("800x450") # 少し広げる

input_frame = tk.Frame(root, pady=10)
input_frame.pack()

# --- 入力項目の配置 ---
tk.Label(input_frame, text="クラス:").grid(row=0, column=0)
entry_classname = tk.Entry(input_frame, width=5)
entry_classname.grid(row=0, column=1)

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

# ★体育科用の追加項目
tk.Label(input_frame, text="体(実技):").grid(row=0, column=10)
entry_sport = tk.Entry(input_frame, width=4, bg="#e0ffff") # 色を変えて目立たせる
entry_sport.grid(row=0, column=11)

# ★コース選択ラジオボタン
var_course = tk.IntVar(value=1)
rb_normal = tk.Radiobutton(input_frame, text="普通科", variable=var_course, value=1)
rb_sports = tk.Radiobutton(input_frame, text="体育科", variable=var_course, value=2)
rb_normal.grid(row=1, column=0, columnspan=2)
rb_sports.grid(row=1, column=2, columnspan=2)

btn_add = tk.Button(input_frame, text="追加", command=add_student, bg="#dddddd")
btn_add.grid(row=1, column=10, columnspan=2)

# --- 表の設定 ---
columns = ("Class", "Name", "Type", "JP", "Math", "Eng", "Sport", "Total", "Avg", "Status")
tree = ttk.Treeview(root, columns=columns, show="headings")

tree.heading("Class", text="組")
tree.heading("Name", text="氏名")
tree.heading("Type", text="学科")
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
tree.column("Name", width=100)
tree.column("Type", width=80)

tree.pack(pady=20, fill="both", expand=True)

root.mainloop()