## OMS环境需求:
<pre>
python 2.7.x
django 1.7.11
requests
IPy
PyYAML
</pre>

## salt_api.conf：
<pre>
external_auth:
  pam:
    test:
      - .*
      - '@wheel'
      - '@runner'
      - 'grains.*'
      - 'status.*'
      - 'sys.*'
      - 'test.*'

rest_cherrypy:
  port: 7000
  host: 0.0.0.0
  ssl_crt: /etc/ssl/private/cert.pem
  ssl_key: /etc/ssl/private/key.pem
  webhook_disable_auth: True
  webhook_url: /hook
</pre>
## settings.py里面的注意事项:
<pre>
MASTER_IP = '192.168.2.229'
# master主机名需要注意的是这个主机名必须是设置的minion id对应,包括资产管理里面的主机名(注意不是可见名或别名)
MASTER_HOST = 'test'
</pre>

打开浏览器输入http://ipaddress/dashboard/

## 通过salt-api添加服务器

saltstack --> minion菜单

获取信息按钮，可将minion信息存入数据库！

## 系统设置
## git仓库设置
## saltstack功能介绍
## 安装软件包

