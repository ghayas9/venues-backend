from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser
from .serializers import (
    RegisterSerializer, LoginSerializer, ForgotPasswordSerializer,
    ResetPasswordSerializer, UserSerializer ,UpdateStatusUserSerializer
)
from .permissions import IsSuperAdmin
import random
from .swagger import (
    register_swagger, login_swagger, forgot_password_swagger,
    verify_otp_swagger, reset_password_swagger
)

# --------------------- Registration API ---------------------
@register_swagger
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """
    API for user registration.
    Accepts username, email, password, confirm_password, and name.
    Returns the created user's details.
    """
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "register successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --------------------- Login with Tokens API ---------------------
@login_swagger
@api_view(['POST'])
@permission_classes([AllowAny])
def login_with_tokens(request):
    """
    API for user login with username or email.
    Returns access and refresh tokens along with user details.
    """
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data.get('username')
        email = serializer.validated_data.get('email')
        password = serializer.validated_data['password']

        # Ensure at least one of username or email is provided
        if not username and not email:
            return Response({"message": "Either username or email must be provided."}, status=status.HTTP_400_BAD_REQUEST)

        user = None
        if username:
            user = CustomUser.objects.filter(username=username).first()
        elif email:
            user = CustomUser.objects.filter(email=email).first()

        if user and user.check_password(password) and user.status !='blocked':
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role,
                    "name": user.name
                }
            }, status=status.HTTP_200_OK)
        return Response({"message": "Invalid credentials or unactive"}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# --------------------- Forgot Password API ---------------------
@forgot_password_swagger
@api_view(['POST'])
@permission_classes([AllowAny])
def forgot_password(request):
    """
    API to send an OTP to the user's email for password reset.
    Accepts email and returns a success message if the user exists.
    """
    serializer = ForgotPasswordSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        try:
            user = CustomUser.objects.get(email=email)
            otp = random.randint(100000, 999999)
            user.otp = otp
            user.save()
            send_mail(
                "Password Reset OTP",
                f"Your OTP is {otp}",
                settings.DEFAULT_FROM_EMAIL,
                [email]
            )
            return Response({"message": "OTP sent to email."}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --------------------- Verify OTP API ---------------------
@verify_otp_swagger
@api_view(['POST'])
@permission_classes([AllowAny])
def verify_otp(request):
    """
    API to verify the OTP sent to the user's email.
    Accepts email and OTP.
    Returns success message if OTP is correct.
    """
    email = request.data.get('email')
    otp = request.data.get('otp')

    if not email or not otp:
        return Response({"message": "Email and OTP are required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = CustomUser.objects.get(email=email, otp=otp)
        return Response({"message": "OTP verified successfully."}, status=status.HTTP_200_OK)
    except CustomUser.DoesNotExist:
        return Response({"message": "Invalid OTP or email."}, status=status.HTTP_404_NOT_FOUND)


# --------------------- Reset Password API ---------------------
@reset_password_swagger
@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password(request):
    """
    API to reset the user's password after OTP verification.
    Accepts email, OTP, new_password, and confirm_password.
    Returns a success message if the password is reset successfully.
    """
    serializer = ResetPasswordSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']
        new_password = serializer.validated_data['new_password']
        confirm_password = serializer.validated_data['confirm_password']

        if new_password != confirm_password:
            return Response({"error": "Passwords do not match."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(email=email, otp=otp)
            user.set_password(new_password)
            user.otp = None
            user.save()
            return Response({"message": "Password reset successful."}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "Invalid OTP or email."}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --------------------- Get All Admins API ---------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_admins(request):
    """
    API to get a list of all admin users.
    Accessible only by super admins.
    """
    admins = CustomUser.objects.filter(role='admin')
    serializer = UserSerializer(admins, many=True)
    return Response(serializer.data)


# --------------------- Get Admin by ID API ---------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_admin_by_id(request, admin_id):
    """
    API to get details of a specific admin by ID.
    Accessible only by super admins.
    """
    try:
        admin = CustomUser.objects.get(id=admin_id, role='admin')
        serializer = UserSerializer(admin)
        return Response(serializer.data)
    except CustomUser.DoesNotExist:
        return Response({"error": "Admin not found."}, status=status.HTTP_404_NOT_FOUND)


# --------------------- Approve Admin API ---------------------
@api_view(['PUT'])
@permission_classes([AllowAny])
def approve_admin(request, admin_id):
    """
    API to approve a pending admin user.
    Accessible only by super admins.
    """
    try:
        user = CustomUser.objects.get(id=admin_id)
    except CustomUser.DoesNotExist:
        return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = UpdateStatusUserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Status updated successfully."}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --------------------- Get All Users API ---------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_users(request):
    """
    API to get a list of all users.
    Accessible only by super admins.
    """
    users = CustomUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# --------------------- Get User by ID API ---------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_by_id(request, user_id):
    """
    API to get details of a specific user by ID.
    Accessible only by super admins.
    """
    try:
        user = CustomUser.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except CustomUser.DoesNotExist:
        return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
