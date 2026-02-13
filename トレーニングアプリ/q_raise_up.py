import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": """問1
次のコードを実行したときの出力として正しい組み合わせはどれか。

class MyError(Exception):
    pass

def func_a():
    print("A")
    raise MyError
    print("B")

def func_b():
    try:
        print("C")
        func_a()
    except MyError:
        print("D")
        raise Exception

try:
    func_b()
except Exception:
    print("E")
""",
        "choices": [
            "A B C D E",
            "C A D E",
            "C A B D E",
            "A C D E",
            "C A E"
        ],
        "answer": 2,
        "explanation": "func_b内でC→func_a内でA→MyError発生→func_b exceptでD→Exception再送出→外側exceptでE。"
    },
    {
        "question": """問2
次のコードを実行したときの出力として正しいものはどれか。

class XError(Exception):
    pass

def raise_x():
    print("P")
    raise XError
    print("Q")

def main():
    try:
        print("R")
        raise_x()
    except XError:
        print("S")
        raise Exception

try:
    main()
except Exception:
    print("T")
""",
        "choices": [
            "R P Q S T",
            "P R S T",
            "R P S T",
            "R S P T",
            "R P S"
        ],
        "answer": 3,
        "explanation": "main内でR→raise_x内でP→XError発生→main exceptでS→Exception再送出→外側exceptでT。"
    },
    {
        "question": """問3
次のコードを実行したときの出力として正しいものはどれか。

class AError(Exception):
    pass

def inner():
    print("X")
    raise AError
    print("Y")

def outer():
    try:
        print("Z")
        inner()
    except AError:
        print("W")
        raise Exception

try:
    outer()
except Exception:
    print("V")
""",
        "choices": [
            "Z X W V",
            "X Z W V",
            "Z X V W",
            "Z X W",
            "X Z V W"
        ],
        "answer": 1,
        "explanation": "outerでZ→innerでX→AError発生→outer exceptでW→Exception再送出→外側exceptでV。"
    },
    {
        "question": """問4
次のコードを実行したときの出力として正しいものはどれか。

class MyErr(Exception):
    pass

def alpha():
    print("1")
    raise MyErr
    print("2")

def beta():
    try:
        print("3")
        alpha()
    except MyErr:
        print("4")
        raise Exception

try:
    beta()
except Exception:
    print("5")
""",
        "choices": [
            "3 1 4 5",
            "1 3 4 5",
            "3 1 2 4 5",
            "3 4 1 5",
            "1 3 5"
        ],
        "answer": 1,
        "explanation": "betaで3→alphaで1→MyErr発生→beta exceptで4→Exception再送出→外側exceptで5。"
    },
    {
        "question": """問5
次のコードを実行したときの出力として正しいものはどれか。

class FooError(Exception):
    pass

def f1():
    print("M")
    raise FooError
    print("N")

def f2():
    try:
        print("O")
        f1()
    except FooError:
        print("P")
        raise Exception

try:
    f2()
except Exception:
    print("Q")
""",
        "choices": [
            "O M P Q",
            "M O P Q",
            "O M N P Q",
            "O P M Q",
            "M O Q"
        ],
        "answer": 1,
        "explanation": "f2でO→f1でM→FooError発生→f2 exceptでP→Exception再送出→外側exceptでQ。"
    },
    {
        "question": """問6
次のコードを実行したときの出力として正しいものはどれか。

class SpecialErr(Exception):
    pass

def step1():
    print("a")
    raise SpecialErr
    print("b")

def step2():
    try:
        print("c")
        step1()
    except SpecialErr:
        print("d")
        raise Exception

try:
    step2()
except Exception:
    print("e")
""",
        "choices": [
            "c a d e",
            "a c d e",
            "c a b d e",
            "c d a e",
            "a c e"
        ],
        "answer": 1,
        "explanation": "step2でc→step1でa→SpecialErr発生→step2 exceptでd→Exception再送出→外側exceptでe。"
    },
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python CBTクイズ（問6レベル）")
        self.q_index = 0
        self.score = 0

        # 問題文
        self.question_label = tk.Label(root, text="", justify="left", wraplength=700, anchor="w")
        self.question_label.pack(pady=10)

        # 選択肢フレーム（横並び）
        self.choice_frame = tk.Frame(root)
        self.choice_frame.pack(pady=5)

        self.choice_buttons = []
        for i in range(5):
            btn = tk.Button(self.choice_frame, text="", width=15, command=lambda idx=i: self.check_answer(idx+1))
            btn.pack(side="left", padx=5)
            self.choice_buttons.append(btn)

        # 次へボタン
        self.next_button = tk.Button(root, text="次へ", command=self.next_question, state="disabled")
        self.next_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        q = questions[self.q_index]
        self.question_label.config(text=q["question"])
        for i, choice in enumerate(q["choices"]):
            self.choice_buttons[i].config(text=choice, state="normal")
        self.next_button.config(state="disabled")

    def check_answer(self, choice):
        q = questions[self.q_index]
        if choice == q["answer"]:
            messagebox.showinfo("結果", "正解！\n\n" + q["explanation"])
            self.score += 1
        else:
            messagebox.showinfo("結果", f"不正解！ 正解は {q['answer']} です。\n\n" + q["explanation"])
        for btn in self.choice_buttons:
            btn.config(state="disabled")
        self.next_button.config(state="normal")

    def next_question(self):
        self.q_index += 1
        if self.q_index >= len(questions):
            messagebox.showinfo("終了", f"全問題終了！ 正解数: {self.score}/{len(questions)}")
            self.root.quit()
        else:
            self.show_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
