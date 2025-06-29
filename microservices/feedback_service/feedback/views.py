from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def feedback_service_health(request):
    """Health check endpoint for feedback service"""
    return Response({
        'service': 'feedback_service',
        'status': 'healthy',
        'message': 'Feedback service is running'
    }, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def feedback_list(request):
    """Feedback management endpoint"""
    if request.method == 'GET':
        return Response({
            'service': 'feedback_service',
            'endpoint': 'feedback_list',
            'feedback': []  # This would contain actual feedback data
        })
    elif request.method == 'POST':
        return Response({
            'service': 'feedback_service',
            'message': 'Feedback created successfully'
        }, status=status.HTTP_201_CREATED)
