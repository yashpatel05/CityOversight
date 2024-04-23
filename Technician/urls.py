from django.contrib import admin
from django.urls import path
from Technician import technician_views

urlpatterns = [
    path('index/', technician_views.index),
    path('logout/', technician_views.logout),
    path('profile/', technician_views.profile),

    path('camera_info_show/', technician_views.camera_data_show),

    path('update_user_profile_show/', technician_views.update_user_profile_show),

    path('edit_user_profile/', technician_views.edit_user_profile),
    path('edit_user_profile_photo/', technician_views.edit_user_profile_photo),

    path('remove_user_profile_photo/', technician_views.remove_user_profile_photo),

    path('accept_camera/<int:id>', technician_views.accept_camera),

    path('change_camera_status/<int:id>', technician_views.change_camera_status),

]