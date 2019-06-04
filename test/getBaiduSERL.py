# encoding=utf8
import requests
import ssl
import urllib
import re
from bs4 import BeautifulSoup

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
} #定义头文件，伪装成浏览器
def get(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    resource = urllib.request.urlopen(url, data=None, timeout=10).read()
    content = str(resource, 'utf-8', 'ignore')
    return content
def getRealLink_re(url):
    rs = requests.get(url,headers=headers,timeout=10)
    matchObj = re.search(r'replace\(\"(.*)\"\)},timeout',rs.text)
    if matchObj:
        print ("matchObj.group() : ", matchObj.group())
        print ("matchObj.group(1) : ", matchObj.group(1))
        return matchObj.group(1)
        # print ("matchObj.group(2) : ", matchObj.group(2))
    else:
        print ("No match!!")
        print(rs.text)
        return None

from getRealURL import get_real_url
def getSERL(word = 'PK10开奖'):
    url = 'http://www.baidu.com.cn/s?wd=' + urllib.parse.quote(word) + '&pn=0'
    rs = requests.get(url,headers=headers,timeout=3)
    soup = BeautifulSoup(rs.text, 'html.parser')
    tagh3 = soup.find_all('div', attrs={'class':'f13'})
    for h3 in tagh3:
        href = h3.find('a').get('href')
        print('baidu url:'+href)
        rurl=get_real_url(href,1)
        if rurl !=None:
            # html=get(rurl)
            print('real url:'+rurl)
            matchObj = re.search(r'//(.*?)/',rurl)
            # print(matchObj.group(1))
            # print('http://ip.tool.chinaz.com/'+matchObj.group(1))
            html=get('http://ip.tool.chinaz.com/'+matchObj.group(1))
            soup = BeautifulSoup(html, 'html.parser')
            lis = soup.select("p.bor-b1s span")
            print(lis[3])
            print()
        # break
getSERL()

#www.gdwc365.com 观察

