# # # # from rest_framework import generics
# # # from .models import CustomUser
# # # from .serializers import UserSerializer



# # # from rest_framework import generics
# # # from rest_framework.response import Response
# # # from rest_framework import status
# # # from .serializers import RegisterSerializer

# # # class UserListView(generics.ListAPIView):
# # #     queryset = CustomUser.objects.all()
# # #     serializer_class = UserSerializer

# # # class RegisterView(generics.CreateAPIView):
# # #     serializer_class = RegisterSerializer

# # #     def create(self, request, *args, **kwargs):
# # #         # Call the parent class's create method to handle the registration process
# # #         response = super().create(request, *args, **kwargs)
# # #         return Response(response.data, status=status.HTTP_201_CREATED)


# # # from rest_framework.views import APIView
# # # from rest_framework.response import Response
# # # from rest_framework import status
# # # from django.contrib.auth import authenticate
# # # from rest_framework_simplejwt.tokens import RefreshToken
# # # from django.contrib.auth.models import User
# # # from .serializers import UserSerializer, LoginSerializer, PasswordResetSerializer
# # # from django.core.mail import send_mail
# # # from django.conf import settings

# # # # Register view
# # # class RegisterView(APIView):
# # #     def post(self, request):
# # #         serializer = UserSerializer(data=request.data)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # # # Login view
# # # class LoginView(APIView):
# # #     def post(self, request):
# # #         serializer = LoginSerializer(data=request.data)
# # #         if serializer.is_valid():
# # #             user = serializer.validated_data['user']
# # #             refresh = RefreshToken.for_user(user)
# # #             return Response({
# # #                 'access': str(refresh.access_token),
# # #                 'refresh': str(refresh),
# # #             })
# # #         return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

# # # # Password Reset view (initiate email)
# # # class PasswordResetView(APIView):
# # #     def post(self, request):
# # #         serializer = PasswordResetSerializer(data=request.data)
# # #         if serializer.is_valid():
# # #             email = serializer.validated_data['email']
# # #             try:
# # #                 user = User.objects.get(email=email)
# # #                 # Sending a password reset email
# # #                 reset_link = f"http://localhost:8000/reset-password/{user.id}/"
# # #                 send_mail(
# # #                     'Password Reset',
# # #                     f'Click here to reset your password: {reset_link}',
# # #                     settings.DEFAULT_FROM_EMAIL,
# # #                     [email],
# # #                 )
# # #                 return Response({"message": "Password reset email sent."}, status=status.HTTP_200_OK)
# # #             except User.DoesNotExist:
# # #                 return Response({"error": "Email not found."}, status=status.HTTP_404_NOT_FOUND)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # from rest_framework.permissions import AllowAny
# # from drf_yasg.utils import swagger_auto_schema
# # from django.contrib.auth import get_user_model, authenticate
# # from django.core.mail import send_mail
# # from django.contrib.auth.tokens import default_token_generator
# # from rest_framework.permissions import IsAuthenticated
# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from rest_framework import status
# # from .serializers import UserSerializer, PasswordChangeSerializer
# # from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# # # User Registration
# # # class RegisterView(APIView):
# # #     @swagger_auto_schema(
# # #         operation_description="Register a new user with a username, email, and password.",
# # #         request_body=UserSerializer,
# # #         responses={
# # #             201: 'User registered successfully!',
# # #             400: 'Bad request. Validation error.',
# # #         }
# # #     )
# # #     def post(self, request):
# # #         serializer = UserSerializer(data=request.data)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # # class RegisterView(APIView):
# # #     permission_classes = [AllowAny]  # Allow unauthenticated access to the registration endpoint
    
# # #     @swagger_auto_schema(
# # #         operation_description="Register a new user with a username, email, and password.",
# # #         request_body=UserSerializer,  # This will automatically generate form fields in Swagger UI
# # #         responses={
# # #             201: 'User registered successfully!',
# # #             400: 'Bad request. Validation error.',
# # #         }
# # #     )
# # #     def post(self, request):
# # #         """
# # #         POST method to register a new user.
# # #         - The request should contain `username`, `email`, and `password`.
# # #         """
# # #         serializer = UserSerializer(data=request.data)
        
