from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.user_login, name='login'),
    path('register/', views.user_registration, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('post_create/', views.PostCreateViewSet.as_view({'get': 'list', 'post': 'create'}), name='post_create-list'),
    path('post_create/<int:pk>/', views.PostCreateViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='post_create-detail'),
    path('teligram-api/',views.send_telegram_api,name="teligram")

]