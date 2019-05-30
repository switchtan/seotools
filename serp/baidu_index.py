from urllib.request import urlopen
import ssl
import urllib
import re
def get(url):
	ssl._create_default_https_context = ssl._create_unverified_context
	resource = urllib.request.urlopen(url).read()
	content = str(resource, 'utf-8', 'ignore')
	return content

list1 = ['0008mu.com', 'img369.cn', '1111vv.com', '66io.cn','33tm.cn','pk10kaijiang8.com','bismara22.com']


def get_index_baidu(site):
	serp= get("http://www.baidu.com/s?wd=site:"+site)
	#print(serp)
	pattern  = re.compile('找到相关结果数约(\d+)个')
	m= pattern.search(serp)
	if m is not None:
		result = m.group(1)
		#print(m.group(1))
		print(site+' 收录数：'+result)
	else:
		print(site+' 收录数：0')

for item in list1:
	get_index_baidu(item)