# # #         if serializer.is_valid():
# # #             serializer.save()  # Save the user instance
# # #             return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # class RegisterView(APIView):
# #     permission_classes = [AllowAny]
# #     def post(self, request, *args, **kwargs):
# #         serializer = UserSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()  # This will call the create method in the serializer
# #             return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # # Login (JWT Authentication)
# # class CustomTokenObtainPairView(TokenObtainPairView):
# #     pass

# # class CustomTokenRefreshView(TokenRefreshView):
# #     pass

# # # Forgot Password - Send Reset Email
# # class ForgotPasswordView(APIView):
# #     def post(self, request):
# #         email = request.data.get('email')
# #         try:
# #             user = get_user_model().objects.get(email=email)
# #             token = default_token_generator.make_token(user)
# #             reset_url = f'http://example.com/reset-password/{token}/'
# #             send_mail(
# #                 'Password Reset Request',
# #                 f'Use this link to reset your password: {reset_url}',
# #                 'no-reply@example.com',
# #                 [email]
# #             )
# #             return Response({"message": "Password reset email sent!"}, status=status.HTTP_200_OK)
# #         except get_user_model().DoesNotExist:
# #             return Response({"message": "Email not found."}, status=status.HTTP_400_BAD_REQUEST)

# # # Reset Password - Using token
# # class ResetPasswordView(APIView):
# #     def post(self, request, token):
# #         new_password = request.data.get('new_password')
# #         try:
# #             uid = default_token_generator.check_token(token)
# #             if not uid:
# #                 return Response({"message": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
# #             user = get_user_model().objects.get(id=uid)
# #             user.set_password(new_password)
# #             user.save()
# #             return Response({"message": "Password has been reset!"}, status=status.HTTP_200_OK)
# #         except Exception as e:
# #             return Response({"message": "Error resetting password."}, status=status.HTTP_400_BAD_REQUEST)

# # # Change Password
# # class ChangePasswordView(APIView):
# #     permission_classes = [IsAuthenticated]

# #     def post(self, request):
# #         old_password = request.data.get('old_password')
# #         new_password = request.data.get('new_password')

# #         user = authenticate(username=request.user.username, password=old_password)
# #         if user:
# #             user.set_password(new_password)
# #             user.save()
# #             return Response({"message": "Password changed successfully!"}, status=status.HTTP_200_OK)
# #         return Response({"message": "Old password is incorrect!"}, status=status.HTTP_400_BAD_REQUEST)

# # # Get All Users (For Admin only)
# # class GetAllUsersView(APIView):
# #     permission_classes = [IsAuthenticated]  # Admin check can be added here

# #     def get(self, request):
# #         users = get_user_model().objects.all()
# #         return Response({"users": [user.username for user in users]}, status=status.HTTP_200_OK)

# # # Activate/Deactivate User
# # class ActivateDeactivateUserView(APIView):
# #     permission_classes = [IsAuthenticated]

# #     def patch(self, request, user_id):
# #         try:
# #             user = get_user_model().objects.get(id=user_id)
# #             user_profile = user.userprofile
# #             user_profile.is_active = not user_profile.is_active
# #             user_profile.save()
# #             action = "activated" if user_profile.is_active else "deactivated"
# #             return Response({"message": f"User {action}!"}, status=status.HTTP_200_OK)
# #         except get_user_model().DoesNotExist:
# #             return Response({"message": "User not found!"}, status=status.HTTP_404_NOT_FOUND)

# # # Admin Approve or Reject User
# # class ApproveRejectUserView(APIView):
# #     permission_classes = [IsAuthenticated]

# #     def patch(self, request, user_id):
# #         try:
# #             user = get_user_model().objects.get(id=user_id)
# #             if user.userprofile.role == 'super_admin':
# #                 return Response({"message": "Cannot approve or reject a super admin!"}, status=status.HTTP_403_FORBIDDEN)

# #             user.userprofile.is_verified = not user.userprofile.is_verified
# #             user.userprofile.save()

# #             action = "approved" if user.userprofile.is_verified else "rejected"
# #             return Response({"message": f"User {action}!"}, status=status.HTTP_200_OK)
# #         except get_user_model().DoesNotExist:
# #             return Response({"message": "User not found!"}, status=status.HTTP_404_NOT_FOUND)


