import urllib.request as request
import json
import bs4
src = "https://www.ptt.cc/bbs/movie/index.html"
#建立 request 物件，附加 Headers 資訊
req = request.Request(src, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
    "cookie":"over18=1"
})
with request.urlopen(req) as response:
    data = response.read().decode("utf-8")

#利用 beautifulsoup 解析 html
root = bs4.BeautifulSoup(data,"html.parser")
title = root.find_all("div",class_="title")

for t in title:
  if t.a != None:
    print(t.a.string)

nextLink=root.find("a",string="‹ 上頁")
