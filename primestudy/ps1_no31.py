class OurException(Exception):
    pass

def raise_her_exception(a):
    print(a, "is a")
    raise OurException
    print("easygoing person")

def func(key:int):
    # int:はアノテーション
    try:
        if key ==0:
            raise_her_exception('Saya')
    except OurException as e:
        print("intelligent")
        raise Exception

key = 0
try:
    func(key)
except Exception as f:
    # 例外Exceptionが起こったら以下のprintが出力される
    print("speedstar")