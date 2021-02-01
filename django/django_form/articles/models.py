from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, Thumbnail

#FIll : 300* 300 (crop)
# FIT : 가장 긴 곳 을 300으로 맞추고 비율 유지
# Thumbnail: 라이브러리가 내부 알고리즘으로 깔끔하게 잘라줌

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()

    # 원본 저장 보여줄땐잘라서 
    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 100)],
                                      format='JPEG',
                                      options={'quality': 60})

    # 원본을 잘라서 저장
    # avatar_thumbnail = ProcessedImageField(upload_to='avatars',
    #                                        processors=[ResizeToFill(100, 50)],
    #                                        format='JPEG',
    #                                        options={'quality': 60})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)

    # settings.AUTH_USER_MODEL


class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)