import random
P = set()
while len(P) < 7:
    n = random.randint(1,48)
    P.add(n)
print("本期開獎號碼為:", P)

atr = int(input("請輸入中獎幾碼:"))
t = 0
while True:
    L = set()
    while len(L) < 7:
        n = random.randint(1,48)
        L.add(n)
    t += 1
    N = 0
    for a in L:
        if a in P:
            N += 1
    if N >= atr:
        break
print("恭喜中頭獎!!你共買了", t , "張彩券")