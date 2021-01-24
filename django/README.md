

# Django

Django 프레임워크에 대한 정리.  

기본적인 CRUD 기능과 로그인 기능을 만들어 보는 것을 목표로 하며 그 과정을 상세히 기술하여 다음에 django 프레임워크를 사용할 일이 있을때 참고할 수 있도록 한다.

​    

## 설치 및 프로젝트 생성

Pip을 통해서 Django 프레임워크를 설치한다. 

```bash
$ pip install django
```

​    

다음과 같은 명령어를 통해 프로젝트와 app을 생성하고 서버를 실행시켜 본다.

```bash
$ django-admin stratproject [프로젝트명] # 프로젝트 생성
# manage.py 가 있는 폴더로 이동
$ python manage.py startapp [app명] # app 생성
$ python runserver 8080 # 서버 실행
```

작성일을 기준으로 로컬서버에 접속했을 때 초록색 로켓이 있는 웹페이지가 보인다면 성공이다.

​    

## Settings

Django 프로젝트와 app을 생성하면 각각의 폴더안에 몇가지 파일들이 생성된다. 각각의 기능은 본 실습을 하면서 필요해지면 그 때 설명을 한다. 우선 본 실습에 필요한 setting을 해보자.  

Aws에서 구동되는 서버에 접속을 할 수 있도록 프로젝트 폴더의 `setting.py`파일에서 `ALLOWED_HOSTS` 변수를 수정한다.

```python
# 프로젝트/setting.py
ALLOWED_HOSTS = [
    '*'   # 모든 host에서 접속할 수 있도록 *로 설정
]
```

​    

App을 생성했다면 `setting.py`에 반드시 등록해줘야 한다. 본인은 `hello` App을 생성했다.

```python
# 프로젝트/setting.pㅛ
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'hello',  # app 등록
]
```

​    

또한 언어와 시간을 대한민국으로 설정한다.

```python
# 프로젝트/setting.py
LANGUAGE_CODE = 'ko-KR'
TIME_ZONE = 'Asia/Seoul
```

기본 설정이 끝났다. 

​    

## 웹페이지 생성

###  Hello world!

`Root_URL/hello`에 요청을 보내면 'hello world!' 텍스트를 응답으로 하는 웹페이지를 생성해보면서 django의 기본 메커니즘을 익히도록 한다.  



#### 1. URL 설정

먼저, URL을  설정한다.

```python
# 프로젝트/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
]
```

```python
# hello app폴더에 urls.py 파일 생성
# hello/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]
```

`프로젝트/urls.py` 코드에서는 hello app의 urls.py를 참조한다는 의미이고 `hello/urls.py` 코드에서는 hello URL에 요청을 보내면  `views.index` 를 통해 응답하겠다는 의미이다.



#### 2. Views

URL설정을 마쳤으니 요청에 응답할 수 있도록 `views.index`의 코드를 작성하도록 한다.

```python
# hello/views.py
from django.shortcuts import render

def index(request):  	# request 인자가 반드시 필요하다.
    return render(request, 'hello/hi.html')
```

위 코드를 살펴보면 요청을 받아 `hello/hi,html` 의 파일을 렌더링하여 응답한다는 의미이다. 이제 `hello/hi.html` 의 코드를 작성해야한다. 

​    

#### 3. Templates

Django는 `render` method 사용시 두 번째 인자로 들어가는 `hello/hi.html` 파일을 각 app의 templates 폴더에서 찾도록 설정되어 있다. 따라서 각 app의 templates 폴더 안에 html 파일을 생성하면 된다. 



이 때 고려해야 할 것이 한가지 있다. 여러 app이 있을 경우 django는 각 app의 templates 폴더 안에 있는 html 파일이 어떤 app이 사용하는 html파일인지 모른다. 예를들어 hello app의 hi.html 파일과 bye app의 hi.html 파일이 있고 `render` 매서드의 두번째 인자로 `hi.html`을 넘겨주게 되면 django는 이 파일이 hello app에 작성된 코드인지 bye app에 작성된 코드인지 모른다. (setting.py 에 등록된 app순서대로 templates를 탐색하므로 먼저 등록된 app의 html 파일이 반환된다.)



이러한 혼란을 피하기위해 templates 폴더 안에 app의 이름과 같은 폴더를 하나 더 생성하여 `hello/hi.html` , `bye/hi.html`과 같이 구분 하도록 한다. 



고려해야할 것이 한가지 더 있다. Django를 사용하면서 여러 html 코드를 작성하게 될텐데 각 html 코드마다 중복되는 코드를 넣어야 할 일이 있다. 이럴 경우 코드 수정을 할 때 각 html 파일을 모두 수정해야하는 수고로움이 있다. 이러한 일을 좀 더 간편하게 하기 위해 Django는 `Template inheritance` 라는 강력한 기능을 제공하는데 이를 사용해서 `hi.html` 을 작성해 보자.



Root 디렉토리에 templates 폴더를 생성하고 그 안에 `base.html` 파일을 생성하고 다음과 같이 작성한다.

```html
<!--templates/base.html-->
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello</title>
</head>
<body>
    <h1>Template inheritance</h1>
    {% block body %}
    {% endblock %}
</body>
</html>
```





Django는 일반적으로 app 내에 있는 templates 폴더가 아닌 외부의 templates 폴더는 탐색하지 않는다. 따라서 `setting.py` 에 해당 경로를 등록해야한다.

```python
# 프로젝트/settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        
        # app내에 있는 폴더가 아닌 추가적으로 사용하고 싶은 폴더를 설정한다.
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')  # <-- 다음과 같이 추가
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```





이제 `hi.html` 코드를 작성한다.

```html
<!-- 
hello/templates/hello 폴더 생성
hello/templates/hello/hi.html 파일 생성
hello/templates/hello/hi.html
-->
{% extends 'base.html' %}
    
{% block body %}
<p>hello world!</p>
{% endblock %}
```

서버를 실행시키고 `프로젝트 url/hello` 에 요청을 보내면 `hello world!` 가 출력되는 것을 볼 수 있다.



