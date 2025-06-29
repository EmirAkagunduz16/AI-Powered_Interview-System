from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.user_service_health, name='user_service_health'),
    path('users/', views.users_list, name='users_list'),
] 