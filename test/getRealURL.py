# encoding=utf8
import requests
http_headers = { 'Accept': '*/*','Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
def get_real_url(url,try_count = 1):
    if try_count > 3:
        return url
    try:
        rs = requests.get(url,headers=http_headers,timeout=3)
        # print(rs.status_code)
        if rs.status_code > 400:
            return get_real_url(url,try_count+1)
        return rs.url
    except:
        return get_real_url(url, try_count + 1)

# baiduurl= 'https://www.baidu.com/link?url=d-zIZAUaGPjitWmmq8mS8c3xgqARRriuOUA5rmNxoMDbj3t8-IJc7H3SIbWvjqBLiBQWMiBDUP9uyqQNLfKFX_&wd=&eqid=b521e4a600081d3a000000065cf62f60'
# baiduuul= 'https://www.baidu.com/link?url=CqpnWE-4XqeiOgpeAFrPGzPrjSgmZbDXgIzHuJR1Qbi0yjJVrFkz9S873Qf1TT2W0q7aVW9PC7ZecvjttDdhAa&wd=&eqid=8f79da28002a05ba000000065cf62627'
# baidulll= 'https://www.baidu.com/link?url=MG-VGqpe91mLDxUp36Hm-ke-kQ97exjdpKBRymGKktKzHBUBCb8DIfDJi04nzz_n7DnNepKalvq3U01uYwl3Bq&wd=&eqid=bd68731900014a3a000000065cf62e01'
# real_url=get_real_url('http://www.baidu.com/link?url=y74--gie25AmGUaZ3W-voN-R7TFXin9GqgZJ0x8aLMLSoQIbo-workf-e8oSaNb8rEpLsQWyyOwuK5iRJaZ8hK',1)
# print(real_url)