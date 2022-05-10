USD = 3000
NTD = USD * 29.5
Rate = 1.04
t = 0
while NTD < 1000000:
    USD *= Rate
    NTD = USD * 29.5
    t += 1
y = t/7
print("當獲利率等於",Rate,"時，要超過一百萬要獲利",t,"次，約",round(y),"年時間")
