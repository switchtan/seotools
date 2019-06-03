# encoding=utf8
import requests
import re
baiduurl= 'https://www.baidu.com/link?url=3-7LQmpAZQiezPJLmYPsKxaEQM3ureLRRS_TXh-OjDXyoIR8jAwBdFRMl9ZQKoQaae1Wr_yl6AyKwz0dk9MiJ8Xtb1u4f4_FJ4kMGdzPEjO&wd=&eqid=d5abd5de00396861000000065cf5004a'
http_headers = { 'Accept': '*/*','Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}

def get_real_url(url,try_count = 1):
    if try_count > 3:
        return url
    try:
        rs = requests.get(url,headers=http_headers,timeout=10)
        print(rs.status_code)
        if rs.status_code > 400:
            return get_real_url(url,try_count+1)
        print(rs.text)
        matchObj = re.search(r'replace\(\"(.*)\"\)},timeout',rs.text)
        if matchObj:
            print ("matchObj.group() : ", matchObj.group())
            print ("matchObj.group(1) : ", matchObj.group(1))
            # print ("matchObj.group(2) : ", matchObj.group(2))
        else:
            print ("No match!!")
        return rs.url
    except:
        return get_real_url(url, try_count + 1)
real_url=get_real_url(baiduurl,1)
print(real_url)