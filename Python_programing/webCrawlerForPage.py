#連續抓取頁面
import urllib.request as request
import json
import bs4

def getData(url):
  
  #建立 request 物件，附加 Headers 資訊
  req = request.Request(src, headers={
      "cookie":"over18=1",
      "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
  })
  with request.urlopen(req) as response:
      data = response.read().decode("utf-8")

  # print(data)

  #利用 beautifulsoup 解析 html
  root = bs4.BeautifulSoup(data,"html.parser")
  title = root.find_all("div",class_="title")

  for t in title:
    if t.a != None:
      print(t.a.string)



  #抓取上一頁網址, 先找 a 標籤(超連結標籤，然後找到目標字串，找出他的href)
  nextLink=root.find("a",string="‹ 上頁")
  return nextLink["href"]

for i in range(3):
  print("第",i+1,"頁")
  pageURL = "https://www.ptt.cc"+getData(pageURL)




