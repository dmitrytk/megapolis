import jwt
from django.conf import settings
from django.contrib.auth import user_logged_in
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler

from api.models import Employee
from api.serializers import EmployeeSerializer


# Логин
@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    try:
        username = request.data['username']
        password = request.data['password']

        user = Employee.objects.get(username=username, password=password)
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                serializer = EmployeeSerializer(user)
                user_details = {'user': serializer.data, 'token': token}
                user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)

            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'error': 'please provide a email and a password'}
        return Response(res)


# Данные пользователя
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user(request):
    current_user = request.user
    serializer = EmployeeSerializer(current_user)
    return JsonResponse(serializer.data)
