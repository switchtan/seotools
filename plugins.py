#!/usr/bin/python

import os
#delete-duplicate-posts
#list1 = ['disable-google-fonts','autoptimize','all-in-one-seo-pack', 'wp-super-cache','spiderdisplay','autoptimize','wp-baidu-submit','wptouch','baidu-submit-link','i3geek-mip','i3geek-baiduxzh','broken-link-checker']
list1=['wp-fastest-cache','disable-google-fonts','autoptimize']
str=""
for item in list1:
	str=str+"wget --quiet http://downloads.wordpress.org/plugin/"+item+".zip\n"
	str=str+"unzip -q "+item+".zip\n"
	str=str+"mv "+item+" ./wp-content/plugins/\n"


pathnow= os.getcwd()
x_path=pathnow.split('/')
domain_name=x_path[-1]
str = str+ 'curl http://'+domain_name+'/active_plugins.php'

print(str)

f = open('wp-plugins.sh','w')
f.write(str)
f.close()
os.system('rm -rf ./wp-content/plugins/*;chmod 777 wp-plugins.sh;./wp-plugins.sh')
