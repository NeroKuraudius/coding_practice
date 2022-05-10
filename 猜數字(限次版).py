N=33
G=None
GC=0
GL=3
OOL=False
while N!=G and not(OOL):
    GC+=1
    if GC<=GL:
        G=int(input("請輸入數字: "))
        if G>33:
            print("往下")
        elif G<33:
            print("往上")
    else:        
        OOL=True
if OOL:
    print("真可惜,你沒猜中...")
else:
    print("恭喜你猜中了!")