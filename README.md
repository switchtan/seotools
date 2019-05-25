系统目标：
* 跟踪优化情况
* 自动化建站
里程碑：
* dns 服务器 站点 收录 （信息集中显示）
* 自动建站（nginx）
* 站内统计 竞争对手分析

usecase:

多用户相关（为了以后可以出售）
* 0.1 用户登录
* 0.2 用户角色（seo leader，优化员，boss）

服务器相关
* 1.1 添加服务器（IP,用户名，密码）
* 1.2 添加服务器后台管理地址（url，用户名，密码）
* *1.3 服务器到期提醒  https://www.vultr.com/api/


域名相关
* 2.1 添加域名（url，服务器）
* 2.2 自动建站
* 2.3 监测收录（需要持续记录）
* 2.4 检测关键词排名 （需要持续记录）
* 2.5 接受搜索引擎蜘蛛来访数据（api接口） （需要持续记录）

竞争对手研究
* 8.1 添加网站（url，tdk自动获取，评语）
* 8.2 网站各项评分
* 8.3 黑帽方法



内容优化
* 15.1 tdk/c 匹配
* 15.2 阅读高10篇/ 阅读低10篇/
* 15.3 收录/不收录页面对比

可以运用的api
* 域名/dns：dnspod
* 网站统计：api
* 服务器：vultr


自动化安装脚本运行：
wget https://github.com/switchtan/seotools/archive/master.zip;
unzip master.zip ;
cp seotools-master/* ./ ;
python3 run.py ;
python3 plugins.py ;
