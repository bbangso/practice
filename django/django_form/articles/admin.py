from django.contrib import admin
from .models import Article

# Register your models here.

# admin site에 등록해줘
admin.site.register(Article)