# from rest_framework import status
# from rest_framework.response import Response
# from .serializers import UserSerializer

# from rest_framework.permissions import AllowAny
# from rest_framework.decorators import api_view, permission_classes

# @api_view(['POST'])
# @permission_classes([AllowAny]) 
# def register_user(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({"message": "User created successfully", "user": serializer.data}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework.permissions import AllowAny
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth import authenticate
# from django.core.mail import send_mail
# from rest_framework.permissions import IsAdminUser
# from rest_framework_simplejwt.tokens import RefreshToken
# from .models import User, Role
# from .serializers import (
#     UserRegistrationSerializer,
#     CustomTokenObtainPairSerializer,
#     ForgotPasswordSerializer,
#     ResetPasswordSerializer,
#     UserSerializer,
# )


# # Register a New User
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def register_user(request):
#     serializer = UserRegistrationSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # Login with JWT
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def login_user(request):
#     serializer = CustomTokenObtainPairSerializer(data=request.data)
#     if serializer.is_valid():
#         return Response(serializer.validated_data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


# # Forgot Password API
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def forgot_password(request):
#     serializer = ForgotPasswordSerializer(data=request.data)
#     if serializer.is_valid():
#         email = serializer.validated_data['email']
#         user = User.objects.filter(email=email).first()
#         if user:
#             # Example email logic (replace with actual token generation)
#             reset_token = "sample-reset-token"  # You would generate a real token here.
#             send_mail(
#                 'Reset Password',
#                 f'Your reset token is: {reset_token}',
#                 'noreply@venuebooking.com',
#                 [email],
#             )
#             return Response({"message": "Password reset token sent."}, status=status.HTTP_200_OK)
#         return Response({"error": "Email not found."}, status=status.HTTP_404_NOT_FOUND)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # Reset Password API
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def reset_password(request):
#     serializer = ResetPasswordSerializer(data=request.data)
#     if serializer.is_valid():
#         token = serializer.validated_data['token']
#         new_password = serializer.validated_data['new_password']
#         # Verify token and update password logic here (replace with real implementation)
#         user = User.objects.first()  # Example user (replace with token logic)
#         user.set_password(new_password)
#         user.save()
#         return Response({"message": "Password reset successful."}, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # List All Users (Admin Only)
# @api_view(['GET'])
# @permission_classes([IsAdminUser])
# def list_users(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# # Get User by ID (Admin Only)
# @api_view(['GET'])
# @permission_classes([IsAdminUser])
# def get_user_by_id(request, user_id):
#     try:
#         user = User.objects.get(id=user_id)
#         serializer = UserSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except User.DoesNotExist:
#         return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)


# views.py
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import User, Role
from .serializers import (
    UserRegistrationSerializer,
    CustomTokenObtainPairSerializer,
    ForgotPasswordSerializer,
    ResetPasswordSerializer,
    UserSerializer,
)

@swagger_auto_schema(method='post', request_body=UserRegistrationSerializer)
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='post', request_body=CustomTokenObtainPairSerializer)
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    print(request.data)
    serializer = CustomTokenObtainPairSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

@swagger_auto_schema(method='post', request_body=ForgotPasswordSerializer)
@api_view(['POST'])
@permission_classes([AllowAny])
def forgot_password(request):
    serializer = ForgotPasswordSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        user = User.objects.filter(email=email).first()
        if user:
            reset_token = "sample-reset-token"  # You would generate a real token here.
            send_mail(
                'Reset Password',
                f'Your reset token is: {reset_token}',
                'noreply@venuebooking.com',
                [email],
            )
            return Response({"message": "Password reset token sent."}, status=status.HTTP_200_OK)
        return Response({"error": "Email not found."}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='post', request_body=ResetPasswordSerializer)
@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password(request):
    serializer = ResetPasswordSerializer(data=request.data)
    if serializer.is_valid():
        token = serializer.validated_data['token']
        new_password = serializer.validated_data['new_password']
        user = User.objects.first()  # Replace with token-based user retrieval
        user.set_password(new_password)
        user.save()
        return Response({"message": "Password reset successful."}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='get', responses={200: UserSerializer(many=True)})
@api_view(['GET'])
@permission_classes([IsAdminUser])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='get', responses={200: UserSerializer})
@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_user_by_id(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
