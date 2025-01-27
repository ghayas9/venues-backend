# # from django.urls import path
# # from .views import UserListView

# # urlpatterns = [
# #     path('', UserListView.as_view(), name='user-list'),
# # ]


# # from django.urls import path
# # from .views import UserListView, RegisterView

# # urlpatterns = [
# #     path('', UserListView.as_view(), name='user-list'),
# #     path('register/', RegisterView.as_view(), name='register'),
# # ]


# # from django.urls import path
# # from .views import RegisterView, LoginView, PasswordResetView

# # urlpatterns = [
# #     path('register/', RegisterView.as_view(), name='register'),
# #     path('login/', LoginView.as_view(), name='login'),
# #     path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
# # ]

# from django.urls import path
# from . import views
# # from .views import (
# #     RegisterView, CustomTokenObtainPairView, ForgotPasswordView,
# #     ResetPasswordView, ChangePasswordView, GetAllUsersView,
# #     ActivateDeactivateUserView, ApproveRejectUserView
# # )

# urlpatterns = [
#     # path('register', RegisterView.as_view(), name='register'),
#     # path('login', CustomTokenObtainPairView.as_view(), name='login'),
#     # path('forgot-password', ForgotPasswordView.as_view(), name='forgot_password'),
#     # path('reset-password/<str:token>', ResetPasswordView.as_view(), name='reset_password'),
#     # path('change-password', ChangePasswordView.as_view(), name='change_password'),
#     # path('users/', GetAllUsersView.as_view(), name='get_all_users'),
#     # path('users/activate/<int:user_id>', ActivateDeactivateUserView.as_view(), name='activate_deactivate_user'),
#     # path('users/approve-reject/<int:user_id>', ApproveRejectUserView.as_view(), name='approve_reject_user'),
#     path('register/', views.register_user, name='register_user'),
# ]


# from django.urls import path
# from .views import (
#     register_user,
#     login_user,
#     forgot_password,
#     reset_password,
#     list_users,
#     get_user_by_id,
# )

# urlpatterns = [
#     path('register/', register_user, name='register'),
#     path('login/', login_user, name='login'),
#     path('forgot-password/', forgot_password, name='forgot-password'),
#     path('reset-password/', reset_password, name='reset-password'),
#     path('users/', list_users, name='list-users'),
#     path('users/<int:user_id>/', get_user_by_id, name='get-user-by-id'),
# ]


# urls.py
from django.urls import path
from .views import (
    register_user,
    login_user,
    forgot_password,
    reset_password,
    list_users,
    get_user_by_id,
)

urlpatterns = [
    path('register', register_user, name='register'),
    path('login', login_user, name='login'),
    path('forgot-password', forgot_password, name='forgot-password'),
    path('reset-password', reset_password, name='reset-password'),
    path('users', list_users, name='list-users'),
    path('users/<int:user_id>', get_user_by_id, name='get-user-by-id'),
]