# 自@property デコレータ：メソッドをプロパティのように見せることもできる
class Dog:
    def __init__(self, birth_year):
        self.birth_year = birth_year
    
    @property  # これを付けると、メソッドがプロパティのように使える
    def age(self):
        current_year = 2026
        return current_year - self.birth_year

my_dog = Dog(2020)
print(my_dog.age)  # 6 ← ()不要！（でも実は内部で関数が実行されている）