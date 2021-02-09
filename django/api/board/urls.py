from django.urls import path
from . import views

app_nmae = 'board'

urlpatterns = [
    path('json1/', views.article_list_1),
    path('json2/', views.article_list_2),
    path('json3/', views.article_list_3),
    path('ping/', views.ping),
    path('pong/', views.pong),
]