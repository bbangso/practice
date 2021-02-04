from django.shortcuts import  get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ArticleListSerializer, ArticleDetailSerializer, ArticleSerializer
from .models import Article

# Create your views here.

@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)    

    return Response(serializer.data)


@api_view(['GET'])
def article_detail(request, article_pk):
    print("asdasd")
    articles = get_object_or_404(Article, pk=article_pk)

    serializer = ArticleDetailSerializer(articles)
    return Response(serializer.data)

@api_view(['POST'])
def create_article(request):
    serializer = ArticleSerializer()

    return Response({
        "asdf":"asdf"
    })