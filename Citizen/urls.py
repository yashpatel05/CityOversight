from django.contrib import admin
from django.urls import path
from Citizen import citizen_views

urlpatterns = [
    path('index/', citizen_views.index),
    path('logout/', citizen_views.logout),
    path('profile/', citizen_views.profile),

    path('garbage_report_pending/', citizen_views.garbage_report_pending_show),
    path('complain_pending/', citizen_views.complain_pending_show),
    path('garbage_report_solved/', citizen_views.garbage_report_solved_show),
    path('complain_solved/', citizen_views.complain_solved_show),

    path('insert_new_complain/', citizen_views.insert_new_complain),

    path('update_user_profile_show/', citizen_views.update_user_profile_show),
    path('update_my_complain_show/<int:id>', citizen_views.update_my_complain_show),
    path('my_complain_show/', citizen_views.my_complain_show),

    path('edit_user_profile/', citizen_views.edit_user_profile),
    path('edit_user_profile_photo/', citizen_views.edit_user_profile_photo),
    path('edit_my_complain/<int:id>', citizen_views.edit_my_complain),

    path('delete_my_complain/<int:id>', citizen_views.delete_my_complain),

    path('remove_user_profile_photo/', citizen_views.remove_user_profile_photo),

    path('ajax/load-cities/', citizen_views.load_city, name='ajax_load_city'),
]