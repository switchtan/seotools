#!/usr/bin/python

import os

list1 = ['all-in-one-seo-pack', 'wp-super-cache','spiderdisplay','wp-baidu-submit','wptouch','baidu-submit-link','i3geek-mip','i3geek-baiduxzh','broken-link-checker']
str="l\n"
for item in list1:
	str=str+"wget --quiet http://downloads.wordpress.org/plugin/"+item+".zip\n"
	str=str+"unzip -q "+item+".zip\n"
	str=str+"mv "+item+" ./wp-content/plugins/\n"
print(str)
f = open('wp-plugins.sh','w')
f.write(str)
f.close()
os.system('rm -rf ./wp-content/plugins/*;chmod 777 wp-plugins.sh;./wp-plugins.sh')
