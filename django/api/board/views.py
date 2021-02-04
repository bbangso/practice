from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Article

# Create your views here.

def article_list_1(request):
    articles = Article.objects.all()
    data = []
    for article in articles:
        data.append({
            "title" : article.title,
            "content" : article.content,
        })
    return JsonResponse(data, safe=False)