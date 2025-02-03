from django.urls import path
from .views import (
    register, login_with_tokens, forgot_password, reset_password, verify_otp,
    get_all_admins, get_admin_by_id, approve_admin,
    get_all_users, get_user_by_id
)

urlpatterns = [
    path('register', register, name='register'),
    path('login', login_with_tokens, name='login'),
    path('forgot-password', forgot_password, name='forgot-password'),
    path('verify-otp', verify_otp, name='verify-otp'),
    path('reset-password', reset_password, name='reset-password'),
    path('admins', get_all_admins, name='get-all-admins'),
    path('admins/<int:admin_id>', get_admin_by_id, name='get-admin-by-id'),
    path('admins/<int:admin_id>/approve', approve_admin, name='approve-admin'),
    path('users', get_all_users, name='get-all-users'),
    path('users/<int:user_id>', get_user_by_id, name='get-user-by-id'),
]
