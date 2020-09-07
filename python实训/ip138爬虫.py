import requests
ip = input("输入要解析的ip")
url = "http://m.ip138.com/ip.asp"
params={"ip":"www.baidu.com"}
headers = {"User-Agent":"Mozilla/4.0(compatible: MSIE 7.0: Windows NT 10.0:WOW6:Trident/7.0)"}
result = requests.get(url,params=params,headers=headers)
if result.status_code==200:
   result.encoding=result.apparent_encoding
   fw=open("ipsearch.html","wb")
   fw.write(reuslt.content)
   fw.close()
else:
    print(result.status_code)
