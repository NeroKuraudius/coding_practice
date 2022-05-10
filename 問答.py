questions = ["1.茸茸最愛誰?\nA.小丸子\nB.布布\nC.雞丁\n","2.誰身上的毛最多?\nA.泡泡\nB.布布\nC.汪汪\n","3.跟我們出去嘉義玩的是誰?\nA.波波\nB.花花\nC.布布\n"]
from First_try import test

start=[test(questions[0],"C"),test(questions[1],"A"),test(questions[2],"B")]

def exam(start):
    score = 0
    for First_try in start:
        answer = input(First_try.D)
        if answer == First_try.A:
            score +=1
    print("恭喜你，三題中你答對了" + str(score) + "題!~")

exam(start)

input()