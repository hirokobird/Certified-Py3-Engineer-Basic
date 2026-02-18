# 自作クラスの例
class Dog:
    def __init__(self, name, age):
        self.name = name  # プロパティ（値）
        self.age = age    # プロパティ（値）
    
    def bark(self):       # メソッド（関数）
        return f"{self.name}: ワン！"
    
    def get_age(self):    # メソッド（関数）
        return self.age

my_dog = Dog("ポチ", 3)

# プロパティ：値を直接参照
print(my_dog.name)  # "ポチ" ← ()不要
print(my_dog.age)   # 3 ← ()不要

# メソッド：関数を実行
print(my_dog.bark())     # "ポチ: ワン！" ← ()必要
print(my_dog.get_age())  # 3 ← ()必要