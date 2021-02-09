import art

from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.http.response import JsonResponse


from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article
from .serializers import ArticleSerializer

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

@api_view(['GET'])
def article_list_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


def ping(request):
    return render(request, 'board/ping.html')

def pong(request):
    user_input = request.GET.get('inputText')
    art_text = art.text2art(user_input)
    data = {
        'success': True,
        'content': art_text,
    }
    return JsonResponse(data)