'''
ステップ1:クラスの定義とインスタンスの作成

問題1: ペットの名前と年齢を設定しよう

Petクラスを作り、__init__メソッドでnameとage属性を初期化してください。
インスタンスを1つ作り、名前と年齢を表示するコードを書いてみましょう。

出力例:
ペットの名前はTaro、2歳です

'''

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_pet = Pet("Taro", 2)
print(f"ペットの名前は{my_pet.name}、{my_pet.age}歳です")

# --------------------------------------------------------------------
'''
問題2: 好きな食べ物のクラスを作ろう

Foodクラスを作り、__init__メソッドでname（食べ物の名前）とcolor（色）を初期化してください。
インスタンスを1つ作り、食べ物の名前と色を表示しましょう。


出力例:
私の好きな食べ物はりんごで、色は赤です

'''
class Food:
    def __init__(self, name, color):
        self.name = name
        self.color = color

my_food = Food("りんご", "赤")
print(f"私の好きな食べ物は{my_food.name}で、色は{my_food.color}です")

# --------------------------------------------------------------------
'''
問題3:キャラクターのクラスを作ろう


Characterクラスを作り、__init__メソッドでnameとpower（強さ）を初期化してください。
勇者と魔法使いのインスタンスを2つ作り、それぞれの名前とレベルを表示しましょう。

出力例:
勇者のレベルは100です
魔法使いのレベルは80です

'''
class Character:
    def __init__(self, name, power):
        self.name = name
        self.power = power

hero1 = Character("勇者", 100)
hero2 = Character("魔法使い", 80)
print(f"{hero1.name}のレベルは{hero1.power}です")
print(f"{hero2.name}のレベルは{hero2.power}です")

# --------------------------------------------------------------------
'''
ステップ2: メソッドの追加の練習問題

問題1:問題1: 犬が吠えるクラスを作ろう

Dogクラスを作り、__init__メソッドでnameとage属性を初期化してください。
さらに、barkメソッドを追加して、犬の名前を使った吠え声を出力しましょう。
インスタンスを1つ作り、名前と年齢を表示した後、barkメソッドを呼び出してください。

出力例:
犬の名前はポチ、3歳だよ！
ポチがワンワン！

'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name}がワンワン！")

my_dog = Dog("ポチ", 3)
print(f"犬の名前は{my_dog.name}、{my_dog.age}歳だよ！")
my_dog.bark()

# --------------------------------------------------------------------
'''
問題2: 猫が鳴くクラスを作ろう

Catクラスを作り、__init__メソッドでnameとcolor属性を初期化してください。
さらに、meowメソッドを追加して、猫の名前と色を使った鳴き声を出力しましょう。
インスタンスを1つ作り、名前と色を表示した後、meowメソッドを呼び出してください。

出力例:
猫の名前はタマ、色は白だよ！
白のタマがニャー！

'''
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def meow(self):
        print(f"{self.color}の{self.name}がニャー！")

my_cat = Cat("タマ", "白")
print(f"猫の名前は{my_cat.name}、色は{my_cat.color}だよ！")
my_cat.meow()

# --------------------------------------------------------------------
'''
問題3: ゲームキャラクターの攻撃クラスを作ろう

Heroクラスを作り、__init__メソッドでnameとpower（攻撃力）を初期化してください。
さらに、attackメソッドを追加して、キャラクターの名前と攻撃力を使った攻撃メッセージを出力しましょう。
インスタンスを1つ作り、名前と攻撃力を表示した後、attackメソッドを呼び出してください。

出力例:
ヒーローの名前は勇者、攻撃力は50だよ！
勇者が50の力で攻撃した！

'''
class Hero:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f"{self.name}が{self.power}の力で攻撃した！")

my_hero = Hero("勇者", 50)
print(f"ヒーローの名前は{my_hero.name}、攻撃力は{my_hero.power}だよ！")
my_hero.attack()

# --------------------------------------------------------------------
'''
ステップ3:複数のメソッドと属性の操作の練習問題

