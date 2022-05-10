import urllib.request 
import requests
from bs4 import BeautifulSoup
import os
#找真正的網址
print("請輸入網址：")
url = input()
#給他信封並署名
response = requests.get(url,cookies = {"over18":"1"})
html = BeautifulSoup(response.text, "lxml")
content = html.find("div", id="main-content")
metas = content.find_all("a")
for x in range(len(metas)):
    pic_url = metas[x].get("href") #獲得metas中href標籤後的網址
    dirname = "妹圖/"
    if not os.path.exists("妹圖"):
        os.mkdir(dirname)
    else:
        pass
    fname = "妹圖/" + pic_url.split("/")[-1]
    urllib.request.urlretrieve(pic_url,fname)
print("完成！請關閉視窗。")