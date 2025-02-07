# from django.urls import path
# from . import views

# urlpatterns = [
#     # -------------------- Admin Endpoints --------------------

#     # List all bookings (admin and super admin)
#     path('admin/', views.list_bookings, name='list-bookings'),

#     # Create a booking (admin and super admin)
#     path('admin/create/', views.create_booking, name='create-booking'),

#     # Retrieve, update, or delete a booking (admin and super admin)
#     path('admin/<int:booking_id>/', views.manage_booking, name='manage-booking'),

#     # -------------------- Public Endpoints --------------------

#     # List all confirmed bookings (public)
#     path('public/', views.public_list_bookings, name='public-list-bookings'),

#     # Retrieve a specific confirmed booking (public)
#     path('public/<int:booking_id>/', views.public_retrieve_booking, name='public-retrieve-booking'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    # -------------------- Admin Endpoints --------------------

    # List all bookings (admin and super admin)
    path('', views.list_bookings, name='list-bookings'),

    # Create a booking (admin and super admin)
    path('create', views.create_booking, name='create-booking'),

    # Retrieve, update, or delete a booking (admin and super admin)
    path('<int:booking_id>', views.retrieve_booking, name='retrieve-booking'),
    path('<int:booking_id>/update', views.update_booking, name='update-booking'),
    path('<int:booking_id>/delete', views.delete_booking, name='delete-booking'),

    # -------------------- Public Endpoints --------------------

    # List all confirmed bookings (public)
    path('public', views.public_list_bookings, name='public-list-bookings'),

    # Retrieve a specific confirmed booking (public)
    path('public/<int:booking_id>', views.public_retrieve_booking, name='public-retrieve-booking'),
]
