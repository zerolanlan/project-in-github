import requests
from bs4 import BeautifulSoup


url="http://119.6.110.75:6677/loginAction.do"
data={"zjh":20171818,"mm":20171818}
header={"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)"}
session=requests.Session()
session.post(url,data)

classurl="http://119.6.110.75:6677/kclbAction.do?oper=kclb"
data2={
  "currentPage":1,
   "page":1,
   "pageSize": 20
  
}
response=session.post(classurl,data2)

soup=BeautifulSoup(response.content,"html.parser")
# soup.find("form")#找到第一个表格吧
# soup.find_all("form")#找到所有的表格
table=soup.find("table",class_="displayTag")
thead=table.find("thead")
# tablehead=table.thead
tbody=table.tbody
tableheads=thead.tr.find_all("th")
for th in tableheads:
	print(th['width'])
	print(th['class'])
	print(th.string)
tablerows=tbody.find_all('tr')
for tr in tablerows:
	tabledatas=tr.find_all('td')
	for td in tabledatas:
		if td.string !=None:
			print(td.string.strip())
		else:
			print("  ")

		
