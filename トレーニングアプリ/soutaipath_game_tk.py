import tkinter as tk
from tkinter import messagebox
import random
import posixpath

# === 仮想ファイルシステム生成 ===
def generate_file_system():
    base_options = ["/home/user", "/users/student", "/mnt/data/user1"]
    base = random.choice(base_options)

    folders = [
        "docs", "images", "projects", "notes", "backup", "reports",
        "photos", "personal", "shared", "archive"
    ]
    files = [
        "readme.txt", "todo.md", "journal.txt", "code.py", "report.pdf",
        "trip.jpg", "family.png", "summary.docx", "data.csv", "index.html"
    ]

    file_system = {}
    depth = random.randint(3, 6)

    # ルートにいくつかのフォルダとファイルを追加
    file_system[base] = random.sample(folders, 3) + random.sample(files, 2)

    # 再帰的にディレクトリ構造を構築
    paths = [base]
    for _ in range(depth * 2):
        parent = random.choice(paths)
        new_folder = random.choice(folders)
        new_path = f"{parent}/{new_folder}"
        if new_path not in file_system:
            file_system[new_path] = random.sample(folders, random.randint(0, 2)) + \
                                    random.sample(files, random.randint(1, 3))
            paths.append(new_path)

    return file_system

# 相対パス生成
def get_relative_path(from_path, to_path):
    return posixpath.relpath(to_path, start=from_path)

# クイズ問題生成（難易度で深さ制限）
def generate_quizzes(fs, difficulty="easy"):
    dirs = list(fs.keys())
    files = []
    for path, items in fs.items():
        for item in items:
            full = posixpath.join(path, item)
            if "." in item:
                files.append(full)
            else:
                dirs.append(full)
    all_paths = dirs + files

    max_depth_diff = {"easy": 2, "medium": 3, "hard": 5}[difficulty]
    max_absolute_depth = {"easy": 4, "medium": 6, "hard": 10}[difficulty]

    def depth(path):
        return len(path.strip("/").split("/"))

    quizzes = []
    for _ in range(100):
        src = random.choice(dirs)
        dst = random.choice(all_paths)
        if (
            src != dst and
            abs(depth(src) - depth(dst)) <= max_depth_diff and
            max(depth(src), depth(dst)) <= max_absolute_depth
        ):
            quizzes.append((src, dst, get_relative_path(src, dst)))
    return quizzes

# === GUIアプリ ===
class PathTrainerApp:
    def __init__(self, master):
        self.master = master
        master.title("相対パストレーニング")

        self.difficulty = tk.StringVar(value="medium")

        self.create_difficulty_selector()

    def create_difficulty_selector(self):
        frame = tk.Frame(self.master)
        frame.pack(pady=20)

        tk.Label(frame, text="難易度を選択してください：", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        tk.OptionMenu(frame, self.difficulty, "easy", "medium", "hard").pack(side=tk.LEFT, padx=5)

        tk.Button(frame, text="開始", command=self.start_game).pack(side=tk.LEFT, padx=10)

    def start_game(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        self.fs = generate_file_system()
        self.quizzes = generate_quizzes(self.fs, difficulty=self.difficulty.get())
        random.shuffle(self.quizzes)
        self.score = 0
        self.total = 5
        self.current = 0

        self.title_label = tk.Label(self.master, text="相対パスを入力してください：", font=("Arial", 14))
        self.title_label.pack(pady=10)

        self.info_text = tk.Text(self.master, height=10, width=70)
        self.info_text.pack()
        self.info_text.configure(state='disabled')

        self.entry = tk.Entry(self.master, width=50)
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", self.check_answer)

        self.submit_button = tk.Button(self.master, text="送信", command=self.check_answer)
        self.submit_button.pack()

        self.status_label = tk.Label(self.master, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.current >= self.total:
            messagebox.showinfo("結果", f"終了！スコア: {self.score}/{self.total}")
            self.master.quit()
            return

        self.entry.delete(0, tk.END)
        self.src, self.dst, self.answer = self.quizzes[self.current]

        target_file = posixpath.basename(self.dst)
        if "." in target_file:
            action = f"'{target_file}' を読み込むにはどうすればいい？"
        else:
            action = f"'{target_file}' ディレクトリに移動するには？"

        self.info_text.configure(state='normal')
        self.info_text.delete("1.0", tk.END)
        self.info_text.insert(tk.END, f"現在のディレクトリ: {self.src}\n")
        self.info_text.insert(tk.END, f"目標: {self.dst}\n")
        self.info_text.insert(tk.END, f"操作: {action}\n")
        self.info_text.configure(state='disabled')

        self.status_label.config(text=f"問題 {self.current+1}/{self.total}")

    def check_answer(self, event=None):
        user_input = self.entry.get().strip()
        resolved = posixpath.normpath(posixpath.join(self.src, user_input))
        if resolved == self.dst:
            messagebox.showinfo("正解", "✅ 正解です！")
            self.score += 1
        else:
            messagebox.showerror("不正解", f"❌ 不正解です。\n正解: {self.answer}")

        self.current += 1
        self.load_question()


if __name__ == "__main__":
    root = tk.Tk()
    app = PathTrainerApp(root)
    root.mainloop()
