import urllib.request as request
import json
with request.urlopen("https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire") as file:
    data = json.load(file)
namelist = data["result"]["results"]
Namelist = []
n = 0
for name in namelist:
    if n < len(namelist):
        Namelist.append(str(n+1)+ ". " + namelist[n]["公司名稱"])
        n += 1
with open("company_name.txt",mode = "w", encoding="utf-8") as NF:
    for w in range(len(Namelist)):
        NF.write(Namelist[w] + "\n")
print("完成!")