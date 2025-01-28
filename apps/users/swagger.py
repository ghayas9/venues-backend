from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status

# ----------------------- Register API -----------------------
register_request = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username of the user'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL, description='Email of the user'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD, description='Password'),
        'confirm_password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD, description='Confirm password'),
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the user (optional)'),
    },
    required=['username', 'email', 'password', 'confirm_password'],
)

register_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'),
        'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
        'role': openapi.Schema(type=openapi.TYPE_STRING, description='Role'),
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name (optional)'),
    },
)

register_swagger = swagger_auto_schema(
    method='post',
    request_body=register_request,
    responses={
        status.HTTP_201_CREATED: register_response,
        status.HTTP_400_BAD_REQUEST: 'Validation errors',
    },
)

# ----------------------- Login API -----------------------
login_request = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL, description='Email'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD, description='Password'),
    },
    required=['password'],
)

login_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh token'),
        'access': openapi.Schema(type=openapi.TYPE_STRING, description='Access token'),
        'user': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'),
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
                'role': openapi.Schema(type=openapi.TYPE_STRING, description='Role'),
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name (optional)'),
            },
        ),
    },
)

login_swagger = swagger_auto_schema(
    method='post',
    request_body=login_request,
    responses={
        status.HTTP_200_OK: login_response,
        status.HTTP_401_UNAUTHORIZED: 'Invalid credentials',
        status.HTTP_400_BAD_REQUEST: 'Validation errors',
    },
)

# ----------------------- Forgot Password API -----------------------
forgot_password_request = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL, description='Email of the user'),
    },
    required=['email'],
)

forgot_password_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'message': openapi.Schema(type=openapi.TYPE_STRING, description='Success message'),
    },
)

forgot_password_swagger = swagger_auto_schema(
    method='post',
    request_body=forgot_password_request,
    responses={
        status.HTTP_200_OK: forgot_password_response,
        status.HTTP_404_NOT_FOUND: 'User not found',
        status.HTTP_400_BAD_REQUEST: 'Validation errors',
    },
)

# ----------------------- Verify OTP API -----------------------
verify_otp_request = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL, description='Email of the user'),
        'otp': openapi.Schema(type=openapi.TYPE_INTEGER, description='OTP sent to the user email'),
    },
    required=['email', 'otp'],
)

verify_otp_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'message': openapi.Schema(type=openapi.TYPE_STRING, description='OTP verification success message'),
    },
)

verify_otp_swagger = swagger_auto_schema(
    method='post',
    request_body=verify_otp_request,
    responses={
        status.HTTP_200_OK: verify_otp_response,
        status.HTTP_404_NOT_FOUND: 'Invalid OTP or email',
        status.HTTP_400_BAD_REQUEST: 'Validation errors',
    },
)

# ----------------------- Reset Password API -----------------------
reset_password_request = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL, description='Email of the user'),
        'otp': openapi.Schema(type=openapi.TYPE_INTEGER, description='OTP sent to the user email'),
        'new_password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD, description='New password'),
        'confirm_password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD, description='Confirm password'),
    },
    required=['email', 'otp', 'new_password', 'confirm_password'],
)

reset_password_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'message': openapi.Schema(type=openapi.TYPE_STRING, description='Password reset success message'),
    },
)

reset_password_swagger = swagger_auto_schema(
    method='post',
    request_body=reset_password_request,
    responses={
        status.HTTP_200_OK: reset_password_response,
        status.HTTP_404_NOT_FOUND: 'Invalid OTP or email',
        status.HTTP_400_BAD_REQUEST: 'Validation errors',
    },
)

# ----------------------- Admin Management APIs -----------------------
admin_id_parameter = openapi.Parameter(
    'admin_id', openapi.IN_PATH, description="ID of the admin", type=openapi.TYPE_INTEGER
)

user_id_parameter = openapi.Parameter(
    'user_id', openapi.IN_PATH, description="ID of the user", type=openapi.TYPE_INTEGER
)
