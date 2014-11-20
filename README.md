#用户脚本更新

* 服务器地址：　xxx.xxx.xx.75

* 账号密码:  dlrc

* 固件目录：/usr/local/nginx/html/download/firmware

* 配置文件目录：/usr/local/nginx/html/download/userOptFile


## firmware需要更新mysql数据库


使用update.py生成update.sql文件，用mysql执行它

```
mysql -u dlrc -p

source update.sql
```