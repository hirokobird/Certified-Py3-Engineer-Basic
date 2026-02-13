'''
ステップ1:クラスの定義とインスタンスの作成

問題1: ペットの名前と年齢を設定しよう

Petクラスを作り、__init__メソッドでnameとage属性を初期化してください。
インスタンスを1つ作り、名前と年齢を表示するコードを書いてみましょう。

出力例:
ペットの名前はTaro、2歳です

'''

# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age   

# mypet = Pet("太郎", "5")
# print(f"ペットの名前は{mypet.name}、{mypet.age}歳です")

   
# --------------------------------------------------------------------
'''
問題2: 好きな食べ物のクラスを作ろう

Foodクラスを作り、__init__メソッドでname（食べ物の名前）とcolor（色）を初期化してください。
インスタンスを1つ作り、食べ物の名前と色を表示しましょう。


出力例:
私の好きな食べ物はりんごで、色は赤です

'''
# class Food:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     def my_favorit(self):
#         print(f"私の好きな食べ物は{self.name}で、色は{self.color}です")

# myfruits = Food("りんご", "赤")
# myfruits.my_favorit()


# --------------------------------------------------------------------
'''
問題3:キャラクターのクラスを作ろう


Characterクラスを作り、__init__メソッドでnameとpower（強さ）を初期化してください。
勇者と魔法使いのインスタンスを2つ作り、それぞれの名前とレベルを表示しましょう。

出力例:
勇者のレベルは100です
魔法使いのレベルは80です

'''

# class Character:
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def introduce(self):
#         print(f'{self.name}のレベルは{self.power}です')

# player1 = Character("勇者", 100)
# player2 = Character("魔法使い", 80)
# player1.introduce()
# player2.introduce()
# print(f'{player1.name}のレベルは{player1.power}です')
# print(f'{player2.name}のレベルは{player2.power}です')


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

# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def bark(self):
#         print(f"{self.name}がワンワン！")

# mydog = Dog("ポチ", 3)
# print(f"犬の名前は{mydog.name}、{mydog.age}歳だよ！")
# mydog.bark()


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

# class Cat:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
    
#     def meow(self):
#         print(f"{self.color}の{self.name}がニャー！")

# mycat = Cat("タマ", "白")
# print(f"猫の名前は{mycat.name}、色は{mycat.color}だよ！")
# mycat.meow()        


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
# class Hero:
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
    
#     def attack(self):
#         print(f"ヒーローの名前は{self.name}、攻撃力は{self.power}だよ！")
#         print(f"{self.name}が{self.power}の力で攻撃した")

# chara = Hero("勇者", 50)
# chara.attack()


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
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def bark(self, bark):
#         self.bark = bark
#         print(f"{self.name}が{self.bark}！")
    
#     def have_birthday(self):
#         self.age +=1
#         print(f"{self.name}の誕生日！{self.age}歳になったよ！")

# mydog = Dog("ポチ", 3)
# print(f"犬の名前は{mydog.name}、{mydog.age}歳だよ！")
# mydog.bark("ワンワン")
# mydog.have_birthday() 


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

# class Cat:
#     def __init__(self, name, energy):
#         self.name = name
#         self.energy = energy

#     def intro(self):
#         print(f"猫の名前は{self.name}、元気さは{self.energy}だよ！")
    
#     def meow(self, meomeo):
#         self.meomeo = meomeo
#         print(f"{self.name}が{self.meomeo}！")
    
#     def play(self):
#         self.energy -= 10
#         print(f"{self.name}が遊んだ！元気さが{self.energy}になったよ！")

# mycat = Cat("タマ", 80)
# mycat.intro
# mycat.meow("にゃー")
# mycat.play()
# mycat.play()
# mycat.play()


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
#     def bark(self, bow):
#         #super().__init__(name)
#         self.bow = bow
#         print(f"{self.name}が{self.bow}！")

# mydog = Dog("ポチ")
# mydog.eat()
# mydog.bark("ワンワン")


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
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
      
#     def move(self, mvsound):
#         self.mvsound = mvsound
#         print(f"{self.brand}が{self.mvsound}走ってるよ！")

# class Car(Vehicle):
#     def __init__(self, brand):
#         super().__init__(brand)

#     def honk(self, crsound):
#         self.crsound = crsound
#         print(f"{self.brand}が{self.crsound}!")


# mycar = Car("トヨタ")
# mycar2 = Vehicle("スバル")
# print(f"車のブランドは{mycar.brand}だよ！")
# print(f"車のブランドは{mycar2.brand}だよ！")
# print(f"車のブランドは{mycar.brand}だよ！")
# mycar.move("スイスイ")
# mycar.honk("プップー")

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
# class Character:
#     def __init__(self, name):
#         self.name = name
    
#     def attack(self):
#         print(f"{self.name}が攻撃したよ！")

# class Wizard(Character):
#     def cast_spell(self, spelling):
#         self.spelling = spelling
#         print(f"{self.name}が魔法を唱えた！{self.spelling}！")

# mychara = Wizard("魔法使い")
# print(f"キャラの名前は{mychara.name}だよ！")
# mychara.attack()
# mychara.cast_spell("キラキラ")

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
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         print(f"{self.name}が何か鳴いてるよ！")

# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name}がワンワン！")

# mydog = Dog("ポチ")
# print(f"名前は{mydog.name}だよ！")
# mydog.speak()  


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

# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
    
#     def move(self):
#         print(f"{self.brand}が移動するよ")

# class Car(Vehicle):
#     def move(self, carsound):
#         self.carsound = carsound
#         print(f"{self.brand}が{self.carsound}と走ってるよ！")

# mycar = Car("トヨタ")
# print(f"車のブランドは{mycar.brand}だよ！")
# mycar.move("ブーン")
# mycar2 = Vehicle("日産")
# mycar2.move()
        


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
# class Character:
#     def __init__(self, name):
#         self.name = name
    
#     def attack(self):
#         print(f"{self.name}は攻撃を仕掛けた")

# class Wizard(Character):
#     def attack(self, amethod, asound):
#         self.asound = asound
#         self.amethod = amethod
#         print(f"{self.name}が{self.amethod}で攻撃！{self.asound}！")

# mychara = Wizard("魔法使い")
# print(f"キャラの名前は{mychara.name}だよ！")
# mychara.attack("魔法", "バチーン")
# mychara2 = Character("剣士")
# mychara2.attack()

# print("-----------------")


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
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def eat(self):
#         print(f"{self.name}がご飯を食べてるよ！")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

#     def bark(self, bbark):
#         self.bbark = bbark
#         print(f"{self.breed}の{self.name}が{self.bbark}！")

# mydog = Dog("ポチ","柴犬")
# print(f"名前は{mydog.name}、犬種は{mydog.breed}だよ！")
# mydog.eat()
# mydog.bark("ワンワン")

# print("-----------------")

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
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

#     def move(self):
#         print(f"{self.brand}が移動してるよ！")

# class Car(Vehicle):
#     def __init__(self, brand, speed):
#         super().__init__(brand)
#         self.speed = speed

#     def move(self, msound):
#        super().move()
#        self.msound = msound
#        print(f"{self.brand}が{self.speed}km/hで{self.msound}と走ってるよ！")

# mycar = Car("トヨタ", 180)
# print(f"車のブランドは{mycar.brand}、最高速度は{mycar.speed}km/hだよ！")
# mycar.move("ブーン")

# print("-----------------")
# # --------------------------------------------------------------------
# '''
# 問題3: キャラクターと魔法使いのクラスにsuper()を活用

# 問題:
# Characterクラスを作り、__init__でname属性を初期化し、attackメソッドで汎用的な「攻撃する」メッセージを出力してください。
# Characterを継承したWizardクラスを作り、__init__でsuper()を使って親のnameを初期化し、追加でmagic（魔法力）属性を初期化します。
# さらに、attackメソッドをオーバーライドして、super()で親のattackを呼び出し、魔法力を使った攻撃メッセージを追加します。
# Wizardのインスタンスを1つ作り、名前、魔法力を表示し、attackを呼び出してください。

# 出力例:
# キャラの名前は魔法使い、魔法力は50だよ！
# 魔法使いが攻撃したよ！
# 魔法使いが50の魔法で攻撃！バチーン！

# '''
# class Character:
#     def __init__(self, name):
#         self.name = name
    
#     def attack(self):
#         print(f"{self.name}が攻撃したよ！")

# class Wizard(Character):
#     def __init__(self, name, magic):
#         super().__init__(name)
#         self.magic = magic

#     def attack(self, amethod, asound):
#         super().attack()
#         self.amethod = amethod
#         self.asound = asound
#         print(f"{self.name}が{self.magic}の{self.amethod}で攻撃！{self.asound}！")

# mychara = Wizard("魔法使い", 50)
# print(f"キャラの名前は{mychara.name}、魔法力は{mychara.magic}だよ！")
# mychara.attack("魔法", "バチーン")

print("-----------------")

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
# class Animal:
#     total_animals = 0
    
#     def __init__(self, name):
#         self.name = name
#         Animal.total_animals += 1
        
#     def intro(self):
#         print(f"私は{self.name}！動物園には{Animal.total_animals}匹の動物がいるよ！")

# ani1 = Animal("ライオン")
# ani2 = Animal("シマウマ")
# ani1.intro()
# ani2.intro()
# print(f"動物の総数は{Animal.total_animals}匹だよ！")



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
    total_products = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.total_products += 1
    
    def show_info(self):
        print(f"商品: {self.name}、価格: {self.price}円、お店に{Product.total_products}個あるよ！")

item1 = Product("りんご", 100)
item2 = Product("バナナ", 150)
item1.show_info()
item2.show_info()
print(f"お店の商品は全部で{Product.total_products}個だよ！")
    
print("-----------------")


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
    character_type = "戦士"

    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def show_status(self):
        print(f"{self.name}はレベル{self.level}の{Character.character_type}だよ！")

    def change_type(self, new_chara):
        Character.character_type = new_chara
        print(f"キャラの種類を{new_chara}に変えたよ！")

chara = Character("勇者", 10)
chara.show_status()
chara.change_type("魔法使い")
chara.show_status()