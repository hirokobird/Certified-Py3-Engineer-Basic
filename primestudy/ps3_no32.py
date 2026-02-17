
# No.32 

# グローバル空間
loc = "1"  # ← do_global()で"5"に変更される

def scope():
    # scope関数の空間
    loc = "2"  # ← do_nonlocal()で"4"に変更される
    
    def do_local():
        # do_local関数の空間（独立）
        loc = "3"  # ← ここだけの変数、終了後に消える
    
    def do_nonlocal():
        nonlocal loc  # 上の階層（scope）のlocを指す
        loc = "4"
    
    def do_global():
        global loc  # 一番外（グローバル）のlocを指す
        loc = "5"
    
    do_local()
    print("[A]", loc)
    do_nonlocal()
    print("[B]", loc)
    do_global()
    print("[C]", loc)

print("[D]", loc)
scope()
print("[E]", loc)