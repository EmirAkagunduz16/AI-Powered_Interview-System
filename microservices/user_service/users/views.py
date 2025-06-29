from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def user_service_health(request):
    """Health check endpoint for user service"""
    return Response({
        'service': 'user_service',
        'status': 'healthy',
        'message': 'User service is running'
    }, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def users_list(request):
    """User management endpoint"""
    if request.method == 'GET':
        return Response({
            'service': 'user_service',
            'endpoint': 'users_list',
            'users': []  # This would contain actual user data
        })
    elif request.method == 'POST':
        return Response({
            'service': 'user_service',
            'message': 'User created successfully'
        }, status=status.HTTP_201_CREATED)
