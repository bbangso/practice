from django.urls import path
from . import views

urlpatterns = [
    path('json1', views.article_list_1),
    path('json2', views.article_list_2),
]