問題1: 犬の誕生日を祝うクラス

Dogクラスを作り、__init__メソッドでnameとage属性を初期化してください。以下の2つのメソッドを追加します：
    →bark: 犬の名前を使って吠え声を出力。
    →have_birthday: 犬の年齢を1増やし、誕生日メッセージを出力。
インスタンスを1つ作り、名前と年齢を表示し、barkとhave_birthdayを呼び出してください。

出力例:
犬の名前はポチ、3歳だよ！
ポチがワンワン！
ポチの誕生日！4歳になったよ！

'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name}がワンワン！")
    
    def have_birthday(self):
        self.age += 1
        print(f"{self.name}の誕生日！{self.age}歳になったよ！")

my_dog = Dog("ポチ", 3)
print(f"犬の名前は{my_dog.name}、{my_dog.age}歳だよ！")
my_dog.bark()
my_dog.have_birthday()

# --------------------------------------------------------------------
'''
問題2: 猫が遊ぶクラス

Catクラスを作り、__init__メソッドでnameとenergy（元気さ、0～100の数値）を初期化してください。以下の2つのメソッドを追加します：
    →meow: 猫の名前を使って鳴き声を出力。
    →play: 元気さを10減らし、遊んだメッセージを出力。
インスタンスを1つ作り、名前と元気さを表示し、meowとplayを呼び出してください。

出力例:
猫の名前はタマ、元気さは80だよ！
タマがニャー！
タマが遊んだ！元気さが70になったよ！

'''
class Cat:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
    
    def meow(self):
        print(f"{self.name}がニャー！")
    
    def play(self):
        self.energy -= 10
        print(f"{self.name}が遊んだ！元気さが{self.energy}になったよ！")

my_cat = Cat("タマ", 80)
print(f"猫の名前は{my_cat.name}、元気さは{my_cat.energy}だよ！")
my_cat.meow()
my_cat.play()

# --------------------------------------------------------------------
'''
問題3: ゲームキャラクターのレベルアップ

Heroクラスを作り、__init__メソッドでnameとlevel属性を初期化してください。以下の2つのメソッドを追加します：
    →attack: 名前とレベルを使って攻撃メッセージを出力。
    →level_up: レベルを1増やし、レベルアップメッセージを出力。
インスタンスを1つ作り、名前とレベルを表示し、attackとlevel_upを呼び出してください。

出力例:

ヒーローの名前は勇者、レベルは5だよ！
勇者がレベル5の力で攻撃！
勇者がレベルアップ！レベル6になったよ！
'''
class Hero:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def attack(self):
        print(f"{self.name}がレベル{self.level}の力で攻撃！")
    
    def level_up(self):
        self.level += 1
        print(f"{self.name}がレベルアップ！レベル{self.level}になったよ！")

my_hero = Hero("勇者", 5)
print(f"ヒーローの名前は{my_hero.name}、レベルは{my_hero.level}だよ！")
my_hero.attack()
my_hero.level_up()


# --------------------------------------------------------------------
'''
ステップ4:簡単な継承の練習問題

問題1: 動物と犬のクラス

Animalクラスを作り、__init__でname属性を初期化し、eatメソッドで「食べる」メッセージを出力してください。
Animalを継承したDogクラスを作り、barkメソッドを追加して犬の名前を使った吠え声を出力します。
Dogのインスタンスを1つ作り、名前を表示し、eatとbarkを呼び出してください。

出力例:
名前はポチだよ！
ポチがご飯を食べてるよ！
ポチがワンワン！
'''
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def eat(self):
#         print(f"{self.name}がご飯を食べてるよ！")

# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name}がワンワン！")

# my_dog = Dog("ポチ")
# print(f"名前は{my_dog.name}だよ！")
# my_dog.eat()
# my_dog.bark()

