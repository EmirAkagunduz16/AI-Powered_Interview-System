from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.feedback_service_health, name='feedback_service_health'),
    path('feedback/', views.feedback_list, name='feedback_list'),
] 