"""
成績表アプリ - Pythonクラスの学習用
Tkinterを使用して生徒の成績を管理するアプリケーション
"""

import tkinter as tk
from tkinter import ttk, messagebox


class Student:
    """生徒クラス - 生徒の情報と成績を管理"""
    
    def __init__(self, name, japanese, math, english):
        """
        生徒の初期化
        
        Parameters:
        -----------
        name : str
            生徒の氏名
        japanese : int
            国語の点数
        math : int
            数学の点数
        english : int
            英語の点数
        """
        self.name = name
        self.japanese = japanese
        self.math = math
        self.english = english
    
    def calculate_total(self):
        """合計点を計算するメソッド"""
        return self.japanese + self.math + self.english
    
    def calculate_average(self):
        """平均点を計算するメソッド"""
        return self.calculate_total() / 3
    
    def get_info(self):
        """生徒の情報を辞書形式で返すメソッド"""
        return {
            '氏名': self.name,
            '国語': self.japanese,
            '数学': self.math,
            '英語': self.english,
            '合計': self.calculate_total(),
            '平均': f"{self.calculate_average():.1f}"
        }


class GradeApp:
    """成績表アプリケーションのメインクラス"""
    
    def __init__(self, root):
        """
        アプリケーションの初期化
        
        Parameters:
        -----------
        root : tk.Tk
            Tkinterのルートウィンドウ
        """
        self.root = root
        self.root.title("成績表アプリ")
        self.root.geometry("800x600")
        
        # 生徒リストを保存するリスト
        self.students = []
        
        # UIの構築
        self.create_widgets()
    
    def create_widgets(self):
        """ウィジェットを作成"""
        
        # タイトル
        title_label = tk.Label(
            self.root, 
            text="生徒成績管理システム",
            font=("Arial", 20, "bold"),
            bg="#2C3E50",
            fg="white",
            pady=15
        )
        title_label.pack(fill=tk.X)
        
        # 入力フレーム
        input_frame = tk.Frame(self.root, bg="#ECF0F1", padx=20, pady=20)
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # 入力フィールド
        fields = [
            ("氏名:", "name"),
            ("国語:", "japanese"),
            ("数学:", "math"),
            ("英語:", "english")
        ]
        
        self.entries = {}
        
        for i, (label_text, field_name) in enumerate(fields):
            # ラベル
            label = tk.Label(
                input_frame,
                text=label_text,
                font=("Arial", 12),
                bg="#ECF0F1",
                width=10,
                anchor="w"
            )
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
            
            # 入力欄
            entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[field_name] = entry
        
        # ボタンフレーム
        button_frame = tk.Frame(input_frame, bg="#ECF0F1")
        button_frame.grid(row=len(fields), column=0, columnspan=2, pady=10)
        
        # 追加ボタン
        add_button = tk.Button(
            button_frame,
            text="生徒を追加",
            font=("Arial", 12, "bold"),
            bg="#27AE60",
            fg="white",
            padx=20,
            pady=5,
            command=self.add_student
        )
        add_button.pack(side=tk.LEFT, padx=5)
        
        # クリアボタン
        clear_button = tk.Button(
            button_frame,
            text="クリア",
            font=("Arial", 12),
            bg="#95A5A6",
            fg="white",
            padx=20,
            pady=5,
            command=self.clear_inputs
        )
        clear_button.pack(side=tk.LEFT, padx=5)
        
        # テーブルフレーム
        table_frame = tk.Frame(self.root, bg="white", padx=10, pady=10)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # テーブルラベル
        table_label = tk.Label(
            table_frame,
            text="成績一覧",
            font=("Arial", 14, "bold"),
            bg="white"
        )
        table_label.pack(anchor="w", pady=(0, 10))
        
        # スクロールバー
        scrollbar = tk.Scrollbar(table_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Treeview（テーブル）
        columns = ('氏名', '国語', '数学', '英語', '合計', '平均')
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show='headings',
            yscrollcommand=scrollbar.set,
            height=10
        )
        
        # スクロールバーの設定
        scrollbar.config(command=self.tree.yview)
        
        # 列の設定
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor='center')
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # スタイル設定
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            "Treeview",
            background="white",
            foreground="black",
            rowheight=30,
            fieldbackground="white",
            font=("Arial", 11)
        )
        style.configure(
            "Treeview.Heading",
            font=("Arial", 12, "bold"),
            background="#34495E",
            foreground="white"
        )
        style.map('Treeview', background=[('selected', '#3498DB')])
    
    def validate_score(self, score_str, subject):
        """
        点数の入力を検証
        
        Parameters:
        -----------
        score_str : str
            入力された点数（文字列）
        subject : str
            科目名
            
        Returns:
        --------
        int or None
            有効な点数、または無効な場合はNone
        """
        try:
            score = int(score_str)
            if 0 <= score <= 100:
                return score
            else:
                messagebox.showerror(
                    "入力エラー",
                    f"{subject}の点数は0〜100の範囲で入力してください。"
                )
                return None
        except ValueError:
            messagebox.showerror(
                "入力エラー",
                f"{subject}の点数は整数で入力してください。"
            )
            return None
    
    def add_student(self):
        """生徒を追加"""
        # 入力値の取得
        name = self.entries['name'].get().strip()
        japanese_str = self.entries['japanese'].get().strip()
        math_str = self.entries['math'].get().strip()
        english_str = self.entries['english'].get().strip()
        
        # 氏名のチェック
        if not name:
            messagebox.showerror("入力エラー", "氏名を入力してください。")
            return
        
        # 点数の検証
        japanese = self.validate_score(japanese_str, "国語")
        if japanese is None:
            return
        
        math = self.validate_score(math_str, "数学")
        if math is None:
            return
        
        english = self.validate_score(english_str, "英語")
        if english is None:
            return
        
        # Studentクラスのインスタンスを作成
        student = Student(name, japanese, math, english)
        self.students.append(student)
        
        # テーブルに追加
        info = student.get_info()
        self.tree.insert(
            '',
            'end',
            values=(
                info['氏名'],
                info['国語'],
                info['数学'],
                info['英語'],
                info['合計'],
                info['平均']
            )
        )
        
        # 入力欄をクリア
        self.clear_inputs()
        
        messagebox.showinfo("成功", f"{name}さんの成績を登録しました。")
    
    def clear_inputs(self):
        """入力欄をクリア"""
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        
        # 氏名入力欄にフォーカス
        self.entries['name'].focus()


def main():
    """メイン関数"""
    root = tk.Tk()
    app = GradeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