# --------------------------------------------------------------------
'''
問題2: 乗り物と車のクラス

問題:
Vehicleクラスを作り、__init__でbrand属性を初期化し、moveメソッドで「移動する」メッセージを出力してください。
Vehicleを継承したCarクラスを作り、honkメソッドを追加してブランド名を使ったクラクション音を出力します。
Carのインスタンスを1つ作り、ブランドを表示し、moveとhonkを呼び出してください。

出力例:
車のブランドはトヨタだよ！
トヨタがスイスイ走ってるよ！
トヨタがプップー！

'''
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def move(self):
        print(f"{self.brand}がスイスイ走ってるよ！")

class Car(Vehicle):
    def honk(self):
        print(f"{self.brand}がプップー！")

my_car = Car("トヨタ")
print(f"車のブランドは{my_car.brand}だよ！")
my_car.move()
my_car.honk()

# --------------------------------------------------------------------
'''
問題3: キャラクターと魔法使いのクラス

問題:
Characterクラスを作り、__init__でname属性を初期化し、attackメソッドで「攻撃する」メッセージを出力してください。
Characterを継承したWizardクラスを作り、cast_spellメソッドを追加して名前を使った魔法のメッセージを出力します。
Wizardのインスタンスを1つ作り、名前を表示し、attackとcast_spellを呼び出してください。

出力例:
キャラの名前は魔法使いだよ！
魔法使いが攻撃したよ！
魔法使いが魔法を唱えた！キラキラ！

'''
class Character:
    def __init__(self, name):
        self.name = name
    
    def attack(self):
        print(f"{self.name}が攻撃したよ！")

class Wizard(Character):
    def cast_spell(self):
        print(f"{self.name}が魔法を唱えた！キラキラ！")

my_wizard = Wizard("魔法使い")
print(f"キャラの名前は{my_wizard.name}だよ！")
my_wizard.attack()
my_wizard.cast_spell()

# --------------------------------------------------------------------
'''
ステップ5: メソッドのオーバーライドの練習問題

問題1: 動物と犬の鳴き声

問題:
Animalクラスを作り、__init__でname属性を初期化し、speakメソッドで汎用的な「鳴く」メッセージを出力してください。
Animalを継承したDogクラスを作り、speakメソッドをオーバーライドして犬の名前を使った吠え声を出力します。
Dogのインスタンスを1つ作り、名前を表示し、speakを呼び出してください。

出力例:
名前はポチだよ！
ポチがワンワン！

'''
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name}が何か鳴いてるよ！")

class Dog(Animal):
    def speak(self):
        print(f"{self.name}がワンワン！")

my_dog = Dog("ポチ")
print(f"名前は{my_dog.name}だよ！")
my_dog.speak()

# --------------------------------------------------------------------
'''
問題2: 乗り物と車の動作

問題:
Vehicleクラスを作り、__init__でbrand属性を初期化し、moveメソッドで汎用的な「移動する」メッセージを出力してください。
Vehicleを継承したCarクラスを作り、moveメソッドをオーバーライドしてブランド名を使った車の移動メッセージを出力します。
Carのインスタンスを1つ作り、ブランドを表示し、moveを呼び出してください。

出力例:
車のブランドはトヨタだよ！
トヨタがブーンと走ってるよ！

'''
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def move(self):
        print(f"{self.brand}が移動してるよ！")

class Car(Vehicle):
    def move(self):
        print(f"{self.brand}がブーンと走ってるよ！")

my_car = Car("トヨタ")
print(f"車のブランドは{my_car.brand}だよ！")
my_car.move()

# --------------------------------------------------------------------
'''
問題3: キャラクターと魔法使いの攻撃

問題:
Characterクラスを作り、__init__でname属性を初期化し、attackメソッドで汎用的な「攻撃する」メッセージを出力してください。
Characterを継承したWizardクラスを作り、attackメソッドをオーバーライドして名前を使った魔法の攻撃メッセージを出力します。
Wizardのインスタンスを1つ作り、名前を表示し、attackを呼び出してください。

出力例:
キャラの名前は魔法使いだよ！
魔法使いが魔法で攻撃！バチーン！

'''
class Character:
    def __init__(self, name):
        self.name = name
    
    def attack(self):
        print(f"{self.name}が攻撃したよ！")

