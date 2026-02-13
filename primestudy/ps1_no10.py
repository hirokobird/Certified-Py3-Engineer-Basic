print("==問題の式の形==")
# ※通常はこんなコード書かない。書いたら怒られる。

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
        continue # ここに continue なんて書かなくても、勝手に次のループに行く
    break 

print("==最後まで実行するなら下記の式==")

for n in range(2, 10):
    for x in range(2, n): 
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

print("==採用された式を表示すると下記の形==")

for n in range(2, 10):
    for x in range(2, n): 
        if n % x == 0:
            print(f"① {n} ÷ {x} = {n/x}")
            print("①", n, 'equals', x, '*', n//x)
            break
    else:
        print(f"② {n} ÷ {x} = {n/x}")
        print("②", n, 'is a prime number')

"""
1つめのbreakについて、n=4でif節が4%2==0でTrueとなりprint文が実行された場合、続く4%3を検証する前にストップするためのbreak？

2つめのbreakはfor x 節にかかっているけど、これは1つ目のbreakが評価された後に2つ目のbreakに飛ぶからループがストップするの？
"""
"""
1. 1つ目の break について

・n=4, x=2 のとき、割り切れるので True になります。
・print が実行された直後、break が発動します。
・この瞬間、内側の x のループは即座に終了するため、x=3（4%3）の検証は行われません。

解説: これは「最小の約数」が見つかった時点で「あ、こいつは素数じゃない（合成数だ）」と確定するからです。無駄な計算を省くためにここでストップさせています。

2. 2つ目の break への流れについて
ここが一番面白いところです。「1つ目のbreakから直接飛んでくる」という感覚でほぼ合っていますが、正確な**「通るルート」**はこうなります。

処理の流れ（n=4 の場合）

1. 内側ループ: x=2 で break （1つ目）が発動。

👉 「内側の for ループ」から脱出します。

2.運命の分岐点（else 節）:

　・Pythonはここで考えます。「内側のループは最後まで完走したかな？ それとも中断（break）されたかな？」

　・今回: 「中断された」 ので、else: ブロック（素数です表示 & continue）はスキップ（無視）されます。

3. 転落（Fall through）:

　・else ブロックが無視されたので、プログラムはそのまま下へ落ちていきます。

4. 2つ目の break に到達:

　・else の壁に守られていない場所に break が置いてあるので、これに衝突します。

　・👉 「外側の n のループ」からも脱出し、プログラム全体が終了します。

整理すると
・素数だった場合 (n=3): 内側ループ完走 → else ブロック実行 → continue で次の n へジャンプ（下の break には届かない）。

・素数じゃなかった場合 (n=4): 内側ループ break → else ブロックをスキップ → そのまま下に落ちて 2つ目の break を踏む。

この「else をスキップして下に落ちる」という挙動こそが、2つ目の break が実行されてしまう原因です。
"""
