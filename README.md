# OMS环境需求:
<pre>
python 2.7.x
django 1.7.11
requests
IPy
PyYAML
</pre>

# salt_api.conf：
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
# 创建数据库及创建用户
<pre>
CREATE DATABASE `OMS` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci
</pre>
settings.py里面的注意事项:
<pre>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'OMS',
        'USER': 'mysql_user',
        'PASSWORD': 'mysql_password',
        'HOST': '192.168.2.215',
        'PORT': 3306,
    }
}
...... 省略N行

MASTER_IP = '192.168.2.229'
MASTER_HOST = 'test'    # master主机名需要注意的是这个主机名必须是设置的minion id对应,包括资产管理里面的主机名(注意不是可见名或别名)
</pre>

创建数据库和用户:
<pre>
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver 0.0.0.0:8000
</pre>
打开浏览器输入http://ipaddress/dashboard/
![dashboard](images/DAE2AF1E-6AE7-47EC-9DC4-3DDA4848B2E3.png)
# 通过salt-api添加服务器

saltstack --> minion菜单

获取信息按钮，可将minion信息存入数据库！

# 系统设置
# git仓库设置
# saltstack功能介绍
# 安装软件包

