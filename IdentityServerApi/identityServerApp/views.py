from base64 import urlsafe_b64decode
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser, Role
from .serializers import UserSerializer



@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  login and roles views similarly
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, username=email, password=password)
    
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
#forgot password
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes


@api_view(['POST'])
def forgot_password(request):
    email = request.data.get('email')

    # Send a password reset email (use Django's built-in PasswordResetView)
    reset_view = PasswordResetView.as_view()
    response = reset_view(request)

    if response.status_code == status.HTTP_200_OK:
        return Response({"message": "Password reset email sent"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Password reset email not sent"}, status=status.HTTP_400_BAD_REQUEST)
   
#reset password
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

@api_view(['POST'])
def reset_password(request):
    uidb64 = request.data.get('uidb64')
    token = request.data.get('token')
    new_password = request.data.get('new_password')
    confirm_password = request.data.get('confirm_password')

    # Decode uidb64 to get user ID
    try:
        uid = urlsafe_b64decode(uidb64).decode()
    except (TypeError, ValueError, OverflowError):
        uid = None

    user = CustomUser.objects.get(id=uid)

    if default_token_generator.check_token(user, token) and new_password == confirm_password:
        user.set_password(new_password)
        user.save()
        return Response({"message": "Password reset successful"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Password reset failed"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['GET'])
def roles(request):
    roles = Role.objects.all()
    role_names = [role.name for role in roles]
    return Response(role_names, status=status.HTTP_200_OK)
