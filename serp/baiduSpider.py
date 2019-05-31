# encoding=utf8
import requests

url='http://www.33tm.cn/'

send_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 baiduspider/10.4.3505.400",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"
}#伪装成浏览器
response=requests.get(url,headers=send_headers)#访问
print(response.text)
response.close()#访问后就关闭访问
