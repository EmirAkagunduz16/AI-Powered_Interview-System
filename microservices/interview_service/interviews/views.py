from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def interview_service_health(request):
    """Health check endpoint for interview service"""
    return Response({
        'service': 'interview_service',
        'status': 'healthy',
        'message': 'Interview service is running'
    }, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def interviews_list(request):
    """Interview management endpoint"""
    if request.method == 'GET':
        return Response({
            'service': 'interview_service',
            'endpoint': 'interviews_list',
            'interviews': []  # This would contain actual interview data
        })
    elif request.method == 'POST':
        return Response({
            'service': 'interview_service',
            'message': 'Interview created successfully'
        }, status=status.HTTP_201_CREATED)
