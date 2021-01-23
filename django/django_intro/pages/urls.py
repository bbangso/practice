from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('hello/', views.hello),
    path('lotto/', views.lotto),
    path('iam/', views.iam),
    path('lunch/', views.lunch),
    path('hi/<str:name>/', views.hi),
    path('sum/<int:a>/<int:b>/', views.add),
    path('posts/<int:num>/', views.posts),
]