class Wizard(Character):
    def attack(self):
        print(f"{self.name}が魔法で攻撃！バチーン！")

my_wizard = Wizard("魔法使い")
print(f"キャラの名前は{my_wizard.name}だよ！")
my_wizard.attack()

# --------------------------------------------------------------------
'''
ステップ6:super()を使った継承の練習問題

問題1: 動物と犬のクラスにsuper()を活用

Animalクラスを作り、__init__でname属性を初期化し、eatメソッドで「食べる」メッセージを出力してください。
Animalを継承したDogクラスを作り、__init__でsuper()を使って親のnameを初期化し、追加でbreed（犬種）属性を初期化します。
さらに、barkメソッドを追加して犬の名前と犬種を使った吠え声を出力します。
Dogのインスタンスを1つ作り、名前、犬種を表示し、eatとbarkを呼び出してください。

出力例:
名前はポチ、犬種は柴犬だよ！
ポチがご飯を食べてるよ！
柴犬のポチがワンワン！

'''
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name}がご飯を食べてるよ！")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 親の__init__を呼び出し
        self.breed = breed
    
    def bark(self):
        print(f"{self.breed}の{self.name}がワンワン！")

my_dog = Dog("ポチ", "柴犬")
print(f"名前は{my_dog.name}、犬種は{my_dog.breed}だよ！")
my_dog.eat()
my_dog.bark()

# --------------------------------------------------------------------
'''
問題2: 乗り物と車のクラスにsuper()を活用

Vehicleクラスを作り、__init__でbrand属性を初期化し、moveメソッドで「移動する」メッセージを出力してください。
Vehicleを継承したCarクラスを作り、__init__でsuper()を使って親のbrandを初期化し、追加でspeed（最高速度）属性を初期化します。
さらに、moveメソッドをオーバーライドして、super()で親のmoveを呼び出し、速度を使ったメッセージを追加します。
Carのインスタンスを1つ作り、ブランド、速度を表示し、moveを呼び出してください。

出力例:
車のブランドはトヨタ、最高速度は180km/hだよ！
トヨタが移動してるよ！
トヨタが180km/hでブーンと走ってるよ！

'''
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def move(self):
        print(f"{self.brand}が移動してるよ！")

class Car(Vehicle):
    def __init__(self, brand, speed):
        super().__init__(brand)  # 親の__init__を呼び出し
        self.speed = speed
    
    def move(self):
        super().move()  # 親のmoveを呼び出し
        print(f"{self.brand}が{self.speed}km/hでブーンと走ってるよ！")

my_car = Car("トヨタ", 180)
print(f"車のブランドは{my_car.brand}、最高速度は{my_car.speed}km/hだよ！")
my_car.move()

# --------------------------------------------------------------------
'''
問題3: キャラクターと魔法使いのクラスにsuper()を活用

問題:
Characterクラスを作り、__init__でname属性を初期化し、attackメソッドで汎用的な「攻撃する」メッセージを出力してください。
Characterを継承したWizardクラスを作り、__init__でsuper()を使って親のnameを初期化し、追加でmagic（魔法力）属性を初期化します。
さらに、attackメソッドをオーバーライドして、super()で親のattackを呼び出し、魔法力を使った攻撃メッセージを追加します。
Wizardのインスタンスを1つ作り、名前、魔法力を表示し、attackを呼び出してください。

出力例:
キャラの名前は魔法使い、魔法力は50だよ！
魔法使いが攻撃したよ！
魔法使いが50の魔法で攻撃！バチーン！

'''
class Character:
    def __init__(self, name):
        self.name = name
    
    def attack(self):
        print(f"{self.name}が攻撃したよ！")

