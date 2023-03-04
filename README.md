# 1. 创建虚拟环境并安装 Django 和 mysqlclient
```shell
python3 -m venv myproject-env
source myproject-env/bin/activate
pip install django mysqlclient
```
# 2. 创建 Django 项目
```shell
django-admin startproject myproject
cd myproject
```

# 3. 配置数据库
打开 myproject/settings.py 文件，添加如下代码
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '',
    }
}

```

# 4. 迁移数据库
```bash
python manage.py migrate
```

# 5. 创建应用程序

```bash
python manage.py startapp myapp
```

# 6. 编写视图
打开 myapp/views.py 文件，添加如下代码：
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")
```

# 7. 编写 URLconf
打开 myproject/urls.py 文件，添加如下代码：
```python
from django.urls import path
from myapp.views import index

urlpatterns = [
    path('', index, name='index'),
]
```

# 8. 运行服务器
```
python manage.py runserver
```