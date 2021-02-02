from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('<int:pk>/', views.detail, name='detail'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('<int:pk>/follow/', views.follow, name='follow'),
]