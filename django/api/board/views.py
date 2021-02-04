from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.http.response import JsonResponse
from .models import Article

# Create your views here.

@require_GET
def article_list_1(request):
    articles = Article.objects.all()
    data = []
    for article in articles:
        data.append({
            "title" : article.title,
            "content" : article.content,
        })
    return JsonResponse(data, safe=False)

@require_GET
def article_list_2(request):
    from django.core import serializers
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return JsonResponse(data, safe=False)