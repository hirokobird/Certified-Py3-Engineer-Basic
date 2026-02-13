class Student:
    # 初期化メソッド（イニシャライザ）
    def __init__(self, name, classname, jp, math, eng):
        self.name = name # インスタンス変数
        self.classname = classname
        self.jp = int(jp)     # 計算用に整数化
        self.math = int(math)
        self.eng = int(eng)
   
    # 1. 合計点を計算するメソッド
    def calc_total(self):
        return self.jp + self.math + self.eng

    # 2. 平均点を計算するメソッド
    def calc_average(self):
        return round(self.calc_total() / 3, 1) # 小数第1位まで
   
    # 3. 結果を出力するメソッド
    def result(self):
        print(f"【{self.classname}】{self.name}さん のテスト結果：合計点 {self.calc_total()} / 平均点 {self.calc_average()}です")


student_a = Student("A山T太", "普通科", 55, 65, 70) # インスタンス化
student_b = Student("B川C美", "普通科", 85, 95, 80) # インスタンス化
student_a.result() # result()メソッドを実行