class Wizard(Character):
    def __init__(self, name, magic):
        super().__init__(name)  # 親の__init__を呼び出し
        self.magic = magic
    
    def attack(self):
        super().attack()  # 親のattackを呼び出し
        print(f"{self.name}が{self.magic}の魔法で攻撃！バチーン！")

my_wizard = Wizard("魔法使い", 50)
print(f"キャラの名前は{my_wizard.name}、魔法力は{my_wizard.magic}だよ！")
my_wizard.attack()

# --------------------------------------------------------------------
'''
ステップ7:クラス変数の活用

問題1: 動物園の動物カウンター

問題:
Animalクラスを作り、クラス変数total_animalsで動物の総数を管理してください。
__init__でname属性を初期化し、インスタンス作成時にtotal_animalsを1増やします。
introduceメソッドを追加して、名前と総数を使った自己紹介メッセージを出力します。
Animalのインスタンスを2つ作り、それぞれでintroduceを呼び出し、最後にtotal_animalsを表示してください。

出力例:
私はライオン！動物園には2匹の動物がいるよ！
私はシマウマ！動物園には2匹の動物がいるよ！
動物の総数は2匹だよ！
'''

class Animal:
    total_animals = 0  # クラス変数
    
    def __init__(self, name):
        self.name = name
        Animal.total_animals += 1
    
    def introduce(self):
        print(f"私は{self.name}！動物園には{Animal.total_animals}匹の動物がいるよ！")

lion = Animal("ライオン")
zebra = Animal("シマウマ")
lion.introduce()
zebra.introduce()
print(f"動物の総数は{Animal.total_animals}匹だよ！")

# --------------------------------------------------------------------
'''
問題2: お店の商品カウンター

問題:
Productクラスを作り、クラス変数total_productsで商品の総数を管理してください。
__init__でnameとprice属性を初期化し、インスタンス作成時にtotal_productsを1増やします。
show_infoメソッドを追加して、商品の名前、価格、総数を出力します。
Productのインスタンスを2つ作り、それぞれでshow_infoを呼び出し、最後にtotal_productsを表示してください。

出力例:
商品: りんご、価格: 100円、お店に2個あるよ！
商品: バナナ、価格: 150円、お店に2個あるよ！
お店の商品は全部で2個個だよ！

'''
class Product:
    total_products = 0  # クラス変数
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.total_products += 1
    
    def show_info(self):
        print(f"商品: {self.name}、価格: {self.price}円、お店に{Product.total_products}個あるよ！")

apple = Product("りんご", 100)
banana = Product("バナナ", 150)
apple.show_info()
banana.show_info()
print(f"お店の商品は全部で{Product.total_products}個だよ！")

# --------------------------------------------------------------------
'''
問題3: ゲームキャラクターの種別管理

問題:
Characterクラスを作り、クラス変数character_typeでキャラクターの種類（例: "戦士"）を管理してください。
__init__でnameとlevel属性を初期化します。
show_statusメソッドを追加して、名前、レベル、キャラクターの種類を出力します。
さらに、change_typeメソッドを追加してcharacter_typeを変更可能にします。
Characterのインスタンスを1つ作り、show_statusを呼び出し、change_typeで種類を変更後、再度show_statusを呼び出してください。

出力例:
勇者はレベル10の戦士だよ！
キャラの種類を魔法使いに変えたよ！
勇者はレベル10の魔法使いだよ！
'''
class Character:
    character_type = "戦士"  # クラス変数
    
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def show_status(self):
        print(f"{self.name}はレベル{self.level}の{Character.character_type}だよ！")
    
    def change_type(self, new_type):
        Character.character_type = new_type
        print(f"キャラの種類を{new_type}に変えたよ！")

hero = Character("勇者", 10)
hero.show_status()
hero.change_type("魔法使い")
hero.show_status()