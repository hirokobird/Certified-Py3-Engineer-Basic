# クラスに関する練習問題（解答・解説）

# --------------------------------------------------------------------------------
# 問1. クラスの定義とインスタンス化として正しいものを選択してください。（1つ選択）
class MyClass:
    def __init__(self, value):
        self.value = value


'''
MyClassをインスタンス化する正しい記述はどれか
A. obj = MyClass(10)
B. obj = new MyClass(10)
C. obj = MyClass.create(10)
D. obj = MyClass.init(10)

正解: A 
解説: Pythonにおいてクラスをインスタンス化する際は、クラス名の後に丸括弧を付け、必要な引数を渡します。
選択肢Aがこの形式に合致しています。new は Java や C++ などの言語で使うキーワードですが、Pythonでは使いません。
'''

# --------------------------------------------------------------------------------
'''
問2. __init__メソッドに関する記述として誤っているものを選択してください。（1つ選択）

A. __init__メソッドは、クラスのインスタンスが生成される際に自動的に呼び出される特別なメソッドである。
B. __init__メソッドは、インスタンスの初期化を行うために使用される。
C. __init__メソッドの第一引数は慣習的にselfと名付けられ、生成されたインスタンス自身を指す。 
D. __init__メソッドは、必ず値をreturnする必要がある。

正解: D 
解説: __init__メソッドは、インスタンスの初期化を行うための特殊なメソッドであり、値をreturnする必要はありません。
通常、初期化処理のみを行い、Noneを暗黙的に返し、returnを書かないのが普通です。
'''
# --------------------------------------------------------------------------------
# 問3. 次のコードを実行した結果として正しいものを選択してください。（1つ選択）

class MyClass:
    class_var = 0  # クラス変数

    def __init__(self, instance_value):
        self.instance_var = instance_value
        MyClass.class_var += 1

obj1 = MyClass(10)
obj2 = MyClass(20)

print("obj1.class_var =", obj1.class_var)
print("obj2.class_var =", obj2.class_var)
print("obj1.instance_var =", obj1.instance_var)
print("obj2.instance_var =", obj2.instance_var)

'''
A. 
obj1.class_var = 1
obj2.class_var = 1
obj1.instance_var = 10
obj2.instance_var = 20

B. 
obj1.class_var = 2
obj2.class_var = 2
obj1.instance_var = 10
obj2.instance_var = 20

C. 
obj1.class_var = 0
obj2.class_var = 0
obj1.instance_var = 10
obj2.instance_var = 20

D. 
obj1.class_var = 2
obj2.class_var = 10
obj1.instance_var = 20
obj2.instance_var = 20

正解: B 
解説: class_varはクラス変数であり、すべてのインスタンスで共有されます。
インスタンスが生成されるたびにMyClass.class_varがインクリメントされるため、obj1とobj2のどちらからアクセスしても同じ値（2）になります。
一方、instance_varはインスタンス変数であり、各インスタンスに固有の値を持ちます。
'''
# --------------------------------------------------------------------------------
# 問4. メソッド内でのselfを使った別のメソッドの呼び出しとして正しいものを選択してください。（1つ選択）

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"

    def introduce(self):
        # ここに`bark`メソッドを呼び出すコードを記述
        pass

dog = Dog("Buddy")
print(dog.introduce())

'''
期待する結果がBuddy says Woof!となるように、introduceメソッド内の空欄に適切な記述はどれか。

A. return bark() 
B. return self.bark() 
C. return Dog.bark() 
D. return self.bark

正解: B 
解説: クラスのメソッド内で同じクラスの別のメソッドを呼び出す場合、self.メソッド名()という形式で呼び出します。
selfは現在のインスタンスを指し、そのインスタンスに紐づくメソッドを実行します。
'''
# --------------------------------------------------------------------------------
'''
問5. クラスの継承に関する記述として誤っているものを選択してください。（1つ選択）

A. 継承元となるクラスを「基底クラス」または「親クラス」と呼び、継承先のクラスを「派生クラス」または「子クラス」と呼ぶ。 
B. 派生クラスは、基底クラスの属性（変数やメソッド）を自動的に受け継ぐ。 
C. Pythonでクラスを継承する際は、class ChildClass(ParentClass):のように記述する。 
D. 派生クラスで__init__メソッドを定義する場合、基底クラスの__init__メソッドは自動的に呼び出されるため、明示的に呼び出す必要はない。

正解: D 
解説: 派生クラスで__init__メソッドを定義する場合、基底クラスの__init__メソッドは自動的には呼び出されません。
基底クラスの初期化処理を実行したい場合は、super().__init__(引数)やParentClass.__init__(self, 引数)のように明示的に呼び出す必要があります。
'''
# --------------------------------------------------------------------------------
# 問6. メソッドのオーバーライドとして正しい記述はどれか。（1つ選択）

class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        # ここにDogクラス独自の鳴き声の処理を記述
        pass

dog = Dog()
print(dog.speak())

'''
期待する結果がDog barksとなるように、Dogクラスのspeakメソッド内の空欄に適切な記述はどれか。

A. return "Dog barks" 
B. return super().speak() 
C. return Animal.speak(self) 
D. return self.speak()

正解: A 
解説: メソッドのオーバーライドとは、親クラスと同じ名前のメソッドを子クラスで新たに定義し、その動作を変更することです。
Dogクラスのspeakメソッドで「Dog barks」という文字列を返すことで、親クラスのspeakメソッドを上書きし、Dogクラス独自の振る舞いを実現できます。
選択肢BとCは親クラスのメソッドを呼び出す方法ですが、ここでは子クラス独自の動作をさせたいので適切ではありません。
選択肢Dは同じメソッドを再帰的に呼ぶため、無限ループとなりエラーを引き起こします。
'''
# --------------------------------------------------------------------------------
'''
問7. あるオブジェクトが特定のクラスのインスタンスであるかを確認する関数として正しいものを選択してください。（1つ選択）
A. typeof() 
B. isinstance() 
C. is_type() 
D. check_instance()

正解: B 
解説: Pythonでは、あるオブジェクトが特定のクラスのインスタンスであるかを判定するために、組み込み関数のisinstance(オブジェクト, クラス)を使用します。
選択肢Aのtypeof は JavaScriptの関数で、選択肢Cのis_type はPythonには存在しない架空の関数です。
'''
# --------------------------------------------------------------------------------
# 問8. 次のコードを実行した結果として正しいものを選択してください。（1つ選択）

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine_status = "off"

    def start_engine(self):
        self.engine_status = "on"
        print(f"{self.brand} engine is {self.engine_status}.")

    def drive(self):
        if self.engine_status == "on":
            print(f"{self.brand} is driving.")
        else:
            print(f"{self.brand} cannot drive, engine is {self.engine_status}.")

my_car = Car("Toyota")
my_car.drive()
my_car.start_engine()
my_car.drive()

'''
A. 
Toyota cannot drive, engine is off. 
Toyota engine is on. 
Toyota is driving. 

B. 
Toyota engine is on. 
Toyota is driving. 

C. 
Toyota cannot drive, engine is off. 
Toyota is driving. 

D. 
Toyota is driving. 
Toyota engine is on. 
Toyota cannot drive, engine is off.

正解: A 
解説: 最初のmy_car.drive()の呼び出し時点ではengine_statusは"off"なので、「Toyota cannot drive, engine is off.」と表示されます。
次にmy_car.start_engine()が呼び出され、engine_statusが"on"になり、「Toyota engine is on.」と表示されます。
最後のmy_car.drive()の呼び出しではengine_statusが"on"になっているため、「Toyota is driving.」と表示されます。
'''
