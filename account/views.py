from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializers import SignUpSerializer, UserSerializer

from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(method='POST', request_body=SignUpSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_employee(request):
    data = request.data
    serializer = SignUpSerializer(data=data)
    if serializer.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            employee = User.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
                username = data['email'],
                password = make_password(data['password'])
            )
            return Response({
                'status':'Employee created'
            }, status.HTTP_201_CREATED)
        else:
            return Response({
                'error':'User already exists.'
            }, status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_employees(request):
    employees = User.objects.all()
    serializer = UserSerializer(employees, many=True)
    return Response({
        'All employees':serializer.data
    }, status.HTTP_200_OK)


    

