from django.shortcuts import  get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ArticleSerializer
from .models import Article

# Create your views here.

@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)    

    return Response(serializer.data)
