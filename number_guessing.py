C = 22
G = None

while G!=C:
    G = int(input("請輸入猜測數字:"))
    if G>C:
        print("再小一點!")
    elif G<C:
        print("再大一點!")
    elif G==C:
        print("恭喜你猜中了~")

input()
        
