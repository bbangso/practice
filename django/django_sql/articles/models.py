from django.db import models

# Create your models here.
class Reporter(models.Model):
    username = models.CharField(max_length=10)

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)


# on_delete
# * CASCADE : 해당 객체가 삭제 되었을때 참조하는 객체 모두 삭제
# * PROTECT : 참조하는 객체가 존재하면, 삭제 금지
# * SET_NULL : NULL값으로 치환. NOT NULL 옵션이 있는 경우는활용 할 수 없음
# * SET_DEFAULT : 디폴트 값을 참조하게끔 한다