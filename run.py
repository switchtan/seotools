import os
pathnow= os.getcwd()
x_path=pathnow.split('/')
#print(x_path)
domain_name=x_path[-1]
domain_path=domain_name.replace('.', '_')
print (domain_path)
f= open("wp-install.sht","r")
f_str=f.read()
f_str=f_str.replace('{mysqldb}',domain_path[0:16])
f_str=f_str.replace('{mysqluser}',domain_path[0:16])
f_str=f_str.replace('{mysqlpass}','guavaguava00')
f_str=f_str.replace('{siteurl}',domain_name)
f.close()
#print(f_str)
f1 = open('wp-install.sh','w')
f1.write(f_str)
f1.close()
os.system('chmod 777 wp-install.sh;./wp-install.sh')
