from random import randint
print("[0]剪刀、[1]石頭、[2]布")
me = input("剪刀石頭...")
com = randint(0,2)
L = ["剪刀","石頭","布"]
win = "恭喜，你贏了!!"
while int(me)==int(com):
     print("你出的拳是" , L[int(me)] , "，電腦出的拳是" , L[int(com)])
     print("平手，再來一次!!")
     me = input("剪刀石頭...")
     com = randint(0 , 2)
if int(me)==2 and int(com)==1: 
    print("你出的拳是" , L[int(me)] , "，電腦出的拳是" , L[int(com)])
    print(win)
elif int(me)==1 and int(com)==0:
    print("你出的拳是" , L[int(me)] , "，電腦出的拳是" , L[int(com)])
    print(win)
elif int(me)==0 and int(com)==2:
    print("你出的拳是" , L[int(me)] , "，電腦出的拳是" , L[int(com)])
    print(win)
else:
    print("你出的拳是" , L[int(me)] , "，電腦出的拳是" , L[int(com)])
    print("遺憾，你輸了...")
input()