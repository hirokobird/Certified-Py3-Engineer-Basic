import tkinter as tk
from tkinter import messagebox


# 中級レベル 8問（問5相当）
questions = [
    {
        "question": """問1
次のコードの出力として正しいものはどれか。

def inner():
    try:
        print("A")
        raise ValueError
    except ValueError:
        print("B")
        raise Exception

try:
    inner()
except Exception:
    print("C")
""",
        "choices": [
            "A\nB",
            "A\nB\nC",
            "A\nC",
            "エラーで終了する"
        ],
        "answer": 2,
        "explanation": "inner内でValueErrorを捕捉後にExceptionを再送出し、外側で捕捉してCを表示します。"
    },
    {
        "question": """問2
次のコードの出力として正しいものはどれか。

def outer():
    try:
        print("X")
        inner()
    except Exception:
        print("Z")

def inner():
    try:
        print("Y")
        raise KeyError
    except KeyError:
        print("K")
        raise

outer()
""",
        "choices": [
            "X\nY\nK\nZ",
            "X\nY\nK",
            "X\nY\nZ",
            "エラーで終了する"
        ],
        "answer": 1,
        "explanation": "innerでKeyErrorを捕捉してKを出力後、再送出→outerのexceptでZ。"
    },
    {
        "question": """問3
次のコードの出力として正しいものはどれか。

try:
    try:
        print("Start")
        raise ValueError
    except ValueError:
        print("Inner")
        raise
except Exception:
    print("Outer")
""",
        "choices": [
            "Start\nOuter",
            "Start\nInner\nOuter",
            "Inner\nOuter",
            "エラーで終了する"
        ],
        "answer": 2,
        "explanation": "内側exceptでInnerを出力後、raiseで再送出→外側exceptでOuter。"
    },
    {
        "question": """問4
次のコードの出力として正しいものはどれか。

def func():
    try:
        raise ValueError
    except ValueError:
        print("Caught")
        raise KeyError

try:
    func()
except KeyError:
    print("Handled KeyError")
""",
        "choices": [
            "Caught",
            "Caught\nHandled KeyError",
            "エラーで終了する",
            "Handled KeyError"
        ],
        "answer": 2,
        "explanation": "func内でValueErrorを捕捉後、KeyErrorを送出→外側exceptで処理。"
    },
    {
        "question": """問5
次のコードの出力として正しいものはどれか。

def a():
    try:
        raise ValueError
    except ValueError:
        print("A")
        raise

def b():
    try:
        a()
    except ValueError:
        print("B")

b()
""",
        "choices": [
            "A",
            "A\nB",
            "B\nA",
            "エラーで終了する"
        ],
        "answer": 2,
        "explanation": "a()でValueErrorを捕捉しAを出力後、再送出→bのexceptでB。"
    },
    {
        "question": """問6
次のコードの出力として正しいものはどれか。

try:
    raise ValueError
except ValueError:
    print("V")
    try:
        raise KeyError
    except KeyError:
        print("K")
""",
        "choices": [
            "V\nK",
            "V",
            "K\nV",
            "エラーで終了する"
        ],
        "answer": 1,
        "explanation": "最初のexceptでVを出力し、その中でKeyErrorを捕捉してK。"
    },
    {
        "question": """問7
次のコードの出力として正しいものはどれか。

def test():
    try:
        print("1")
        raise ValueError
    except ValueError:
        print("2")
        raise Exception

try:
    test()
except Exception:
    print("3")
""",
        "choices": [
            "1\n2",
            "1\n3",
            "1\n2\n3",
            "エラーで終了する"
        ],
        "answer": 3,
        "explanation": "test内でValueErrorを捕捉→2出力→Exception送出→外側exceptで3。"
    },
    {
        "question": """問8
次のコードの出力として正しいものはどれか。

def inner():
    try:
        print("In")
        raise ValueError
    except ValueError:
        print("Val")
        raise Exception

def outer():
    try:
        print("Out")
        inner()
    except Exception:
        print("Ex")

outer()
""",
        "choices": [
            "Out\nIn\nVal\nEx",
            "Out\nIn\nEx",
            "In\nVal\nEx",
            "エラーで終了する"
        ],
        "answer": 1,
        "explanation": "outer開始でOut、inner開始でIn、ValueError捕捉でVal、Exception再送出→outerのexceptでEx。"
    },
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python CBTクイズ（中級・例外処理編）")
        self.q_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", justify="left", wraplength=600, anchor="w")
        self.question_label.pack(pady=10)

        self.choice_buttons = []
        for i in range(4):  # 今回は4択
            btn = tk.Button(root, text="", width=80, anchor="w", command=lambda idx=i: self.check_answer(idx+1))
            btn.pack(pady=2)
            self.choice_buttons.append(btn)

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
