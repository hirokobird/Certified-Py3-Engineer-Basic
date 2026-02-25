"""
ユーザー定義の例外を送出
"""

class MyException(Exception):
    '''ユーザー定義例外'''
    pass

def raise_my_exception():
    raise MyException

def func(sw):
    try:
        if sw == 0:
            raise_my_exception()
    except MyException as e:
        print("ユーザー定義例外を捕捉")
        # ユーザー定義例外への対処を試みる
        # 回復不能と判断
        print("回復できませんでした。")
        raise Exception

sw = int(input("sw: "))
try:
    func(sw)
except Exception as e:
    print("例外捕捉！")
    print(type(e))