

# Django CURD

## 프로젝트및 app 설정

### 1. 프로젝트생성

```

```

### 2. 프로젝트설정 (settings.py)

```python
# settings.py
```

### 3. app 생성(articles)

## Model 정의

### 1. model 정의
``` python
# models.py
class Article(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

* `models.Model`을 상속받은 클래스를 생성한다.
* 속성은 내가 구성하고 싶은 테이블의 컬럼의 이름을 지정하고, 데이터타입에 맞춰서 필드를 정의한다.

### 2. 마이그레이션

* 정의된 모델을 데이터베이스에 반영하기 위해서는 마이그레이션 명령어를 통해 마이그레이션 파일을 생성한다.

  ``` python
  $ pyhton manage.py makemigrations
  ```

* 마이그레이션 파일은 모델의 변경사항을 관리한다.

* 생성된 마이그레이션 파일을 데이터베이스에 반영하기 위해서는 아래의 명령어를 입력한다.

  ```python
  $ python manage.py migrate
  ```

  

## Django ORM

> 기본적인 데이터베이스 조작은 CURD

### 1. 생성

```python
article = Article()
article.title = '제목'
article.content = '내용'
article.save()
```

### 2. 조회

```python
Article.objects.all()
Article.objects.get(id=1)
```

### 3. 수정

```python
a1 = Article.objects.get(id=1)
a1.title = '제목 수정'
a1.save()
```

### 4. 삭제

``` python
a1 = Article.objects.get(id=1)
a1.delete()
```



