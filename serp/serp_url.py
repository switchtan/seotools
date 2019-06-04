# encoding=utf8
import requests
import re
baiduurl= 'https://www.baidu.com/link?url=3-7LQmpAZQiezPJLmYPsKxaEQM3ureLRRS_TXh-OjDXyoIR8jAwBdFRMl9ZQKoQaae1Wr_yl6AyKwz0dk9MiJ8Xtb1u4f4_FJ4kMGdzPEjO&wd=&eqid=d5abd5de00396861000000065cf5004a'
baiduuul= 'https://www.baidu.com/link?url=CqpnWE-4XqeiOgpeAFrPGzPrjSgmZbDXgIzHuJR1Qbi0yjJVrFkz9S873Qf1TT2W0q7aVW9PC7ZecvjttDdhAa&wd=&eqid=8f79da28002a05ba000000065cf62627'
baidulll= 'https://www.baidu.com/link?url=MG-VGqpe91mLDxUp36Hm-ke-kQ97exjdpKBRymGKktKzHBUBCb8DIfDJi04nzz_n7DnNepKalvq3U01uYwl3Bq&wd=&eqid=bd68731900014a3a000000065cf62e01'
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
real_url=get_real_url(baidulll,1)
print(real_url)