from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.interview_service_health, name='interview_service_health'),
    path('interviews/', views.interviews_list, name='interviews_list'),
] 